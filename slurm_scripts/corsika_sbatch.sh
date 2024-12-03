#/bin/sh

export CORVER=77100

echo $CORSIKA_HOME
ls

export RUNDIR=/corsika-${CORVER}/run

export COREXE=`ls $RUNDIR | grep corsika`
echo $COREXE

cd $RUNDIR
ls


$COREXE < /mnt/${CORSIKA_INPUT} #> out_${COREXE}_${CORSIKA_INPUT}.txt


echo "here we are"

