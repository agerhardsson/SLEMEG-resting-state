#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 15:35:51 2021

@author: andger
"""
import mne
import os
from glob import glob

# %%

root = os.getcwd()
datapath = root + '/data-ds-200Hz'
files = glob(datapath + '/*_raw.fif')

overwrite = False
bp = (1, 60)

for file in files[0:2]:
    newname = file.replace('_ds_raw',
                           '_' + str(bp[0]) + '-' + str(bp[1]) + 'Hz_ds_raw')
    if overwrite or not os.path.exists(newpath):
        raw = mne.io.read_raw(file, preload=True)
        raw.filter(bp[0], bp[1])
        raw.save(newname)
        del(raw)
