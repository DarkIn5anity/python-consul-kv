#!/bin/bash
set -e

#construct our command
PYTHON_CMD="python /dsc/dsc.py $*"

# Ensure the minimum environment variables are specified...
for a in "$*"; do
    if [[ $a != *"--example"* ]];then
        echo "--example is required"
        exit 1
    fi
done


echo -e "Running $PYTHON_CMD \n"

exec $PYTHON_CMD