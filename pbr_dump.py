#!/usr/bin/env python3
import argparse
import os

import utils

parser = argparse.ArgumentParser()
parser.add_argument("--sectorsize", type=int, default=512)
parser.add_argument("infile")
args = parser.parse_args()

common_fields = [
    ('jump', '3s'),
    ('oem_name', '8s'),
    ('sectorsize', 'H'),
    ('sectors_per_cluster', 'B'),
    ('reserved_sector', 'H'),
    ('fat_count', 'B'),
    ('root_count', 'H'),
    ('sector_count', 'H'),
    ('media_type', 'B'),
    ('fat_sectors', 'H'),
    ('sectors', 'H'),
    ('heads', 'H'),
    ('hidden_sectors', 'I'),
    ('double_sectors', 'I'),
]

f16_fields = [
    ('os_data', '3s'),
    ('volume_serial', 'I'),
    ('volume_label', '11s'),
    ('fs', '8s'),
]

f32_fields = [
    ('double_fat_sector_count', 'I'),
    ('flags', 'H'),
    ('version', 'H'),
    ('root_dir_offset', 'I'),
    ('info_offset', 'H'),
    ('backup_offset', 'H'),
    ('reserved', '12s'),
    ('logical_drive_num', 'B'),
    ('unused', 'B'),
    ('extended_sig', 'B'),
    ('serial_num', 'I'),
    ('volume_name', '11s'),
    ('fat_name', '8s'),
    ('program', '420s'),
    ('sig', '2s'),
]

fat16_pbr_t = utils.NamedStruct(common_fields + f16_fields, '<')
fat32_pbr_t = utils.NamedStruct(common_fields + f32_fields, '<')

cylinders = lambda size, pbr: size / (pbr.sectorsize * pbr.heads * pbr.sectors)

with open(args.infile, "rb") as f:
    size = os.path.getsize(args.infile)
    match = None

    while match is None:
        sector = f.read(args.sectorsize)
        fat16_pbr = fat16_pbr_t.unpack(sector[:fat16_pbr_t.size])
        fat32_pbr = fat32_pbr_t.unpack(sector[:fat32_pbr_t.size])

        if fat16_pbr.fs.startswith(b"FAT"):
            match = fat16_pbr
        elif fat32_pbr.fat_name.startswith(b"FAT"):
            match = fat32_pbr
            
    if match:
        utils.dump(match._asdict())
        print()
        print("offset:", f.tell() - args.sectorsize)
        print("cylinders (calculated):", cylinders(size, match))
