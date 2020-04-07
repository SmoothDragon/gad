#!/bin/bash

# Script modifies ~/.bashrc
#

target=~/.bash_aliases

comment="# Modify rm to run a safety check before deleting"
line="alias rm=gad-rm"

cp -i $target $target.`date +%Y%m%d_%H%M%S` # Make file backup
sed -i "/$comment/d" $target
sed -i "/$line/d" $target


