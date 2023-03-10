#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
harvest-genedb.py
Check the current IMGT/GENE-DB download page 
and download files if it's got a new release
"""

import subprocess
import urllib.request
import os
import shutil
import sys
from datetime import datetime

__email__ = 'jheather@mgh.harvard.edu'
__version__ = '0.1.0'
__author__ = 'Jamie Heather'

# Check the most recent release on record here
release_dir = '../releases/'
old_releases = [x for x in os.listdir(release_dir)]
old_releases.sort()
last_release = old_releases[-1].split('_')[-1]

print("Last banked release detected:\t" + last_release)

# Check current release
release_url = "https://www.imgt.org/download/GENE-DB/RELEASE"

try:
    with urllib.request.urlopen(release_url) as in_url:
        current_release = in_url.read().decode('utf-8')
except urllib.error.URLError as err:
    print(err.reason)
    sys.exit()

print("Currently available release:\t" + current_release)

if current_release != last_release:
    print("Newer release detected: downloading")
    wget_dir = 'www.imgt.org/'

    # Download whole release, move to appropriately named directory
    today = datetime.today().date().isoformat()
    out_dir = release_dir + '_'.join([today, 'GENEDB', current_release]) + '/'
    wget_cmd = "wget --recursive --no-clobber --page-requisites --convert-links " \
        "--domains www.imgt.org --no-parent https://www.imgt.org/download/GENE-DB/"
    subprocess.call(wget_cmd, shell=True)
    shutil.move(wget_dir + 'download/GENE-DB/', out_dir)

    # Then clean up unwanted files here and in that directory
    shutil.rmtree(wget_dir)
    clean_cmd = ("rm " + out_dir + '*=*')
    subprocess.call(clean_cmd, shell=True)
