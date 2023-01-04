#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxPosPrefixes' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def maxPosPrefixes(arr):
    # Write your code here
    # we can sort the items in decending order to get the larger positive numbers to come first.
    # Then we can add the elements and count the number of positive prefix sums 
    arr.sort(reverse=True)
    
    # Variables for positive sum and count
    psum = 0
    cnt = 0
    
    # find psum and count positive psum
    for element in arr:
        psum += element
        
        if psum > 0:
            cnt += 1
    
    # return number of psums
    return cnt
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = maxPosPrefixes(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
