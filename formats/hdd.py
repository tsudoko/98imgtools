import utils

# Used by Virtual98

header = utils.NamedStruct([
    ('magic', '8s'),
    ('comment', '128s'),
    ('padding1', '4x'),
    ('size', 'H'),
    ('sectorsize', 'H'),
    ('sectors', 'B'),
    ('heads', 'B'),
    ('cylinders', 'H'),
    ('totals', 'I'),
    ('padding2', '68x'),
], '<')
