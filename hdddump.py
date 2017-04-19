#!/usr/bin/env python3
import argparse

import utils
from formats import hdd

parser = argparse.ArgumentParser()
parser.add_argument("infile")
args = parser.parse_args()

with open(args.infile, "rb") as f:
    header = hdd.header.unpack(f.read(hdd.header.size))
    utils.dump(header._asdict())
    assert header.magic == b"VHD1.00\0", "magic check failed, this might not be an hdd file"
