#!/usr/bin/env python3
# NOTE: it is recommended to use this even if you don't understand the following code.

import sys

# uncomment the two following lines if you want to read/write from files
sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

N = int(input().strip())

X = [i for i in range(N)]
Y = [i for i in range(N)]

points = []
for i in range(N):
    X[i], Y[i] = map(int, input().strip().split())
    points.append([X[i], Y[i]])

ans = ""

avX = sum(X)/N
belowMiddle = []
overMiddle = []

points.sort()

count = sum(1 for row in points if row[0] == avX)

for i in range(0, N):
    if points[i][0] > avX:
        belowMiddle = points[:(i - count)]
        overMiddle = points[i:]
        break
    
if len(belowMiddle) != len(overMiddle):
    ans = "NO"
else:
    overMiddle.reverse()
    
for i in range(len(overMiddle)):
    if not(belowMiddle[i][0] == (2 * avX - overMiddle[i][0]) and belowMiddle[i][1] == overMiddle[i][1]):
        ans = "NO"
        break
    ans = "NO"
    if i == (len(overMiddle) - 1):
        ans = "YES"
        
print(ans)

sys.stdout.close()
