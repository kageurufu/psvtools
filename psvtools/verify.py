import os
import sys
import hashlib
import codecs

from .psv import *

def verify_file(fp, op=sys.stdout):
	header = read_header(fp)
	filehash = codecs.encode(bytearray(header.hash), 'hex-codec').decode()

	image_offset = header.image_offset_sector * 512
	total_size = header.image_size
	fp.seek(0, os.SEEK_END)
	end_of_file = fp.tell()

	fp.seek(image_offset)
	
	sha256 = hashlib.sha256()
	
	while fp.tell() < end_of_file:
		sha256.update(fp.read(512))

	if end_of_file - image_offset < total_size:
		null_bytes = total_size - (end_of_file - image_offset)
		while null_bytes:
			sha256.update(b'\x00' * 512)
			null_bytes -= 512

	print('Expected: %s' % filehash)
	print('Image:    %s' % sha256.hexdigest())

	if filehash == sha256.hexdigest():
		print("Valid!")
		return True
	else:
		return False