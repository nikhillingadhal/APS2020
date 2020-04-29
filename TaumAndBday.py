#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'taumBday' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER b
#  2. INTEGER w
#  3. INTEGER bc
#  4. INTEGER wc
#  5. INTEGER z
#

def taumBday(b, w, bc, wc, z):
    val=bc
    val1=wc
    if wc+z<bc:
        val=wc+z
    if bc+z<wc:
        val1=bc+z
    return (val*b)+(val1*w)


