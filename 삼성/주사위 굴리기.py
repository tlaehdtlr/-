def move(command, r,c):
    if command==1:
        c+=1
        if c>=M: return None
        dice[0] = dice[0][1:] + [dice[0][0]]
        dice[1][0] = dice[0][0]
        dice[1][2] = dice[0][2]
    elif command==2:
        c-=1
        if c<0: return None
        dice[0] = [dice[0][-1]] + dice[0][:-1]
        dice[1][0] = dice[0][0]
        dice[1][2] = dice[0][2]
    elif command==3:
        r-=1
        if r<0: return None
        dice[1] = [dice[1][-1]] + dice[1][:-1]
        dice[0][0] = dice[1][0]
        dice[0][2] = dice[1][2]
    elif command==4:
        r+=1
        if r>=N: return None
        dice[1] = dice[1][1:] + [dice[1][0]]
        dice[0][0] = dice[1][0]
        dice[0][2] = dice[1][2]
    return (r,c)


def copy(r,c):
    if road[r][c]==0:
        road[r][c] = dice[0][0]
    else:
        dice[0][0] = dice[1][0] = road[r][c]
        road[r][c] = 0


# 주사위
# 0 : 가로돌기(동+), 1 : 세로돌기(남+)
# [0,0] , [1,0] 이 현재 맞닿은 곳
dice = [[0]*4 for _ in range(2)]

# input
N, M, x, y, K = map(int, input().split())
road = [list(map(int, input().split())) for _ in range(N)]
commands = list(map(int, input().split()))
for command in commands:
    res = move(command, x,y)
    if res:
        x, y = res[0], res[1]
        copy(x,y)
        print(dice[0][2])