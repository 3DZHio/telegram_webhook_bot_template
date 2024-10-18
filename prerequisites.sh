#!/bin/bash


## START ##
echo "| START |"


## ENV ##
if [ -f .env.example ]; then
    ## ReName .env.example To .env ##
    mv .env.example .env
else
    if [ -f .env ]; then
        ## Variables ##
        source .env
    else
        echo "| ERROR | // NOT FOUND // .env or .env.example file" >&2
        exit 1
    fi
fi


## GitIgnore ##
if [ "${SAVE_ENV}" == "1" ]; then
    sed -i "s/^.env$/##.env/" .gitignore
fi


## Redis Memory OverCommit ##
if [ "$(sudo cat /proc/sys/vm/overcommit_memory)" != "1" ]; then
    echo 1 | sudo tee /proc/sys/vm/overcommit_memory
fi


## Install Requirements ##
pip install -r requirements.txt


## SUCCESS ##
echo "| SUCCESS |"