#!/usr/bin/env python

'''Find .gad root for given location.
If no root is found exit with status -1.
Otherwise print root name.
'''

if __name__ == '__main__':
    import sys
    import gad

    if len(sys.argv) > 1:
        item = sys.argv[1]
    else:
        item = '.'

    result = gad.gadroot(item)
    if result is None:
        exit(-1)
    print(result)

