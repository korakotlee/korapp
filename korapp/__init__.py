"""
__init__.py
"""

__author__ = 'korakotlee'

# import sys
import os
import argparse
from pathlib import Path
from korapp import korgen
from korapp import kornew
from korapp import kordir
from korapp import kordoc

__version__ = "0.1.2"


def cli():
    parser = argparse.ArgumentParser(description='generate app from mind map.')
    parser.add_argument('command')
    parser.add_argument('app_name', nargs='?')
    parser.add_argument('-b', '--brain', default=Path(kordir.home+'/.brain'),
                        help='brain location')

    args = parser.parse_args()
    # command = 'help' if len(sys.argv) < 2 else sys.argv[1].lower()
    # check if new.mm in brain
    if args.command == 'new':
        new_mm = os.path.join(args.brain, 'new.mm')
        if not os.path.isfile(new_mm):
            print(f"!!! Error: cannot find brain in location: {args.brain}")
            return
        kornew.init(args.app_name, args.brain)
    elif args.command == 'gen':
        korgen.init()
    elif args.command == 'doc':
        kordoc.init()
    else:
        print('''
usage: korapp [-h] [-b BRAIN] command app_name

generate app from mind map.

positional arguments:
  command
  app_name

optional arguments:
  -h, --help            show this help message and exit
  -b BRAIN, --brain BRAIN
                        brain location
''')


if __name__ == "__main__":
    cli()
