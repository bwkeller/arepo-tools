import re
import numpy as np
import pandas as pd
import collections

def info(fname):
    number = re.compile(r'\d+[.]*\d*[e-]*\d*')
    labels = ['Sync-Point', 'TimeBin', 'Time', 'Systemstep', 'Nsync-grv', 'Nsync-hyd']
    with open(fname, 'r') as infile:
        raw = [line for line in infile.readlines() if line != '\n']
        getnum = lambda idx: [float(number.findall(line)[idx]) for line in raw]
        data = {labels[i]:getnum(i) for i in range(len(labels))}
    return pd.DataFrame(data)

def cpu(fname):
    number = re.compile(r'\d+[.]*\d*[e-]*\d*')
    line = re.compile(r'Step.*?^$', re.DOTALL|re.MULTILINE)
    data = {'Step':[], 'Time':[], 'CPUs':[], 'MultiDomains':[],
            'HighestActiveTimeBin':[], 'total':[]}
    with open(fname, 'r') as infile:
        raw = line.findall(infile.read())
        for entry in raw:
            elms = entry.split('\n')
            add_entry = lambda name, e_idx, l_idx: data[name].append(float(number.findall(elms[e_idx])[l_idx]))
            add_entry('Step', 0, 0)
            add_entry('Time', 0, 1)
            add_entry('CPUs', 0, 2)
            add_entry('MultiDomains', 0, 3)
            add_entry('HighestActiveTimeBin', 0, 4)
            add_entry('total', 2, 0)
    return pd.DataFrame(data)
