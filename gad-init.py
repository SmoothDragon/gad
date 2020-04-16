#!/usr/bin/env python

'''Initial .gad directory
'''

if __name__ == '__main__':
    import sys
    import gad

    if len(sys.argv) > 1:
        item = sys.argv[1]
    else:
        item = '.'

    result = gad.gadroot(item)
    print(item)
    if result is None:
        gad.gad_init(item)
