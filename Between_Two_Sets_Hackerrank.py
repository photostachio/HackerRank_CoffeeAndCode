# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 08:53:05 2020

@author: User
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    # Write your code here
    j = a[len(a)-1]
    k = b[0]
    fact = []
    final = []
    count = 0
    for i in range(j, k+1):
        count = 0
        for c in b:
            if c%i == 0:
                count+=1
            else:
                break
        if count == len(b):
            fact.append(i)
        else:
            pass
    count = 0
    for q in fact:
        count = 0
        for p in a:
            if q%p == 0:
                count+=1
            else:
                break
        if count == len(a):
            final.append(q)
        else:
            pass
    return len(final)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
