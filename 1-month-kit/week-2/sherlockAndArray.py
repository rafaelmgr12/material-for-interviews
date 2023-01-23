#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'balancedSums' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def balancedSums(arr):
    # Write your code here
    # Not optimal solution
    #  for i in range(len(arr)):
    #     if sum(arr[:i]) == sum(arr[i+1:]):
    #         return "YES"
    # return "NO"
    
    right = sum(arr)
    left = 0
    for i in arr:
        right -= i
        if left == right:
            return "YES"
        left += i
    
    return "NO"


if __name__ == '__main__':

    arr = [1,2,3]

    result = balancedSums(arr)

    print(result)
  

