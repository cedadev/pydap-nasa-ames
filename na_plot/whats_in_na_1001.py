#!/usr/bin/env python


import sys
import os

import matplotlib.pyplot as plt
import numpy
import nappy


def read_data(fpath):
    f = nappy.openNAFile(fpath) 
    f.readData()
    return f


def main(fpath):
 
    na = read_data(fpath)
    print 

    vars = {}

    for i in range(na.NV):
        data = na.V[i]
        print '{0: <30} {1: <20} {2: <20}'.format(na.VNAME[i], min(data), max(data))
        #print "%s\t\t\t%s\t\t%s" % (na.VNAME[i], min(data), max(data))
    

if __name__ == "__main__":

    main(sys.argv[1])
