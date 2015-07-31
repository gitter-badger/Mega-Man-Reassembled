#!/usr/bin/python
from os import system as scall
from sys import exit as exit

copy_directory = "cp -R "
dirs_to_copy = [
'../Libraries/*',
'../assets',
'../src/*'
]
destination = "../build/components"
err = scall("cat ../build/components")
if not err:
    pass
else:
    scall("mkdir -p ../build/components")
for directory in dirs_to_copy:
    err = scall(copy_directory + directory + " " + destination)
    if not err:
        print("Successfully copied directory " + directory + " to " + destination + ".")
    else:
        print("Could not copy " + directory + " to " + destination + ".")
        exit(-1)
