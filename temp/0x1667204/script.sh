#!/bin/bash
compiler=$1
file=$2
output=$3
args=$4
exec  1> $"/compile/output"
exec  2> $"/compile/errors"

if [ "$output" = "" ]; then
	$compiler /compile/$file < /compile/input
else
	$compiler /compile/$file
	if [ $? -eq 0 ]; then
		$output < /compile/input
	fi
fi

mv /compile/output /compile/completed

