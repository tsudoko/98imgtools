98imgtools
==========

Simple scripts for reading/writing PC-9801 emulator image headers.
There's an additional `pbr_dump` script which can be used to dump FAT
partition boot sectors, if needed.

Example usage
-------------

Mount a HDI image:

    mount -ooffset=$(./pbr_dump.py image.hdi | awk '$1=="offset:"{print $2}') image.hdi /mount/point

Supported formats
-----------------

 * HDD
 * HDI
 * NHD
 * SLH

See [`formats`](formats/) for the various format structures.

Tools
-----

### `hdddump.py`
Display header information from an HDD hard drive image file.

Verifies magic values in header.

### `hddgen.py`
Creates a new blank HDD image header to the user's specifications. Blank space is not allocated.

### `hdidump.py`
Display header information from an HDI hard drive image file.

### `nhddump.py`
Display header information from an NHD hard drive image file.

Verifies magic values in header.

### `nhdgen.py`
Creates a new blank NHD image header to the user's specifications. Blank space is not allocated.

### `pbr_dump.py`
Dumps the boot sector of the first partition found in the provided disk image.

### `slhdump.py`
Display header information from an SLH hard drive image file.

Verifies magic values in header.

### `slhgen.py`
Creates a new blank SLH image header to the user's specifications. Blank space is not allocated.
