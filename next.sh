#!/bin/bash

cd `dirname $0`

#Stop Streams first
./stop.sh

#Change Station
nmax=(stations/*)
nmax=${#nmax[@]}
nmax=$((nmax-1)) #Subtract 1, because index starts at zero

ncur=`cat last-station.txt`

if [ "$nmax" -eq "$ncur" ]; then
	nnew="0"
else
	nnew=$((ncur+1))
fi
echo $nnew > ./last-station.txt

sleep 1

#Start again
./play.sh

