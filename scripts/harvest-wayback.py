#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
harvest-wayback.py
Go through the WayBackMachine entries for the IMGT/GENE-DB download page and download files
Uses the 'reference/wayback-links.txt' document, which contains a manual scrape of all dates as of 2023-02-28
NB: only one snapshot per date included
"""

import subprocess
import os
import shutil
import sys
from datetime import datetime

__email__ = 'jheather@mgh.harvard.edu'
__version__ = '0.1.0'
__author__ = 'Jamie Heather'

# Read in URLs
with open('../reference/wayback-links.txt') as in_file:
    urls = [x for x in list(set(in_file.read().splitlines())) if x]

urls.sort()

# Make a temporary folder to work in
tmp_dir = '.tmp-wayback-dir'
if tmp_dir in os.listdir(os.getcwd()):
    print('Warning: existing temporary directory detected: delete if safe, and re-run')
    sys.exit()

os.mkdir(tmp_dir)
os.chdir(tmp_dir)

# Then go through each url in turn and scrape it into its own folder with just the data
base_cmd = "wget --recursive --no-clobber --page-requisites --convert-links --domains web.archive.org --no-parent "
for url in urls:
    timestamp = url.split('/')[4]
    date = datetime.strptime(timestamp[:8], '%Y%m%d').strftime('%Y-%m-%d')

    # Run bash wget to download the available data
    cmd = base_cmd + url
    subprocess.call(cmd, shell=True)

    # Then retain the appropriate subdirectory
    data_timestamp_possibilities = os.listdir('web.archive.org/web/')
    data_timestamp_possibilities.sort()
    data_timestamp = data_timestamp_possibilities[0]
    data_dir = '/'.join(['web.archive.org/web', data_timestamp, 'https:/imgt.org/download/GENE-DB/'])

    with open(data_dir + 'RELEASE', 'r') as in_file:
        release = in_file.readline().rstrip()

    out_dir_nam = date + '_WBM_' + release
    shutil.move(data_dir, out_dir_nam)
    shutil.rmtree('web.archive.org')

    # Then ensure there's only one entry per release number, keeping the earliest
    release_dirs = os.listdir(os.getcwd())
    releases = list(set([x.split('_')[2] for x in release_dirs]))
    releases.sort()

    for release in releases:
        matching_dirs = [x for x in release_dirs if x.endswith(release)]
        matching_dirs.sort()
        shutil.move(matching_dirs[0], '../../releases/' + matching_dirs[0])

os.chdir('../')
shutil.rmtree(tmp_dir)
