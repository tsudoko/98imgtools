import utils

header = utils.NamedStruct([
    ('magic', '16s'),
    ('comment', '256s'),
    ('raw_offset', 'I'),
    ('cylinders', 'I'),
    ('heads', 'H'),
    ('sectors', 'H'),
    ('sectorsize', 'H'),
], '<', 512)
