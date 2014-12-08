#!/bin/bash
if (($# != 4));then
	echo 'incorrect number of inputs'
	echo 'usage: ./queue.sh <lambda> <mu> <n> <T>'
	echo 'exiting...'
	exit
fi
rm -f hist.png
python queue_simulator.py $1 $2 $3 $4
matlab -nodisplay -nosplash -r "plot_histogram('${1}', '${2}', '${3}', '${4}')"
google-chrome hist.png
