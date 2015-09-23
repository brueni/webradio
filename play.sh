#!/bin/bash
laststationfile=`cat last-station.txt`
stream=`cat stations/$laststationfile`

mpg321 $stream
