import utils

header = utils.NamedStruct([
    ('magic', '4s'),
    ('size', 'Q'),
    ('sectorsize', 'I'),
    ('cylinders', 'I'),
    ('heads', 'I'),
    ('sectors', 'I'),
    ('serial_number', '20s'),
    ('revision', '8s'),
    ('model_name', '40s'),
], '<', 512)
