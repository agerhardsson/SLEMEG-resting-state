# The SLEMEG Project

## Data sharing agreement

While waiting for further clarifications regarding data sharing of MEG-data pleae adhear to the following:

By using the data you agree to the following statements:

- I will not share or make data publically available
- I will not make efforts to identify any person behind the data

## Project description

The overaching aim of this project was to study the effect of partial sleep deprivation on neurophysiological processes using Magnetoencephalography (MEG).

It was a within-subjects design, with participants performing the same tasks twice - once after normal sleep and once after two nights of sleep restricted to 4 hours (01:00-05:00). The measurments were done on NatMEG (www.natmeg.se) at Karolinska Institutet.

When comming to the lab the participants started by filling out some questionnaires about sleepiness, sleepiness related symptoms and affective state, afterwich they performed a 5 minutes psychomotor vigilance test (PVT).

In the MEG scanner the participants performed the following three tasks:
1. Emotional attention task (35 min)
2. Mindwandering task (12 min)
3. Resting statement
  - eyes open (5 min)
  - eyes closed (5 min)

Resting state is a commonly used paradigm in neuroscience aiming to measure the brains activity when nothing in particular is going on. Subjects are instructed to, either with eyes open or closed, relax and not think of anything specific, in this case for five minutes.

## Data description

File names:

Example:
sub-01_ses-con_task_rest_ec_ds_raw.fif

psd = partial sleep deprivation
con = control condition
rest = resting state
eo = eyes open
ec = eyes closed
ds = downsampled

The subjects.tsv data file contains the following information:

Subj_ID: subjects identification number
Age: age in years
Gender: M = Male, F = Female
PSDfirst: order of session with 1 indicating psd session as first session
test_time: approximate time of testing (24h)


## Preprocessing

All data has been preprocessed using [MaxFilter](https://link.springer.com/article/10.1023%2FB%3ABRAT.0000032864.93890.f9) with the following parameters:
- continues head position median averaging
- movement correction
- temporal signal space separation
- cut-off correlation of 0.98

This is commonly done in MEG to remove irrelevant noise caused by head movements and e.g. metal dental retainers.

Then the data was downsampled from 1000Hz to 200Hz.

Other than that, no preprocessing has been done.

There are several ways to further preprocess data.

See [MNE preprocessing](https://mne.tools/stable/preprocessing.html) for further options.

ICA could be a good option to remove artifacts caused by eye blinks and heartbeat.
