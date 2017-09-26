import io
import hashlib
from psvtools.trim import trim_file

def test_trim():
	with open('test/blank.psv', 'rb') as of:
		trimmed = io.BytesIO()
		trim_file(of, trimmed)

	trimmed.seek(0)
	assert hashlib.sha256(trimmed.getvalue()).hexdigest() == 'b66fec166c91d94ceb08d52481ab2cb5f408ae9839cb65b0e6daa9c8ddee0912'
