#!/bin/bash
echo "Ghost installer Starting"
echo "----------------------------------"

c=1
while [ $c -le 10 ]
do
	echo "Installing ghost step " $c
	(( c++ ))
	sleep 1 #
done
echo "=================================="
echo "Ghost installer finish!"