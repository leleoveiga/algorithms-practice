#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'newPassword' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

def newPassword(a, b):
    i = 0
    j = 0
    res = ""
    while i < len(a) or j < len(b):
        if i < len(a):
            res += a[i]
            i += 1
        if j < len(b):
            res += b[j]
            j += 1
        # print(res)
    return res
        