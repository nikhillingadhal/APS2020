#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations
# Complete the substrings function below.
def substrings1(n):
    s=list(n)
    li=[]
    li.append(int(s[0]))
    count=li[0]
    for i in range(1,len(s)):
        li.append((i+1)*int(s[i])+10*int(li[i-1]))
        count+=(li[i])
        count=count%1000000007
    return count
def substrings(num):
    length=len(num)
    total=0
    X = [0]
    for i in range(length):
        X.append((X[-1]*10+1)%(10**9 +7))
        
    for i in range(length):
        toadd=(int(num[i]) *  ( (i+1) *  (X[length-i]%(10**9 +7) )  ))%(10**9 +7)
        total=(total+toadd)%(10**9 +7)
    return total
