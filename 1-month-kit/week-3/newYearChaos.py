#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    # Write your code here
    bribes = 0
    q = [p-1 for p in q]
    for i,p in enumerate(q):
        current = i
        if p - current > 2:
            print("Too chaotic")
            return
        for j in range(max(p-1,0),i):
            if q[j] > p:
                bribes += 1
    print(bribes)

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
