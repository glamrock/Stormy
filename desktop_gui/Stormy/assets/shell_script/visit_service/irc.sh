#!/bin/bash
echo "Try to find irc service location:"
echo "----------------------------------"

c=1
while [ $c -le 10 ]
do
	echo "Finding irc service location step " $c
	(( c++ ))
	sleep 1 #
done
echo "=================================="
echo "IRC is located at : /usr/bin/irc!"
