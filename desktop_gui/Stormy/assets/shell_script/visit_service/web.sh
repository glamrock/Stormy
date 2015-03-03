#!/bin/bash
echo "Try to find web server service location:"
echo "----------------------------------"

c=1
while [ $c -le 10 ]
do
	echo "Finding web server service location step " $c
	(( c++ ))
	sleep 1 #
done
echo "=================================="
echo "Web Server is located at : /usr/bin/apache2!"
