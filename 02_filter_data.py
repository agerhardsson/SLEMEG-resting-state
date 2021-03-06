#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 15:35:51 2021

@author: andger
"""
import mne
import os
from glob import glob
import pandas as pd


# %%

root = os.getcwd()
datapath = root + '/data-ds-200Hz'
subjects = pd.read_csv('subjects.tsv', sep='\t')

bp = (1, 60)
bp_str = str(bp[0]) + '-' + str(bp[1]) + 'Hz'
pattern = '*eo_ds*_raw.fif'
overwrite = False

for sub in subjects.Subj_ID:
    for session in ('con', 'psd'):
        path = datapath + '/*' + sub + '*' + session + '*'
        file = glob(path + pattern)[0]
        if overwrite or bp_str not in file:
            raw = mne.io.read_raw(file)
            newname = file.replace('_ds_raw', '_' +
                                   bp_str + '_ds_raw')
            raw = mne.io.read_raw(file, preload=True)
            raw.filter(bp[0], bp[1])
            raw.save(newname)
            del(raw)
