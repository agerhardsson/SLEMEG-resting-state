#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 15:35:51 2021

@author: andger
"""
import mne
from mne import compute_raw_covariance
import os
from glob import glob

# %%

root = os.getcwd()
datapath = root + '/data-ds-200Hz'
subjects = pd.read_csv('subjects.tsv', sep='\t')

pattern = '*empty*_raw.fif'
overwrite = False

for sub in subjects.Subj_ID:
    for session in ('con', 'psd'):
        path = datapath + '/*' + sub + '*' + session + '*'
        file = glob(path + pattern)[0]
        fname = file.replace('_ds_raw', '_noise_cov')
        if overwrite or not os.path.exists(fname):
            raw = mne.io.read_raw(file, preload=True)
            noise_cov = compute_raw_covariance(raw)
            mne.write_cov(fname, noise_cov)
            del(raw)
