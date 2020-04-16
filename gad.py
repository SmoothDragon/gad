#!/usr/bin/env python

import json
import logging
import os
import pathlib

def gadroot(item):
    item = pathlib.Path(item).resolve()

    # If item is directory, do nothing, otherwise resolve to parent.
    if item.is_dir():
        path = item
    else:
        path = item.parent

    # Traverse parent directories looking for protected indicator
    directories = [path] + list(path.parents)
    for path in directories:
        gadpath = path/'.gad'
        if gadpath.exists():
            return item
    else:
        return None

def gad_config_init(gadpath):
    '''Add configuration file to path.
    '''
    filename = gadpath/'config.json'
    config = {
              'priority': [],
              'ignore': ['.gad', '.git', '.direnv'],
             }
    with open(filename, mode='w') as outfile:
        json.dump(config, outfile)

def subtree(path, ignore_list):
    '''Return all files in directory and below that do not contain items in ignore_list.
    '''
    if len(ignore_list) == 0:
        return path.rglob('*')
    else:
        return (item for item in subtree(path, ignore_list[1:]) if ignore_list[0] not in str(item))

def gad_sql_init(path):
    filename = path/'.gad/config.json'
    with open(filename, mode='r') as infile:
        config = json.load(infile)
    ignore = config['ignore']

    
    for name in path.rglob('*'):
        for item in ignore:
            if item in str(name):
                break
        else:
            print(name)
    for name in subtree(path, ignore):
        print(name)
    # Walk dir
    # Skip .gad dir
    # Create db in nondescrutive way
    # For things not in db, add 
    # ASSET, TRASH, ADD, DEL, UNK, DUP
    # action, time, filename, qhash, size,

def gad_init(directory='.'):
    item = pathlib.Path(directory).resolve()
    if not item.is_dir():
        raise Exception('%s is not a valid directory' % item)
    gadpath = item/'.gad'
    if not gadpath.exists():
        pathlib.Path(gadpath).mkdir(parents=True, exist_ok=True)
        gad_config_init(gadpath)
    gad_sql_init(item)


class gad:
    def __init__(self, *args, **kwargs):
        # Set verbosity according to kwargs
        # Check if .gad.json exists in home directory
        # Validate root directory
        # If not, create .gadconfig with empty root and restart
        # # Protected= [] should be a list of protected roots. Files in those roots will not be deleted.
        ## Alias rm to protect roots
        # Check for .gad.sqlite
        # If not, create database
        # Create keep table key=hash, keep=Boolean, decision date,
        # Create decision message key=date, message=string
        # Create location table key=hash, size=integer, location=filehandle (string), timestamp=date
        pass

    def validateJSONconfig(self):
        pass

    def add(self, filename):
        # Check if filename
        pass

    def rm(self, filename):
        pass

    def status(self):
        pass

    def commit(self):
        pass

    def check(self, filename):
        # check if a filename it in a protected zone
        pass
