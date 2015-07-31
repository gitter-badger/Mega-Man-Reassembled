#!/usr/bin/env python
from os import system as scall

clean = 'rm -Rf '
dirs_to_clean  = [
'../build/'
]
for directory in dirs_to_clean:
    scall(clean + directory)
    print("Cleaned directory " + directory + ".")
