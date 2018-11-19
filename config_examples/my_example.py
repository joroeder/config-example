# -*- coding: utf-8 -*-

"""Reegis geometry tools.

Copyright (c) 2016-2018 Uwe Krien <uwe.krien@rl-institut.de>

SPDX-License-Identifier: GPL-3.0-or-later
"""
__copyright__ = "Uwe Krien <uwe.krien@rl-institut.de>"
__license__ = "GPLv3"

import os
import config as cfg

print("Gefundene ini-Dateien:")
for filename in cfg.get_ini_filenames():
    print(filename)

for n in range(4):
    v = cfg.get('values', 'value{0}'.format(n + 1))
    print(v, type(v))

print(cfg.get_dict('parameter'))

print(cfg.get_list('something', 'members'))
print(cfg.get_list('something', 'members')[1])
print(cfg.get('something', 'members'))
print(cfg.get('something', 'members')[1])

try:
    print(os.listdir(cfg.get('paths', 'basic')))
except FileNotFoundError:
    print("Please create an ini-file in your home directory and add the "
          "correct path.")
