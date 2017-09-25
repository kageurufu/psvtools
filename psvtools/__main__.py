import argparse
import sys

from .trim import trim_file
from .expand import expand_file
from .verify import verify_file

def main(args=None):
    parser = argparse.ArgumentParser('psvtools')

    command = parser.add_mutually_exclusive_group()
    command.add_argument('-t', '--trim', dest='command', action='store_const', const=trim_file, help='Trim a psv file. This is the default behavior')
    command.add_argument('-e', '--expand', dest='command', action='store_const', const=expand_file, help='Expand a trimmed psv file')
    command.add_argument('-v', '--verify', dest='command', action='store_const', const=verify_file, help='Validate the checksum of a psv file')

    parser.add_argument('-o', '--output', type=argparse.FileType('wb', 0), help='output file to write to')
    parser.add_argument('file', type=argparse.FileType('r+b', 0), help='psv file to operate on')
    parser.set_defaults(command=trim_file)

    args = parser.parse_args()
    success = args.command(args.file, args.output)

    sys.exit(0 if success else 1)

def trim():
    parser = argparse.ArgumentParser('psvtrim')

    parser.add_argument('-o', '--output', type=argparse.FileType('wb', 0), help='output file to write to')
    parser.add_argument('file', type=argparse.FileType('r+b', 0), help='psv file to operate on')

    args = parser.parse_args()
    success = trim_file(args.file, args.output)

    sys.exit(0 if success else 1)

def expand():
    parser = argparse.ArgumentParser('psvexpand')

    parser.add_argument('-o', '--output', type=argparse.FileType('wb', 0), help='output file to write to')
    parser.add_argument('file', type=argparse.FileType('r+b', 0), help='psv file to operate on')

    args = parser.parse_args()
    success = expand_file(args.file, args.output)

    sys.exit(0 if success else 1)

def verify():
    parser = argparse.ArgumentParser('psverify')

    parser.add_argument('file', type=argparse.FileType('r+b', 0), help='psv file to operate on')

    args = parser.parse_args()
    success = verify_file(args.file)

    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()