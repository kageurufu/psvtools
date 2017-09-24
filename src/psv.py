from __future__ import print_function

import ctypes
import contextlib
import os
import struct
import sys

PSV_MAGIC = 0x00565350
PSV_VERSION_V1 = 1
FLAG_TRIMMED = 1 << 0
FLAG_DIGITAL = 1 << 2
FLAG_COMPRESSED = 1 << 2
FLAG_LICENSED_ONLY = FLAG_TRIMMED | FLAG_DIGITAL


class PSVFileHeader(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
        ("magic", ctypes.c_uint32),
        ("version", ctypes.c_uint32),
    ]


class PSVFileHeaderV1(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
        ("magic", ctypes.c_uint32),
        ("version", ctypes.c_uint32),
        ("flags", ctypes.c_uint32),
        ("key1", ctypes.c_uint8 * 0x10),  # for klicensee decryption
        ("key2", ctypes.c_uint8 * 0x10),  # for klicensee decryption
        ("signature", ctypes.c_uint8 * 0x14),  # same as in RIF
        # optional consistancy check. sha256 over complete data (including any
        # trimmed bytes) if cart dump, sha256 over the pkg if digital dump.
        ("hash", ctypes.c_uint8 * 0x20),
        # if trimmed, this will be actual size
        ("image_size", ctypes.c_uint64),
        # image (dump/pkg) offset in multiple of 512 bytes. must be > 0 if
        # an actual image exists. == 0 if no image is included.
        ("image_offset_sector", ctypes.c_uint64),
        # ("headers", ctypes.c_opt_header[])# optional additional headers as defined by the flags
    ]

HEADER_VERSIONS = {
    1: PSVFileHeaderV1,
}


def read_header(fp):
    psv_version_header = PSVFileHeader()
    fp.seek(0)
    fp.readinto(psv_version_header)

    assert psv_version_header.magic == PSV_MAGIC, \
    	"Not a valid PSV file"
    assert psv_version_header.version in HEADER_VERSIONS, \
    	"Unknown header version %d" % psv_header.version

    fp.seek(0)

    psv_header = HEADER_VERSIONS[psv_version_header.version]()
    fp.readinto(psv_header)

    return psv_header
