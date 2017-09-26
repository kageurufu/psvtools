from __future__ import print_function
import sys
import hashlib
import io

from .psv import *


def find_end_of_data(fp):
    print("Starting search for end of data")
    fp.seek(0, os.SEEK_END)
    lastpos = fp.tell()
    searchres = 1 << 10

    while True:
        fp.seek(max(-512 * searchres, -512), os.SEEK_CUR)
        buf = fp.read(512)
        fp.seek(-len(buf), os.SEEK_CUR)

        if any(c for c in buf if c != b'\x00'):
            if searchres == 1:
                break
            else:
                searchres = searchres >> 2
                fp.seek(lastpos)
                print("")
        else:
            lastpos = fp.tell()
        print("\r>> Searching backwards from %08x" % (fp.tell()), end='')

    print("\nEnd of data at 0x%08x" % lastpos)
    return lastpos


def trim_file(fp, op=None):
    if op is None:
        print(fp.name)
        op = open(fp.name.replace('.psv', '.trimmed.psv'), 'wb', 0)

    psv_header = read_header(fp)

    if psv_header.flags & FLAG_TRIMMED:
        print("Already trimmed")
        return False

    start_of_data = psv_header.image_offset_sector * 512
    fp.seek(0, os.SEEK_END)
    file_size = fp.tell()
    midpoint = (file_size - start_of_data)

    if not psv_header.image_size:
        psv_header.image_size = file_size - start_of_data
    end_of_data = find_end_of_data(fp)

    psv_header.flags |= FLAG_TRIMMED

    fp.seek(0)
    op.write(fp.read(start_of_data))
    op.seek(0)
    op.write(psv_header)
    op.seek(start_of_data)

    i = 0
    while fp.tell() < end_of_data:
        op.write(fp.read(512))

        i += 1
        if i >= 100:
            print('\rWritten %d%%' % (fp.tell() * 100 // end_of_data), end='')
    print("Complete!            ")
