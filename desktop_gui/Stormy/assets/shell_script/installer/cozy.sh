#!/bin/bash
echo "Cozy installer Starting"
echo "----------------------------------"

c=1
while [ $c -le 10 ]
do
	echo "Installing cozy step " $c
	(( c++ ))
	sleep 1 #
done
echo "=================================="
echo "Cozy installer finish!"
