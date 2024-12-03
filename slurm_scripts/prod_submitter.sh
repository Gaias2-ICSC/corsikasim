#!/bin/bash

for c in 72110 72310 76110 76310; do                              # see containers configurations
    echo "container is : $c"
    for p in 14; do                                               # protons is 14, helium is , carbon is , silicon is, iron is
	echo "primary is: $p"

	for z in V; do                                            # V is vertical (0 - 60 degrees), H is horizontal (60 - 90 degrees)
	    echo "zenith is: $z"

	    for e in L M H UH; do                                 # L is low-energy (1 - 100 TeV), M is medium (100 TeV - 10 PeV), H is high (10 - 100 PeV),
		                                                  # UH is ultra-high (100 PeV - 1 EeV)
		echo "energy is: $e"

		for job in $(seq 1 200); do

		    echo "launching run: $job"
		    echo "$job $c $p $e $z"

		    ./submit_corsika_job.sh $job $c $p $e $z

		done
	    done
	done
    done
done
