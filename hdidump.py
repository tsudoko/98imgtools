#!/usr/bin/env python3
import argparse
import sys

import utils
from formats import hdi

parser = argparse.ArgumentParser()
parser.add_argument("infile")
args = parser.parse_args()

with open(sys.argv[1], "rb") as f:
    header = hdi.header.unpack(f.read(hdi.header.size))
    utils.dump(header._asdict())
