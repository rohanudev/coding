import sys
input = sys.stdin.readline

N = int(input())

plane = []

for _ in range(N):
    tmp = [int(w) for w in input().split()]
    plane.append(tmp)

plane_sorted = sorted(plane, key= lambda x: (x[1], x[0]))

for i in range(N):
    print(plane_sorted[i][0], plane_sorted[i][1])
    
"""
for x, y in plane_sorted:
    print(x, y) 
도 가능하다.
"""