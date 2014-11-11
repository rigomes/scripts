#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Android SVG to Android Resource
# Requires:
#   inkscape
#   pngout

import os
import glob
import xml.etree.ElementTree as ET
import subprocess

from Tkinter import Tk
from tkFileDialog import askdirectory

# Set working path
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Densidades de DPI alvo:
dpis = [0.75, 1.0, 1.5, 2.0, 3.0, 4.0]
dpis_str = ['ldpi', 'mdpi', 'hdpi', 'xhdpi', 'xxhdpi', 'xxxhdpi']

os.system('cls' if os.name == 'nt' else 'clear')
print 'RES Builder'
print '----------------------------------------------------------'
print 'Densidades: '
for den in dpis_str:
    print den + ' ',

print '\n'

files = glob.glob('*.svg')
files += glob.glob('*/*.svg')
Tk().withdraw()
path = askdirectory().encode('utf8')
print 'Output Dir: ' + path

for svg in files:

    tree = ET.parse(svg)
    root = tree.getroot()
    width = int(root.attrib['width'])
    height = int(root.attrib['height'])

    for index in range(len(dpis)):
        dpi = dpis[index]
        dpi_str = dpis_str[index]

        current_path = path + '/drawable-' + dpi_str + '/'

        if not os.path.exists(current_path):
            os.makedirs(current_path)

        print svg + ' > ' + dpi_str

        twidth = int(round(width * dpi))
        theight = int(round(height * dpi))

        target = os.path.basename(svg)
        target = target.replace('.svg', '.png')
        target = target.lower()

        subprocess.call(['inkscape',
                         '-z',
                         '-e',
                         current_path + target,
                         '-f' + svg,
                         '-w ' + str(twidth),
                         '-h' + str(theight)])

        subprocess.call(['pngout',
                         current_path + target])


