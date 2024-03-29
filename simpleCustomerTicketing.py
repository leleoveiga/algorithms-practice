#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the braces function below.
def isBalanced(s):
    brackets = []
    for i in range(len(s)):
        # brackets.append(s[i])
        if s[i] == "[" or s[i] == "{" or s[i] == "(":
            brackets.append(s[i])
        else:
            # print(brackets[-1])
            if len(brackets) > 0 and s[i] == "]" and brackets[-1] == "[" :
                brackets.pop()
            elif len(brackets) > 0 and s[i] == "}" and brackets[-1] == "{" :
                brackets.pop()
            elif len(brackets) > 0 and s[i] == ")" and brackets[-1] == "(" :
                brackets.pop()
            else:
                return "NO"
        print(brackets)
    return "NO" if len(brackets) > 0 else "YES"

def braces(values):
    print(values)
    outputs = []
    for i in range(len(values)):
        outputs.append(isBalanced(values[i]))
    return outputs
