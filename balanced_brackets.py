#!/bin/python

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    t = int(raw_input())

    for t_itr in xrange(t):
        expression = raw_input()
        arr = expression
        stack = list()
        n = len(arr)
        flag = False
        for i in range(n):
            if arr[i] == "(" or arr[i] == "[" or arr[i] == "{":
                stack.append(arr[i])
            else:
                if not stack:
                    print("NO")
                    flag = True
                    break
                b = stack.pop()
                if arr[i] == ")":
                    if b == "[" or b == "{":
                        print("NO")
                        flag = True
                        break
                if arr[i] == "]":
                    if b == "(" or b == "{":
                        print("NO")
                        flag = True
                        break
                if arr[i] == "}":
                    if b == "(" or b == "[":
                        print("NO")
                        flag = True
                        break
        if not flag and stack:
            print("NO")
            continue
        if not flag:
            print("YES")
