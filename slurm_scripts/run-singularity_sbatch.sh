#!/bin/bash

echo $JOB_FOLDER

echo $CORSIKA_INPUT

time singularity run --bind $JOB_FOLDER:/mnt ${CONTAINERDIR}/corsika$CONTAINERVERSION.sif


mv $JOB_FOLDER $BASEDIR/corsika7_joboutput/.
