#!/bin/bash


Age=$1

if [ $Age -lt 13 ]; then 
	echo "child"
elif [ $Age -lt 20 ]; then
	echo "teen"
elif [ $Age -lt 65 ]; then
        echo "adult"
else
	echo "elderly"

fi

