#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def rotate(alph):
    return alph[1:]+alph[0] 
def caesarCipher(s, k):
    alph_origin="abcdefghijklmnopqrstuvwxyz"
    alph="abcdefghijklmnopqrstuvwxyz"
    if(k==0):
        return s
    while (k>0):
        alph=rotate(alph)
        k=k-1
    index=0
    s1=""
    print(alph)
    for i in s:
        if(i.isalpha()):
            if(i.lower()==i):
                print(i)
                ind=alph_origin.find(i)
                i=alph[ind]
                print(i)
            else:
                i=i.lower()
                ind=alph_origin.find(i)
                i=alph[ind].upper()
        s1=s1+i
        index=index+1
    return s1    
    # Write your code here
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
