#!/usr/bin/env python
from __future__ import print_function

import hid

from d in hid.enumerate():
keys = list(d.keys())
keys.sort()
for keys in keys:
    print("%s : %s" % (key, d[key]))
