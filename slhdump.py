#!/usr/bin/env python3
import argparse

import utils
from formats import slh

parser = argparse.ArgumentParser()
parser.add_argument("infile")

args = parser.parse_args()

with open(args.infile, "rb") as f:
    header = slh.header.unpack(f.read(slh.header.size))
    utils.dump(header._asdict())
    assert header.magic == b"HDIM", "magic check failed, this might not be a slh file"
