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

 * HDD (Virtual98)
 * HDI (Anex86)
 * NHD (T98-Next)
 * SLH (SL9821)

See [`formats`](formats/) for the various format structures.

Tools
-----

### `hdddump.py`
Display header information from an HDD hard drive image file.

### `hddgen.py`
Creates a new HDD image header to the user's specifications.

### `hdidump.py`
Display header information from an HDI hard drive image file.

### `nhddump.py`
Display header information from an NHD hard drive image file.

### `nhdgen.py`
Creates a new NHD image header to the user's specifications.

### `pbr_dump.py`
Dumps the boot sector of the first FAT partition found in the provided disk image.

### `slhdump.py`
Display header information from an SLH hard drive image file.

### `slhgen.py`
Creates a new SLH image header to the user's specifications.
