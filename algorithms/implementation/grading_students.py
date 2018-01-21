#!/bin/python3

import sys

def solve(grades):
    results = []
    for grade in grades:
        reste = (5-grade%5)
        if grade+reste >= 40 and reste < 3:
            results.append(grade+reste)
        else:
            results.append(grade)
    return results

n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
   grades_t = int(input().strip())
   grades.append(grades_t)
result = solve(grades)
print ("\n".join(map(str, result)))


