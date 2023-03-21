#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    # Write your code here
    frequency = {}
    for i in s:
        if i in frequency:
            frequency[i] += 1
        else:
            frequency[i] = 1
    # case 1: same frequency
    if len(set(frequency.values())) == 1:
        return "YES"
    # case 2: more than 2 unique frenquencies
    elif len(set(frequency.values())) > 2:
        return "NO"
    # case 3: 2 unique frequencies
    else:
        for key in frequency:
            frequency[key] -= 1
            if len(set(frequency.values())) == 1:
                return "YES"
            frequency[key] += 1
        return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
