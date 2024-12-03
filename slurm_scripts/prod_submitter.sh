#!/bin/bash

for c in 72110 72310 76110 76310; do
    echo "container is : $c"
    for p in 14; do
	echo "primary is: $p"
	for z in V; do
	    echo "zenith is: $z"
	    for e in L M H UH; do
		echo "energy is: $e"
		for job in $(seq 51 200); do
		    echo "launching run: $job"
		    echo "$job $c $p $e $z"
		    ./submit_corsika_job.sh $job $c $p $e $z
		done
	    done
	done
    done
done
