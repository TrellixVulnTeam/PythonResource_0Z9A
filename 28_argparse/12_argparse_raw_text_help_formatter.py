#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""
"""

#end_pymotw_header
import argparse

parser = argparse.ArgumentParser(
    add_help=True,
    formatter_class=argparse.RawTextHelpFormatter,
    description="""
    description
        not
           wrapped""",
    epilog="""
    epilog
      not
         wrapped""",
)

parser.add_argument(
    '-a', action="store_true",
    help="""argument
    help is not
    wrapped
    """,
)

parser.print_help()
"""
(venv) huzhi@huzhideMacBook-Pro argparse % python 12_argparse_raw_text_help_formatter.py
usage: 12_argparse_raw_text_help_formatter.py [-h] [-a]

    description
        not
           wrapped

optional arguments:
  -h, --help  show this help message and exit
  -a          argument
                  help is not
                  wrapped


    epilog
      not
         wrapped
(venv) huzhi@huzhideMacBook-Pro argparse %
"""