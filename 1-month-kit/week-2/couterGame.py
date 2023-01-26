#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'counterGame' function below.
#
# The function is expected to return a STRING.
# The function accepts LONG_INTEGER n as parameter.
#

def counterGame(n):
    # Write your code here
    answer = ["Louise", "Richard"]
    turn = 1
    summer = n
    while summer != 1:
        modulus = summer - 2**(math.log(summer)//math.log(2))
        if modulus != 0:
            summer = modulus
        else:
            summer = summer//2
        turn += 1
    return answer[turn%2]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = counterGame(n)

        fptr.write(result + '\n')

    fptr.close()
