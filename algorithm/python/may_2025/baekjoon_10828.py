import sys

input = sys.stdin.readline

N = int(input().strip())
answer = []
for _ in range(N):
    command = input().strip()
    
    if command == 'top':
        if len(answer):
            print(answer[-1])
        else:
            print(-1)
    
    if command == 'size':
        print(len(answer))
    
    if command == 'empty':
        if len(answer):
            print(0)
        else:
            print(1)
            
    if command == 'pop':
        if len(answer):
            tmp = answer.pop()
            print(tmp)
        else:
            print(-1)
    
    if command[:4] == 'push':
        _, num = command.split()
        answer.append(int(num))
