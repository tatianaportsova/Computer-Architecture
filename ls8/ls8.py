#!/usr/bin/env python3
# python3 ls8/ls8.py -v
# python3 ls8/ls8.py ls8/examples/mult.ls8
# python3 ls8/ls8.py ls8/examples/print8.ls8
# python3 ls8/ls8.py ls8/examples/stack.ls8

"""Main."""

import sys
from cpu import *

cpu = CPU()
# cpu.load()
cpu.load(sys.argv[1])
cpu.run()