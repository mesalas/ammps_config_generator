#!/bin/bash
WORKDIR=working
mkdir $WORKDIR
OUTDIR=out
mkdir $OUTDIR

FILES=*.xlsx
counter=0
for f in $FILES
do
	echo "running $f"
	echo "dotnet amm.engine.dll RunConfFromFile $f output $counter"
	dotnet ../bin/amm.engine.dll RunConfFromFile $f $WORKDIR $counter >> $OUTDIR/log.log
	#Compress output files and move to target dir
	gzip -r $WORKDIR
	mv $WORKDIR/*.gz $OUTDIR
	
	counter=`expr $counter + 1`
done
exit
