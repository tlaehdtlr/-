# 12 반시계방향
dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]


def move(block, r, c, direc, value, used):
    k = 0
    while True:
        k += 1
        nr = r+dr[direc]*k
        nc = c+dc[direc]*k
        if not (0 <= nr < N and 0 <= nc < N) or (block[(nr, nc)][0] and (block[(nr, nc)][1] or used)):
            nr -= dr[direc]
            nc -= dc[direc]
            block[(r, c)] = (0, False)
            block[(nr, nc)] = (value, used)
            return
        elif block[(nr, nc)][0] and not block[(nr, nc)][1] and not used:
            if block[(nr, nc)][0] == value:
                block[(r, c)] = (0, False)
                block[(nr, nc)] = (2*value, True)
            return


def game(block, num, a):
    global ans
    res = max(list(map(lambda x: x[0], block.values())))
    if res >= ans:
        print(num)
        # print(block)
        print(a)
        ans = res
    if num > 5:
        return

    for direc in range(4):
        new_block = dict()
        for q, w in block.items():
            new_block[q] = (w[0], False)

        if direc in {0, 1}:
            st = 0
            en = N
            gap = 1
        else:
            st = N-1
            en = -1
            gap = -1
        for r in range(st, en, gap):
            for c in range(st, en, gap):
                val, used = new_block[(r, c)]
                if val:
                    move(new_block, r, c, direc, val, used)
        game(new_block, num+1, a+[direc])


N = int(input())
origin = [list(map(int, input().split())) for _ in range(N)]
block = dict()
for r in range(N):
    for c in range(N):
        block[(r, c)] = (origin[r][c], False)

ans = 0
game(block, 1, [])
print(ans)
