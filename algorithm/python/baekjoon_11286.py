import sys, heapq, math

input = sys.stdin.readline
abs_heap = []
num = int(input().strip())

for _ in range(num):
    tmp = int(input().strip())
    if tmp:
        heapq.heappush(abs_heap,(abs(tmp), tmp))
    else:
        if abs_heap:
            ans = heapq.heappop(abs_heap)
            print(ans[1])
        else:
            print(0)