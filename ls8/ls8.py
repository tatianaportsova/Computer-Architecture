#!/usr/bin/env python3
# python3 ls8/ls8.py -v

"""Main."""

import sys
from cpu import *

cpu = CPU()
# cpu.load()
# cpu.run()
cpu.load(sys.argv[1])
cpu.run()