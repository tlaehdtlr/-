dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def move(r, c, direc):
    cnt = 0
    while True:
        cnt += 1
        nr = r+dr[direc]*cnt
        nc = c+dc[direc]*cnt
        if board[nr][nc] == '#':
            return False, nr-dr[direc], nc-dc[direc], cnt-1
        elif board[nr][nc] == 'O':
            return True, nr, nc, cnt


def escape():
    turn = 0
    cur_R = R[:]
    cur_B = B[:]
    while cur_R:
        # print(turn)
        # print(cur_R)
        # print(cur_B)
        if turn >= 10:
            break
        turn += 1
        next_R = []
        next_B = []
        for i in range(len(cur_R)):
            r_R, c_R = cur_R[i]
            r_B, c_B = cur_B[i]
            for direc in range(4):
                check_R, nr_R, nc_R, cnt_R = move(r_R, c_R, direc)
                check_B, nr_B, nc_B, cnt_B = move(r_B, c_B, direc)
                if check_R and not check_B:
                    return turn
                if check_R or check_B:
                    continue
                if (nr_R, nc_R) == (nr_B, nc_B):
                    if cnt_R > cnt_B:
                        nr_R -= dr[direc]
                        nc_R -= dc[direc]
                    else:
                        nr_B -= dr[direc]
                        nc_B -= dc[direc]
                if ((nr_R, nc_R), (nr_B, nc_B)) in memo:
                    continue
                memo.add(((nr_R, nc_R), (nr_B, nc_B)))
                next_R.append((nr_R, nc_R))
                next_B.append((nr_B, nc_B))

        cur_R = next_R
        cur_B = next_B

    return False


N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

for r in range(N):
    for c in range(M):
        if board[r][c] == 'R':
            R = [(r, c)]
        elif board[r][c] == 'B':
            B = [(r, c)]
memo = {(R[0], B[0])}
ans = escape()
if ans:
    print(ans)
else:
    print(-1)
