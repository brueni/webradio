#!/bin/bash
n=`cat last-station.txt`

files=(stations/*)
streamfile="${files[n]}"
stream=`cat $streamfile`

mpg321 $stream
