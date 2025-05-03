import heapq

N = int(input())

card_stack = []

for _ in range(N):
    input_num = int(input())
    heapq.heappush(card_stack,input_num)

sum = 0
while len(card_stack) > 1:
    
    num1 = heapq.heappop(card_stack)
    num2 = heapq.heappop(card_stack)
    sum_num = num1 + num2
    heapq.heappush(card_stack,sum_num)
    sum += sum_num
    
print(sum)