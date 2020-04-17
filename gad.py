#!/usr/bin/env python

import json
import logging
import os
import pathlib
import sqlite3
import xxhash

gad_sql = '''
CREATE TABLE IF NOT EXISTS action(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(8) UNIQUE NOT NULL
    );

CREATE TABLE IF NOT EXISTS known(
    ID INT PRIMARY KEY,
    size INT NOT NULL,
    ctime INT NOT NULL,
    actionID INT NOT NULL REFERENCES action(ID)
    );

CREATE TABLE IF NOT EXISTS files(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    hash INT NOT NULL REFERENCES known(ID)
    );
'''

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
            return gadpath
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
    with open(str(filename), mode='w') as outfile:
        json.dump(config, outfile)

def gad_sql_init(gadpath):
    db = gadpath/'gad.sqlite3'
    conn = sqlite3.connect(db)
    conn.executescript(gad_sql)
    actions = [(None, action) for action in ['ASSET', 'TRASH', 'NEW', 'DUPS']]
    conn.executemany('INSERT INTO action VALUES(?, ?);', actions)
    conn.commit()


def subtree(path, ignore_list):
    '''Return all files in directory and below that do not contain items in ignore_list.
    '''
    if len(ignore_list) == 0:
        return path.rglob('*')
    else:
        return (item for item in subtree(path, ignore_list[1:]) 
                if not item.is_dir() and ignore_list[0] not in str(item))

def file_hash(filename):
    '''A computationally fast hash, using the filesize as seed.
    Returns a 64-bit signed integer
    '''
    filehash = xxhash.xxh64(seed=os.stat(filename).st_size)
    with open(filename, "rb") as infile:
        for chunk in iter(lambda: infile.read(4096), b""):
            filehash.update(chunk)
    return filehash.intdigest() - (1<<63)  # Signed integer

def gad_path_init(path):
    filename = path/'.gad/config.json'
    with open(str(filename), mode='r') as infile:
        config = json.load(infile)
    ignore = config['ignore']
    for name in subtree(path, ignore):
        if len(str(name)) >= 4095:
            raise Exception('Path length exceeded.')
        print(file_hash(name), name)
    # Walk dir
    # Skip .gad dir

def gad_init(directory='.'):
    item = pathlib.Path(directory).resolve()
    if not item.is_dir():
        raise Exception('%s is not a valid directory' % item)
    gadpath = item/'.gad'
    if not gadpath.exists():
        pathlib.Path(gadpath).mkdir(parents=True, exist_ok=True)
        gad_config_init(gadpath)
        gad_sql_init(gadpath)


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
