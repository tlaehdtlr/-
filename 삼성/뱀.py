def move(tail_r, tail_c, head_r, head_c, direc, time):
    t = 0
    while t < time:
        t += 1
        n_head_r = head_r+dr[direc]
        n_head_c = head_c+dc[direc]
        # 벗어남
        if not (0 <= n_head_r < N and 0 <= n_head_c < N):
            return t, False, None
        # 자신 몸
        if board[n_head_r][n_head_c] > -1:
            return t, False, None
        # 사과
        if (n_head_r, n_head_c) in apples:
            apples.discard((n_head_r, n_head_c))
        # 꼬리 없앰
        else:
            d = board[tail_r][tail_c]
            board[tail_r][tail_c] = -1
            tail_r += dr[d]
            tail_c += dc[d]
        # 이동
        board[n_head_r][n_head_c] = direc
        head_r, head_c = n_head_r, n_head_c
    return t, True, [tail_r, tail_c, head_r, head_c]


# board에 방향을 남겨놓을거임 (북,동,남,서) D: +1, L: -1
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


N = int(input())
board = [[-1]*N for _ in range(N)]
board[0][0] = 1
K = int(input())

apples = set()
for _ in range(K):
    r, c = map(int, input().split())
    apples.add((r-1, c-1))

L = int(input())
change_direc = []
for _ in range(L):
    num, direc = map(str, input().split())
    num = int(num)
    change_direc.append((num, direc))

time = 0
direc = 1
tail_r, tail_c, head_r, head_c = 0, 0, 0, 0
idx = -1
while True:
    if idx + 1 == len(change_direc):
        num = 10000
        change = change_direc[idx][1]
    elif idx == -1:
        num = change_direc[0][0] - time
        change = 0
    else:
        num = change_direc[idx+1][0] - time
        change = change_direc[idx][1]

    if change == 'D':
        direc = (direc+1) % 4
    elif change == 'L':
        direc = (direc-1) % 4

    board[head_r][head_c] = direc

    t, conti, rc = move(tail_r, tail_c, head_r, head_c, direc, num)
    time += t
    if not conti:
        break
    tail_r, tail_c, head_r, head_c = map(int, rc)
    idx += 1

print(time)
