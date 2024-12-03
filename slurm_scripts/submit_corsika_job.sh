#!/bin/bash

jobnumber=$1
containerversion=$2

primary=$3

energy=$4

zenith=$5

if [ $# -ne 5 ]; then
    echo "Need 5 parameters, only $# were given"
    echo "Usage: $0 <job number> <container version> <primary nucleus> <energy range [L, M, H, UH]> <zenith range [V, H]>"
    exit 1
fi


if [ ${containerversion:1:1} -eq 2 ]; then
    echo "USING EPOS"
    all_inputs="all-inputs_epos"
    him="EPOS"
elif [ ${containerversion:1:1} -eq 6 ]; then
    echo "USING SYBILL"
    all_inputs="all-inputs_sybill"
    him="SYBILL"
else
    echo "Unknown HIM"
    exit 1
fi


if [ "$energy" = "L" ]; then
    echo "Low energy range 1e3 - 1e5 GeV"
    energym="1e3"
    energyM="1e5"
    nshow=10000
elif [ "$energy" = "M" ]; then
    echo "Mid energy range 1e5 - 1e7 GeV"
    energym="1e5"
    energyM="1e7"
    nshow=1000
elif [ "$energy" = "H" ]; then
    echo "High energy range 1e7 - 1e8 GeV"
    energym="1e7"
    energyM="1e8"
    nshow=100
elif [ "$energy" = "UH" ]; then
    echo "Ultra high energy range 1e8 - 1e9 GeV"
    energym="1e8"
    energyM="1e9"
    nshow=10
else
    echo "Unknown energy setup: $energy"
    exit 1
fi

if [ "$zenith" = "V" ]; then
    echo "Vertical events: zenith range 0 - 60 degrees"
    zenithm=0
    zenithM=60
elif [ "$zenith" = "H" ]; then
    echo "Horizontal events: zenith range 60 - 90 degrees"
    zenithm=60
    zenithM=90
else
    echo "Unknown zenith setup: $zenith"
    exit 1
fi

export basedir='/mnt/slurmscratch'
export containerdir=${basedir}/corsika7_containers

#echo ${basedir}
#echo ${containerdir}

export job_id=job${jobnumber}_contver${containerversion}_pr${primary}_e${energym}-${energyM}_z${zenithm}-${zenithM}
#echo ${job_id}

export job_folder=${basedir}/${job_id}
mkdir $job_folder
#echo $job_folder

cp corsika_sbatch.sh ${job_folder}/corsika.sh
cp run-singularity_sbatch.sh ${job_folder}/run-singularity.sh

corsika_input=${all_inputs}_${job_id}

#echo ${corsika_input}

seed1=${containerversion:1:2}${jobnumber}${primary}${zenithm%%.*}
seed2=${containerversion:1:2}${jobnumber}${primary}${zenithM%%.*}


if [ "$him" = "EPOS" ]; then

cat<<EOF>> ${corsika_input}

RUNNR   ${jobnumber}                             run number
NSHOW   ${nshow}                             number of showers to generate
PRMPAR  ${primary}                            prim. particle (1=gamma, 14=proton, ...)
ESLOPE  -1                          slope of primary energy spectrum
ERANGE 	${energym}  ${energyM}                    energy range of primary particle (GeV)
THETAP  ${zenithm}  ${zenithM}                        range of zenith angle (degree)
PHIP    -180.  180.                   range of azimuth angle (degree)
SEED    ${seed1}   0   0                     seed for 1. random number sequence
SEED    ${seed2}   0   0                     seed for 2. random number sequence
*THIN    1.E-2  1.E2  0.               thinning definition
*THINH   10.  10.                      relative threshold and weight for hadron thinning
OBSLEV  0.                            observation level (in cm)
MAGNET  20.0  42.8                    magnetic field centr. Europe
HADFLG  0  0  0  0  0  2              flags hadr.interact.&fragmentation
ECUTS   1.  1.  0.001  0.001          energy cuts for particles
MUADDI  T                             additional info for muons
MUMULT  T                             muon multiple scattering angle
ELMFLG  T   F                         em. interaction flags (NKG,EGS)
STEPFC  1.0                           mult. scattering step length fact.
RADNKG  200.E2                        outer radius for NKG lat.dens.distr.
EPOPAR input ../epos/epos.param        !initialization input file for epos
EPOPAR fname inics ../epos/epos.inics  !initialization input file for epos
EPOPAR fname iniev ../epos/epos.iniev  !initialization input file for epos
EPOPAR fname initl ../epos/epos.initl  !initialization input file for epos
EPOPAR fname inirj ../epos/epos.inirj  !initialization input file for epos
EPOPAR fname inihy ../epos/epos.ini1b  !initialization input file for epos
EPOPAR fname check none                !dummy output file for epos
EPOPAR fname histo none                !dummy output file for epos
EPOPAR fname data  none                !dummy output file for epos
EPOPAR fname copy  none                !dummy output file for epos
LONGI   T  10.  F  F                  longit.distr. & step size & fit & outfile
ECTMAP  1.E9                          cut on gamma factor for printout
MAXPRT  1                             max. number of printed events
DIRECT  /mnt/                 output directory
USER    you                           user 
*PAROUT F F                            suppress DAT file
DEBUG   F  6  F  1000000              debug flag and log.unit for out
EXIT                                  terminates input

EOF

elif [ "$him"="SYBILL" ]; then

cat<<EOF>> ${corsika_input}

RUNNR   ${jobnumber}                             run number
NSHOW   ${nshow}                             number of showers to generate
PRMPAR  ${primary}                            prim. particle (1=gamma, 14=proton, ...)
ESLOPE  -1                          slope of primary energy spectrum
ERANGE 	${energym}  ${energyM}                    energy range of primary particle (GeV)
THETAP  ${zenithm}  ${zenithM}                        range of zenith angle (degree)
PHIP    -180.  180.                   range of azimuth angle (degree)
SEED    ${seed1}   0   0                     seed for 1. random number sequence
SEED    ${seed2}   0   0                     seed for 2. random number sequence
*THIN    1.E-2  1.E2  0.               thinning definition
*THINH   10.  10.                      relative threshold and weight for hadron thinning
OBSLEV  0.                            observation level (in cm)
MAGNET  20.0  42.8                    magnetic field centr. Europe
HADFLG  0  0  0  0  0  2              flags hadr.interact.&fragmentation
ECUTS   1.  1.  0.001  0.001          energy cuts for particles
MUADDI  T                             additional info for muons
MUMULT  T                             muon multiple scattering angle
ELMFLG  T   F                         em. interaction flags (NKG,EGS)
STEPFC  1.0                           mult. scattering step length fact.
RADNKG  200.E2                        outer radius for NKG lat.dens.distr.
LONGI   T  10.  F  F                  longit.distr. & step size & fit & outfile
ECTMAP  1.E9                          cut on gamma factor for printout
MAXPRT  1                             max. number of printed events
DIRECT  /mnt/                 output directory
USER    you                           user 
*PAROUT F F                            suppress DAT file
DEBUG   F  6  F  1000000              debug flag and log.unit for out
EXIT                                  terminates input

EOF

    
fi

#cat ${corsika_input}

mv ${corsika_input} ${job_folder}/.

#echo ' FINO A QUA 1'

ls ${job_folder}/

sbatch --job-name=${job_id} --time=7-00:00:00 --mem=3000 --export=ALL,CONTAINERVERSION=${containerversion},CORSIKA_INPUT=${corsika_input},BASEDIR=${basedir},CONTAINERDIR=${containerdir},JOB_FOLDER=${job_folder} --ntasks 1 --output=${basedir}/corsika7_joblog/${job_id}.out --error=${basedir}/corsika7_joblog/${job_id}.err ${job_folder}/run-singularity.sh
