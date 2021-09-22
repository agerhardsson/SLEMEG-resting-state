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

root = os.getcwd()

files = glob(root + '/*_raw.fif')

overwrite = False

for file in files:
    newname = file.replace('_raw', '_ds_raw')
    newpath = root + '/data-ds-200Hz' + newname[newname.rindex('/'):]
    if overwrite or not os.path.exists(newpath):
        raw = mne.io.read_raw(file, preload=True)
        raw.resample(200)
        raw.anonymize()
        raw.save(newpath)
        del(raw)