#!/usr/bin/env python

import pathlib
import sys


def filter_flags(arglist):
    # Remove all arguments that are flags
    # TODO: remove flag arguments
    return (arg for arg in arglist if arg[0] != '-')


def safety_check(items):
    protected = {}
    conflicts = []
    for item in filter_flags(items):
        item = pathlib.Path(item).resolve()

        # If item is directory do nothing, otherwise resolve to parent.
        if item.is_dir():
            path = item
        else:
            path = item.parent

        # Shortcut if path is already protected
        if path in protected:
            if protected[path]:
                conflicts.append(item)
            continue

        # Traverse parent directories looking for protected indicator
        directories = [path] + list(path.parents)
        flag = False
        for path in directories[::-1]:  # Start with root first. Lower dirs automatically protected.
            q = path/'.gad.sqlite'
            if q.exists():
                flag = True
            if flag:
                protected[path] = True
        if flag:
            conflicts.append(item)
    return conflicts

if __name__ == '__main__':
    conflicts = safety_check(sys.argv[1:])
    if len(conflicts) > 0:
        print('The following files are protected:')
        for item in conflicts:
            print(item)
        exit(-1)
    else:
        exit(0)

