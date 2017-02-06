#!/usr/bin/env python3
import argparse

import utils
from formats import nhd

parser = argparse.ArgumentParser()
parser.add_argument("infile")
args = parser.parse_args()

with open(args.infile, "rb") as f:
    header = nhd.header.unpack(f.read(nhd.header.size))
    utils.dump(header._asdict())
    assert header.magic == b"T98HDDIMAGE.R0\0\0", "magic check failed, this might not be a nhd file"
