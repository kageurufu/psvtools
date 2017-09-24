# psvtrim
PSV file trimmer, restoration, and validation utility (Python)

# Current usage:

```bash
$ python -m src --help
usage: psvtools [-h] [-t | -e | -v] [-o OUTPUT] file

positional arguments:
  file                  psv file to operate on

optional arguments:
  -h, --help            show this help message and exit
  -t, --trim            Trim a psv file. This is the default behavior
  -e, --expand          Expand a trimmed psv file
  -v, --verify          Validate the checksum of a psv file
  -o OUTPUT, --output OUTPUT
                        output file to write to
```

