#!/bin/bash

is_equal=1
num=1
while [ $is_equal == 1 ]
do
    python3 gen.py
    s=`cat 1.txt`
    s1=$(./test1 ${s})
    s2=$(./test2 ${s})
    if [ $s1 != $s2 ]
    then
        is_equal=0
        echo "find. $num $s1 $s2"
        break
    else
        let num=num+1
        echo "exploring wrong condition... $num"
    fi
done