# Benchmark simulations with CORSIKA

The CORSIKA air shower simulation software is widely used to obtain simulation of cosmic rays interactions in the atmosphere, and the consequent production of particles in the atmosphere.

## CORSIKA containers

Singularity container definitions are provided to run CORSIKA7 simulations

- obtain CORSIKA 7.7100 from https://www.iap.kit.edu/corsika/
- build the singularity images by doing `sudo singularity build corsika<id>.sif corsika_<id>.def`
- store the images in your folder (see below)


## CORSIKA simulation scripts

Scripts are provided to run the benchmark simulation on a cpu cluster in which the Slurm Workload Manager is installed. These scripts require that all machines can access a `/mnt/slurmscratch` folder in which the singularity images are stored, and in which an output folder and a logfolder are prepared.

