import sys, heapq
input = sys.stdin.readline

N = int(input().strip())
heap_num = []

for _ in range(N):
    num = int(input().strip())
    if num:
        heapq.heappush(heap_num, num)
    else:
        if len(heap_num):
            print(heapq.heappop(heap_num))
        else:
            print(0)