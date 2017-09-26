import io
import hashlib
from psvtools.expand import expand_file

def test_expand():
	with open('test/trimmed.psv', 'rb') as of:
		expanded = io.BytesIO()
		expand_file(of, expanded)

	expanded.seek(0)
	assert hashlib.sha256(expanded.getvalue()).hexdigest() == '6aa9e3c9519a8b3fb9af1c64dfb0703b5cb665280fd87be1f57094b218751c2d'
