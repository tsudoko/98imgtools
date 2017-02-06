import string
import struct
from collections import namedtuple


class NamedStruct(struct.Struct):
    def __init__(self, fields, order='', size=0):
        self.values = namedtuple("header", ' '.join(k for k, _ in fields))
        format = order + ''.join([v for _, v in fields])

        if size:
            format += "%dx" % (size - struct.calcsize(format))

        super().__init__(format)

    def pack(self, *args, **kwargs):
        return super().pack(*self.values(*args, **kwargs))

    def unpack(self, data):
        return self.values._make(super().unpack(data))


# does not handle:
#  - bytes
#  - escapes in bytes
def sourcable_dump(dict_):
    value_esc = {
        "\\": r"\\",
        "'": r"'\''",
    }

    value_trans = str.maketrans(value_esc)

    for k, v in dict_.items():
        k = str(k).lstrip("0123456789")
        k = ''.join([c if c in string.ascii_letters + string.digits + '_' else '_' for c in k])
        v = str(v).translate(value_trans)
        if k:
            print("%s='%s'" % (k, v))


def pretty_dump(dict_):
    items = dict_.items()
    maxlen = max([len(k) for k, _ in items])
    for k, v in items:
        print(("{:%d} {}" % maxlen).format(k, v))


dump = pretty_dump
