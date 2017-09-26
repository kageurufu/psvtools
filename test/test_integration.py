import hashlib
import io

from psvtools.trim import trim_file
from psvtools.expand import expand_file
from psvtools.verify import verify_file

def test_trim_verify():
	trimmed = io.BytesIO()
	with open('test/blank.psv', 'rb') as of:
		trim_file(of, trimmed)

	assert verify_file(trimmed)

def test_expand_verify():
	expanded = io.BytesIO()
	with open('test/trimmed.psv', 'rb') as of:
		expand_file(of, expanded)
	assert verify_file(expanded)

def test_trim_expand_equal():
	trimmed = io.BytesIO()
	expanded = io.BytesIO()

	with open('test/blank.psv', 'rb') as of:
		orig_digest = hashlib.sha256(of.read()).hexdigest()
		of.seek(0)
		trim_file(of, trimmed)
	trimmed.seek(0)
	expand_file(trimmed, expanded)
	assert hashlib.sha256(expanded.getvalue()).hexdigest() == orig_digest
