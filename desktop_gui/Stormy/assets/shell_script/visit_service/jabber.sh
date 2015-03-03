#!/bin/bash
echo "Try to find jabber service locaktion:"
echo "----------------------------------"

c=1
while [ $c -le 10 ]
do
	echo "Finding jabber service location step " $c
	(( c++ ))
	sleep 1 #
done
echo "=================================="
echo "Jabber is located at : /usr/bin/jabber!"
