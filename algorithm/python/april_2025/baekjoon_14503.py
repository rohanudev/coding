import sys
input = sys.stdin.readline

N,M = map(int, input().strip().split())

r, c, d = map(int, input().strip().split())

room = []

for _ in range(N):
    tmp = [int(w) for w in input().strip().split()]

    room.append(tmp)

# 북, 동, 남, 서 순서
dx = [0, 1, 0, -1]  # x(열)
dy = [-1, 0, 1, 0]  # y(행)

def turn_left(d):
    return (d + 3) % 4

count = 0
while True:
    if room[r][c] == 0:
        room[r][c] = 2  # 청소 표시
        count += 1

    cleaned = False  # 4방향 중 청소 가능한 칸이 있었는지

    for _ in range(4):
        d = turn_left(d)
        nx = c + dx[d]
        ny = r + dy[d]

        if 0 <= nx < M and 0 <= ny < N and room[ny][nx] == 0:
            r, c = ny, nx
            cleaned = True
            break  # 방향 회전 + 전진

    if not cleaned:
        # 후진 방향: (현재 방향 + 2) % 4
        back_d = (d + 2) % 4
        bx = c + dx[back_d]
        by = r + dy[back_d]

        if 0 <= bx < M and 0 <= by < N and room[by][bx] != 1:
            r, c = by, bx  # 후진
        else:
            break  # 후진 불가능 → 작동 종료

print(count) # 답 제출