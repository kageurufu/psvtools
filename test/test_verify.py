import gzip
from psvtools.verify import verify_file

def test_verify_expanded():
	with open('test/blank.psv', 'rb') as of:
		assert verify_file(of)

def test_verify_trimmed():
	with open('test/trimmed.psv', 'rb') as of:
		assert verify_file(of)