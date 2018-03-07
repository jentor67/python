import hashlib
import sys

"""md5check.py: Determine whether 2 files match."""
"""user>python md5check.py <file1> <file2>"""

__author__    = "John Major"
__copyright__ = "Copyright 2018, Jentor"


if( len(sys.argv) > 1):
    # file 1
    hasher1 = hashlib.md5()
    firstFile = open(sys.argv[1],'rb')
    buf1 = firstFile.read()
    a = hasher1.update(buf1)
    md5_a=(str(hasher1.hexdigest()))
else:
   print("WARNING: No <file1> present")

if( len(sys.argv) > 2):
    # file 2
    hasher2 = hashlib.md5()
    secondFile = open(sys.argv[2],'rb')
    buf2 = secondFile.read()
    b = hasher2.update(buf2)
    md5_b=(str(hasher2.hexdigest()))
else:
   print("WARNING: No <file2> present")

if( len(sys.argv) > 2):
    if( md5_a == md5_b ):
        print("File:\n"+sys.argv[1]+"\nmatches file:\n"+sys.argv[2])
    else:
        print("File:\n"+sys.argv[1]+"\nDoes not match file:\n"+sys.argv[2])
else:
    print("Syntax will be:>python md5check.py <file1> <file2>")
