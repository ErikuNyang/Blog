#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'divisibleSumPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY ar
#

def divisibleSumPairs(n, k, ar):
    # Write your code here
    counter = 0 
    lastidx = len(ar) - 1 
    for i in range(lastidx):
        for item in ar[i+1:]:
            if ar[i] < item:
                if (ar[i] + item) % 3 == 0:
                    counter += 1
    print(counter)

            6 3
            1 3 2 6 1 2
    

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)
