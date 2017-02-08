#!/usr/bin/env python3
import argparse
import sys

from formats import slh

parser = argparse.ArgumentParser()
parser.add_argument("--serial-number", default='')
parser.add_argument("--revision", default='')
parser.add_argument("--model-name", default='')
parser.add_argument("--sectorsize", type=int, default=512)
parser.add_argument("--size", type=int, required=True, help="size of the raw image in bytes")
parser.add_argument("cylinders", type=int)
parser.add_argument("heads", type=int)
parser.add_argument("sectors", type=int)
args = parser.parse_args()

header = slh.header.pack(
    magic=b"HDIM",
    cylinders=args.cylinders,
    heads=args.heads,
    sectors=args.sectors,
    sectorsize=args.sectorsize,
    size=args.size,
    serial_number=args.serial_number.encode("ascii"),
    revision=args.revision.encode("ascii"),
    model_name=args.model_name.encode("ascii")
)
sys.stdout.buffer.write(header)
