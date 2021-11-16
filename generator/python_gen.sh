#!/bin/bash

is_equal=1
while [ $is_equal -eq 1 ]
do
    python3 gen.py
    s1=$(python3 test1.py < 1.txt)
    s2=$(python3 test2.py < 1.txt)
    if [ $s1 -ne $s2 ]
    then
        is_equal=0
        echo $s1 $s2
        break
    else
        echo exploring wrong condition...
    fi
done