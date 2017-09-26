import io
import hashlib
from psvtools.trim import trim_file

def test_trim():
	with open('test/blank.psv', 'rb') as of:
		trimmed = io.BytesIO()
		trim_file(of, trimmed)

	trimmed.seek(0)
	assert hashlib.sha256(trimmed.getvalue()).hexdigest() == 'e642e1e8e6205bbcac769252c4200aa4af32f899564220e4dab7cb12668191bb'
