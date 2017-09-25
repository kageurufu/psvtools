from __future__ import print_function
import sys
import hashlib

from .psv import *
from .trim import find_end_of_data


def expand_file(fp, op=None):
    psv_header = read_header(fp)

    if not psv_header.flags & FLAG_TRIMMED:
        print("Not trimmed")
        return False

    start_of_data = psv_header.image_offset_sector * 512
    fp.seek(0, os.SEEK_END)
    file_size = fp.tell()
    midpoint = (file_size - start_of_data)

    if not psv_header.image_size:
        psv_header.image_size = file_size - start_of_data
    end_of_data = find_end_of_data(fp)

    psv_header.flags &= ~FLAG_TRIMMED

    fp.seek(0)
    op.write(fp.read(start_of_data))
    op.seek(0)
    op.write(psv_header)
    op.seek(start_of_data)

    i = 0
    while fp.tell() < psv_header.image_size:
        op.write(fp.read(512))

        i += 1
        if i >= 100:
            print('\rWritten %d%%' % (op.tell() * 100 // end_of_data), end='')

    print("Writing padding....")

    while op.tell() < start_of_data + psv_header.image_size:
        op.write('\x00' * 512)

    print("Complete!            ")
