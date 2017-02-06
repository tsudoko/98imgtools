import utils

header = utils.NamedStruct([
    ('dummy', 'I'),
    ('hdd_type', 'I'),
    ('raw_offset', 'I'),
    ('size', 'I'),
    ('sectorsize', 'I'),
    ('sectors', 'I'),
    ('heads', 'I'),
    ('cylinders', 'I'),
], '<', 4096)
