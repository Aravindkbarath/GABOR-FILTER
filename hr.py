#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def encryption(s):
    # Write your code here
    strin = s.strip()
    floor = math.floor(math.sqrt(len(strin)))
    ceil = math.ceil(math.sqrt(len(strin)))
    ans = [[]]
    arr = []
    cou = 0
    sol = ""
    dupstr = strin
    
    for i in range(len(strin)):
        if i!=0 and i%4==0:
            print("\n")
        print(i)
    
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
