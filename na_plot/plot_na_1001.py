#!/usr/bin/env python

"""
plot_na_1001.py
===============

Plots a y-vs-x graph from variable in a NASA Ames 1001 file.

"""


import sys
import os

import matplotlib.pyplot as plt
import numpy
import nappy


def read_data(fpath):
    f = nappy.openNAFile(fpath) 
    f.readData()
    return f

def plot_title_info(na, fpath, plt):
    title = "Source: %s;\nMission: %s;\nFile: %s" % (na.SNAME, na.MNAME, fpath)
    plt.figtext(.5, .95, 'File: %s' % fpath, fontsize=18, ha='center')
    plt.figtext(.5, .9, 'Source: %s' % na.SNAME, fontsize=16, ha='center') 
    plt.figtext(.5, .85, 'Mission: %s' % na.MNAME, fontsize=16, ha='center')

def plot_data(na_obj, fpath, vname1, vdata1, vname2, vdata2,
              x_limits=None, y_limits=None, marker=None):
#    plt.axis([0, 6, 0, 20]) # x_start, x_end, y_start, y_end
    plt.xlabel(vname1)
    plt.ylabel(vname2)
#    plt.title(fpath)
    plot_title_info(na_obj, fpath, plt)

    if x_limits: 
        plt.xlim(x_limits)
    if y_limits:
        plt.ylim(y_limits)

    if not marker: marker = 'r'
    plt.plot(vdata1, vdata2, marker)
    plt.savefig(os.path.basename(fpath) + ".png")
    plt.show()


def main(fpath, x_var_name, y_var_name, x_limits=None, y_limits=None, marker=None):
 
    na = read_data(fpath)

    vars = {}
    if x_limits: x_limits = [eval(x) for x in x_limits.split(",")]
    if y_limits: y_limits = [eval(y) for y in y_limits.split(",")]

    for i in range(na.NV):
        var_name = na.VNAME[i]
#        vars[var_name] = na.V[i]

        if var_name == x_var_name:
            x_var_data = na.V[i] 
        elif var_name == y_var_name:
            y_var_data = na.V[i]

    
    plot_data(na, fpath, x_var_name, x_var_data, y_var_name, y_var_data,
             x_limits=x_limits, y_limits=y_limits, marker=marker)
# y_var, var_key, vars[var_key],
#              x_limits=(100000, 130000), y_limits=(0,150))
     

if __name__ == "__main__":

    main(*sys.argv[1:])
