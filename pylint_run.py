#!/usr/bin/env python
# encoding: utf-8
"""
Author: Avis K
Purpose: It will run pylint for all .py files in a dir,
    and stores in a text file.
"""

from pylint.lint import Run
import glob, os

FILE_CONNECTION = open('pylint_scores.txt', 'w')

os.chdir('*path*')
for file_ in glob.glob("*.py"):
    results = Run([file_], exit=False)
    try:
        score = results.linter.stats['global_note']
    except KeyError:
        score = -1
    if score and score < 0:
        FILE_CONNECTION.write("{}  {}\n".format(file_, score))
        print file, '\t', score
FILE_CONNECTION.close()
