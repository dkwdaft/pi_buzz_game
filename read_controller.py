#!usr/bin/env python
import hid
import time

h = hid.device()
h.open(0x54c, )
