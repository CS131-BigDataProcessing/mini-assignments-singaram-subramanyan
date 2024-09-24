#!/bin/bash


temp=$1

if [ $temp -gt 55 ]; then
        if [ $temp -lt 67 ]; then
                echo "cold"
        elif [ $temp -lt 85 ]; then
                echo "nice"
        elif [ $temp -gt 85 ]; then
                echo "hot"
        fi
elif [ $temp -lt 55 ]; then
        echo "freezing"

fi
