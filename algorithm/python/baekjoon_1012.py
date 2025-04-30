import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
T = int(input())
for _ in range(T):
    M,N,K = map(int, input().strip().split())
    field = [[0]* M for _ in range(N)]

    for _ in range(K):
        x,y = map(int, input().strip().split())
        field[y][x] = 1
        
        
    def dfs(x,y):
        field[y][x] = 0
        
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < M and 0 <= ny < N and field[ny][nx] == 1:
                dfs(nx,ny)
                
    count = 0

    for y in range(N):
        for x in range(M):
            if field[y][x] == 1:
                dfs(x,y)
                count += 1


    print(count)