#!/usr/bin/env python3
import argparse
import sys

from formats import nhd

# T98-Next seems to always use 8 heads, 32 sectors, size/(heads*sectors*sectorsize) cylinders with a sectorsize of 512

parser = argparse.ArgumentParser()
parser.add_argument("--comment", default='')
parser.add_argument("cylinders", type=int)
parser.add_argument("heads", type=int)
parser.add_argument("sectors", type=int)
args = parser.parse_args()

if len(args.comment) >= 256:
    print("comment too long", file=sys.stderr)
    exit(1)

sectorsize = 512
header = nhd.header.pack(
    magic=b"T98HDDIMAGE.R0",
    comment=args.comment.encode("cp932"),
    raw_offset=nhd.header.size,
    cylinders=args.cylinders,
    heads=args.heads,
    sectors=args.sectors,
    sectorsize=sectorsize
)
sys.stdout.buffer.write(header)
