#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Clear SVG
# Requires:
#   inkscape

import os
import glob
import subprocess

# Set working path
os.chdir(os.path.dirname(os.path.realpath(__file__)))

files = glob.glob('*.svg')
files += glob.glob('*/*.svg')

for svg in files:
    print '> ' + svg
    subprocess.call(['inkscape',
                     '--export-plain-svg=' + svg,
                     svg])
