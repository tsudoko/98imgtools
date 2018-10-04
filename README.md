98imgtools
==========

Simple scripts for reading/writing PC-9801 emulator image headers.
There's an additional `pbr_dump` script which can be used to dump FAT
partition boot sectors, if needed.

Example usage
-------------

Mount a HDI image:

    mount -ooffset=$(./pbr_dump.py image.hdi | awk '$1=="offset:"{print $2}') image.hdi /mount/point
