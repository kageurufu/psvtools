# psvtrim
PSV file trimmer, restoration, and validation utility (Python)

# Install

python setup.py

# Current usage:

```bash
$ psvtools --help
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

```bash
$ psvtrim --help
usage: psvtrim [-h] [-o OUTPUT] file

positional arguments:
  file                  psv file to operate on

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        output file to write to
```

```bash
$ psvexpand --help
usage: psvexpand [-h] [-o OUTPUT] file

positional arguments:
  file                  psv file to operate on

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        output file to write to
```

```bash
$ psverify --help
usage: psverify [-h] file

positional arguments:
  file        psv file to operate on

optional arguments:
  -h, --help  show this help message and exit
```

