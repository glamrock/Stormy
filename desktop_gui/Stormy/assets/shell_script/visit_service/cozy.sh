#!/bin/bash
echo "Try to find cozy service locaktion:"
echo "----------------------------------"

c=1
while [ $c -le 10 ]
do
	echo "Finding cozy service location step " $c
	(( c++ ))
	sleep 1 #
done
echo "=================================="
echo "Cozy is located at : /usr/bin/cozy!"
