# 동, 북, 서, 남
# index: 0, 1, 2, 3
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
move_types = ['R','U','L','D']
# 현재 위치
x, y = 1, 1

n = int(input())
plans = input().split()
print(plans)

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]

        #이동한 위치가 보드를 벗어나지 않으면 위치 업데이트
        if 1 <= nx <= n and 1 <= ny <= n:
            x, y = nx, ny

print(x, y)