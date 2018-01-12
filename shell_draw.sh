#!/bin/bash

while true
do
rand=$(( RANDOM % 5 + 1 ))
sed -n "${rand},${rand}p" stafflist
sleep 0.01
clear
done
