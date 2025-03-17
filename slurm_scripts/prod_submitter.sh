#!/bin/bash

for job in $(seq 1 1); do
    for c in 72110 72310 76110 76310; do
	echo "container is : $c"
	for p in 14; do
	    echo "primary is: $p"
	    for z in Z; do
		echo "zenith is: $z"
		for e in 1; do
		    echo "energy is: $e"
		    echo "launching run: $job"
		    echo "$job $c $p $e $z"
		    ./submit_corsika_job.sh $job $c $p $e $z
		done
	    done
	done
    done
done

sleep 10

for job in $(seq 1 5); do
    for c in 72110 72310 76110 76310; do
	echo "container is : $c"
	for p in 14; do
	    echo "primary is: $p"
	    for z in Z; do
		echo "zenith is: $z"
		for e in 10; do
		    echo "energy is: $e"
		    echo "launching run: $job"
		    echo "$job $c $p $e $z"
		    ./submit_corsika_job.sh $job $c $p $e $z
		done
	    done
	done
    done
done

sleep 10

for job in $(seq 1 25); do
    for c in 72110 72310 76110 76310; do
	echo "container is : $c"
	for p in 14; do
	    echo "primary is: $p"
	    for z in Z; do
		echo "zenith is: $z"
		for e in 100; do
		    echo "energy is: $e"
		    echo "launching run: $job"
		    echo "$job $c $p $e $z"
		    ./submit_corsika_job.sh $job $c $p $e $z
		done
	    done
	done
    done
done

sleep 10

for job in $(seq 1 100); do
    for c in 72110 72310 76110 76310; do
	echo "container is : $c"
	for p in 14; do
	    echo "primary is: $p"
	    for z in Z; do
		echo "zenith is: $z"
		for e in 1000; do
		    echo "energy is: $e"
		    echo "launching run: $job"
		    echo "$job $c $p $e $z"
		    ./submit_corsika_job.sh $job $c $p $e $z
		done
	    done
	done
    done
done

sleep 10

for job in $(seq 1 125); do 
    for c in 72110 72310 76110 76310; do
	echo "container is : $c"
	for p in 14; do
	    echo "primary is: $p"
	    for z in Z; do
		echo "zenith is: $z"
		for e in 10000 20000 30000 50000; do
		    echo "energy is: $e"
		    echo "launching run: $job"
		    echo "$job $c $p $e $z"
		    ./submit_corsika_job.sh $job $c $p $e $z
		done
	    done
	done
    done
done

sleep 10

for job in $(seq 1 250); do
    for c in 72110 72310 76110 76310; do
	echo "container is : $c"
	for p in 14; do
	    echo "primary is: $p"
	    for z in Z; do
		echo "zenith is: $z"
		for e in 100000 200000; do
		    echo "energy is: $e"
		    echo "launching run: $job"
		    echo "$job $c $p $e $z"
		    ./submit_corsika_job.sh $job $c $p $e $z
		done
	    done
	done
    done
done

sleep 10

for job in $(seq 1 1250); do

    for c in 72110 72310 76110 76310; do
	echo "container is : $c"
	for p in 14; do
	    echo "primary is: $p"
	    for z in Z; do
		echo "zenith is: $z"
		for e in 300000 500000; do
		    echo "energy is: $e"
		    echo "launching run: $job"
		    echo "$job $c $p $e $z"
		    ./submit_corsika_job.sh $job $c $p $e $z
		done
	    done
	done
    done
done



