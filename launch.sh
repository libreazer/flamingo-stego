#!/bin/bash

#JPEG, BMP, WAV and AU files - Support

file1=$2

file2=$4

enc=$5

comp=$6

xterm -T "User-Friendly Steganography Tool" -e "echo Enter a passphrase to conceal your file securely;steghide embed -cf $file1 -ef $file2 -e $5 -z $comp > temp.txt"

