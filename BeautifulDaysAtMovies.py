#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulDays function below.
def beautifulDays(i, j, k):
    count=0
    for i in range(i,j+1):
        val1=str(i)
        val2=val1[::-1]
        val=abs(int(val1)-int(val2))
        if val//k==val/k:
            count+=1
    return count
