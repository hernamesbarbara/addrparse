#!/usr/bin/env python
# -*- coding: utf-8 -*- 
"""cli.py
 
Usage:
    cli.py EMAIL [(-e | -A | -n | -w)] [-h]
 
Arguments:
    EMAIL                      Email address
 
Options:
    -e --email-only            Only return validated email address [default: true]
    -A --all                   Return all fields
    -n --display-name-only     Only return display name
    -w --website-only          Only return the website and ignore webmail
    -h --help                  Show help message

Examples:
    python scripts/cli.py "a@yhathq.com"
    python scripts/cli.py "Austin Ogilvie <a@yhathq.com>" -A
    python scripts/cli.py "Austin Ogilvie <a@yhathq.com>" -n

"""

import os
import sys
import json
from docopt import docopt
from addrparse import addr

def handle_arguments(args):
    if args.get("--outfile", "stdout") == "stdout":
        outfile = sys.stdout
    else:
        outfile = args["--outfile"]
    if args.get("--all", False):
        target = "--all"
    elif args.get("--display-name-only", False):
        target = "display_name"
    elif args.get("--website-only", False):
        target = "website"
    else:
        target = "email"
    return target, outfile

def main(arguments):
    target, outfile = handle_arguments(arguments)
    email_dict = addr.process_email_address(arguments.get("EMAIL"))
    if target != "--all":
        res = json.dumps(email_dict[target])
    else:
        res = json.dumps(email_dict)
    print >> outfile, res

if __name__ == "__main__":
    main(docopt(__doc__))
