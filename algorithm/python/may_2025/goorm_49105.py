import sys
input = sys.stdin.readline

N = int(input())

ans = [int(w) for w in input().strip().split()]

M = int(input())

question = [int(q) for q in input().strip().split()]

for q in question:
    if q in ans:
        print(1)
    else:
        print(0)