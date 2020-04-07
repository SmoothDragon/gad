#!/bin/bash

# Script modifies ~/.bashrc
#

target=~/.bash_aliases

comment="# Modify rm to run a safety check before deleting"
line="alias rm=gad-rm"

if [ -f ~/.bash_aliases ] && (grep -q "$line" $target ); then
    exit 0 # Line already exists. No need to add it.
fi

cp -i $target $target.`date +%Y%m%d_%H%M%S` # Make file backup
echo $comment >> $target
echo $line >> $target
# sed -i.bak '/pattern to match/d' ./infile


