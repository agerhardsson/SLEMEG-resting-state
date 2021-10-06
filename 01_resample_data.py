#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 14:48:24 2021

@author: andger
"""

import mne
import os
from glob import glob

# %%

root = os.getcwd()  # replace raw data path
datapath = root + '/data-ds-200Hz'
os.makedirs(datapath, exist_ok=True)
subjects = pd.read_csv('subjects.tsv', sep='\t')

pattern = '*empty*_raw.fif'
overwrite = False

for sub in subjects.Subj_ID:
    for session in ('con', 'psd'):
        path = datapath + '/*' + sub + '*' + session + '*'
        file = glob(path + pattern)[0]
        if overwrite or 'ds' not in file:
            raw = mne.io.read_raw(file, preload=True)
            raw.resample(200)
            raw.anonymize()
            raw.save(file.replace('_raw', '_ds_raw'))
            del(raw)
