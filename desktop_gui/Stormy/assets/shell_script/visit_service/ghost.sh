#!/bin/bash
echo "Try to find ghost service locaktion:"
echo "----------------------------------"

c=1
while [ $c -le 10 ]
do
	echo "Finding ghost service location step " $c
	(( c++ ))
	sleep 1 #
done
echo "=================================="
echo "Ghost is located at : /usr/bin/ghost!"
