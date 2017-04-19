#!/usr/bin/env python3
import argparse
import sys

from formats import hdd

parser = argparse.ArgumentParser()
parser.add_argument("--comment", default='')
parser.add_argument("--sectorsize", type=int, default=512)
parser.add_argument("--size", type=int, required=True, help="size of the raw image in bytes")
parser.add_argument("cylinders", type=int)
parser.add_argument("heads", type=int)
parser.add_argument("sectors", type=int)
args = parser.parse_args()

if len(args.comment) >= 128:
    print("comment too long", file=sys.stderr)
    exit(1)

header = hdd.header.pack(
    magic=b"VHD1.00",
    comment=args.comment.encode("cp932"),
    cylinders=args.cylinders,
    heads=args.heads,
    sectors=args.sectors,
    sectorsize=args.sectorsize,
    totals=args.cylinders * args.heads * args.sectors,
    size=args.size
)
sys.stdout.buffer.write(header)
