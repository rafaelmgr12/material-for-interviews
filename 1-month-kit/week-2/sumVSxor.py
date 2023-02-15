#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sumXor' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def sumXor(n):
    # Write your code here
    # Not optimal solution
    # count = 0
    # if n == 0:
    #     return 1
    # for i in range(n):
    #     if n + i == n ^ i:
    #         count += 1
    # return count

    # Optimal solution
    count = 0
    while n:
         if n % 2 == 0:
             count += 1
         n //= 2
    return 2**count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = sumXor(n)

    fptr.write(str(result) + '\n')

    fptr.close()
