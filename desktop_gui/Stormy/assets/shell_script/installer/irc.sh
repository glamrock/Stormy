#!/bin/bash
echo "IRC installer Starting"
echo "----------------------------------"

c=1
while [ $c -le 10 ]
do
	echo "Installing irc step " $c
	(( c++ ))
	sleep 1 #
done
echo "=================================="
echo "IRC installer finish!"