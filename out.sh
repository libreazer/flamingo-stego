#!/bin/bash

sleep 2

awk '{print $5}' temp.txt

s=$0

if ( $s -ne "done" )
then
	echo 1
else
	echo 0
fi
rm temp.txt