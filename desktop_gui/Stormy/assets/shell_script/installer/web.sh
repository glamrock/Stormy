#!/bin/bash
echo "Web Server installer Starting"
echo "----------------------------------"

c=1
while [ $c -le 10 ]
do
	echo "Installing web server step " $c
	(( c++ ))
	sleep 1 #
done
echo "=================================="
echo "Web Server installer finish!"