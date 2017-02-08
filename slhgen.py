#!/usr/bin/env python3
import argparse
import os
import sys

from formats import slh

parser = argparse.ArgumentParser()
parser.add_argument("--serial-number", default='')
parser.add_argument("--revision", default='')
parser.add_argument("--model-name", default='')
parser.add_argument("cylinders", type=int)
parser.add_argument("heads", type=int)
parser.add_argument("sectors", type=int)
parser.add_argument("infile")
args = parser.parse_args()

size = os.path.getsize(args.infile)

sectorsize = 512
header = slh.header.pack(
    magic=b"HDIM",
    cylinders=args.cylinders,
    heads=args.heads,
    sectors=args.sectors,
    sectorsize=sectorsize,
    size=size,
    serial_number=args.serial_number.encode("ascii"),
    revision=args.revision.encode("ascii"),
    model_name=args.model_name.encode("ascii")
)
sys.stdout.buffer.write(header)
