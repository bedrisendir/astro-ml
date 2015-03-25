#!/bin/bash +vx
for machines in `cat $1`
do
if [[ $2 == "-s" ]]
then
  ssh $machines "$3"
elif [[ $2 == "-f" ]]
then
   ssh $machines 'bash -s' < $3
fi
done
