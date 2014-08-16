function top(){
	
	for i in `seq 46 1 51`; do echo -en "\e[38;5;${i}m#\e[0m";done;echo
	for i in `seq 40 1 45`; do echo -en "\e[38;5;${i}m#\e[0m";done;echo
	for i in `seq 34 1 39`; do echo -en "\e[38;5;${i}m#\e[0m";done;echo -e "\tT O P"
	for i in `seq 28 1 33`; do echo -en "\e[38;5;${i}m#\e[0m";done;echo
	for i in `seq 22 1 27`; do echo -en "\e[38;5;${i}m#\e[0m";done;echo
	for i in `seq 16 1 21`; do echo -en "\e[38;5;${i}m#\e[0m";done;echo
	echo
	return 0
}
function right(){
	for i in `seq 21 6 51`; do echo -en "\e[38;5;${i}mS\e[0m";done;echo
	for i in `seq 57 6 87`; do echo -en "\e[38;5;${i}mT\e[0m";done;echo
	for i in `seq 93 6 123`; do echo -en "\e[38;5;${i}mO\e[0m";done;echo -e "\tR I G H T"
	for i in `seq 129 6 159`; do echo -en "\e[38;5;${i}mR\e[0m";done;echo
	for i in `seq 165 6 195`; do echo -en "\e[38;5;${i}mM\e[0m";done;echo
	for i in `seq 201 6 231`; do echo -en "\e[38;5;${i}mY\e[0m";done;echo
	echo
	return 0
}
function left(){
	for i in `seq 46 -6 16`; do echo -en "\e[38;5;${i}m#\e[0m";done;echo
	for i in `seq 82 -6 52`; do echo -en "\e[38;5;${i}m#\e[0m";done;echo
	for i in `seq 118 -6 88`; do echo -en "\e[38;5;${i}m#\e[0m";done;echo -e "\tL E F T"
	for i in `seq 154 -6 124`; do echo -en "\e[38;5;${i}m#\e[0m";done;echo
	for i in `seq 190 -6 160`; do echo -en "\e[38;5;${i}m#\e[0m";done;echo
	for i in `seq 226 -6 196`; do echo -en "\e[38;5;${i}m#\e[0m";done;echo
	echo
	return 0
}
function front(){
	for i in `seq 16 1 21`; do echo -en "\e[38;5;${i}m#\e[0m";done;echo
	for i in `seq 52 1 57`; do echo -en "\e[38;5;${i}m#\e[0m";done;echo
	for i in `seq 88 1 93`; do echo -en "\e[38;5;${i}m#\e[0m";done;echo -e "\tF R O N T"
	for i in `seq 124 1 129`; do echo -en "\e[38;5;${i}m#\e[0m";done;echo
	for i in `seq 160 1 165`; do echo -en "\e[38;5;${i}m#\e[0m";done;echo
	for i in `seq 196 1 201`; do echo -en "\e[38;5;${i}m#\e[0m";done;echo
	echo
	return 0
}
function bottom(){
	for i in `seq 196 1 201`; do echo -en "\e[38;5;${i}m#\e[0m";done;echo
	for i in `seq 202 1 207`; do echo -en "\e[38;5;${i}m#\e[0m";done;echo
	for i in `seq 208 1 213`; do echo -en "\e[38;5;${i}m#\e[0m";done;echo -e "\tB O T T O M"
	for i in `seq 214 1 219`; do echo -en "\e[38;5;${i}m#\e[0m";done;echo
	for i in `seq 220 1 225`; do echo -en "\e[38;5;${i}m#\e[0m";done;echo
	for i in `seq 226 1 231`; do echo -en "\e[38;5;${i}m#\e[0m";done;echo
	echo
	return 0
}
function back(){
	for i in `seq 51 -1 46`; do echo -en "\e[38;5;${i}m#\e[0m";done;echo
	for i in `seq 87 -1 82`; do echo -en "\e[38;5;${i}m#\e[0m";done;echo
	for i in `seq 123 -1 118`; do echo -en "\e[38;5;${i}m#\e[0m";done;echo -e "\tB A C K"
	for i in `seq 159 -1 154`; do echo -en "\e[38;5;${i}m#\e[0m";done;echo
	for i in `seq 195 -1 190`; do echo -en "\e[38;5;${i}m#\e[0m";done;echo
	for i in `seq 231 -1 226`; do echo -en "\e[38;5;${i}m#\e[0m";done;echo
	echo
	return 0
}

top
front
left
back
right
bottom
exit 0
