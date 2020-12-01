dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def escape(turn, R_rc, B_rc, pre_direc):
    global ans
    if turn >= ans:
        return
    # print('----------', turn, '-----------')
    # for q in range(N):
    #     print(board[q])
    R_r, R_c = R_rc
    B_r, B_c = B_rc
    for direc in range(4):
        R_nr, R_nc = R_r+dr[direc], R_c+dc[direc]
        B_nr, B_nc = B_r+dr[direc], B_c+dc[direc]
        next_R_rc = (R_nr, R_nc)
        next_B_rc = (B_nr, B_nc)
        possible = False

        if not (0 <= R_nr < N and 0 <= R_nc < M) or board[R_nr][R_nc] == '#':
            next_R_rc = (R_r, R_c)
        elif board[R_nr][R_nc] == 'O':
            possible = True

        if not (0 <= B_nr < N and 0 <= B_nc < M) or board[B_nr][B_nc] == '#':
            next_B_rc = (B_r, B_c)

        if next_R_rc == next_B_rc:
            continue
        if possible:
            print('----------', turn, '-----------')
            for q in range(N):
                print(board[q])
            ans = turn
            return

        if not (next_R_rc == R_rc and next_B_rc == B_rc):

            board[R_r][R_c] = '.'
            board[B_r][B_c] = '.'

            board[next_R_rc[0]][next_R_rc[1]] = 'R'
            board[next_B_rc[0]][next_B_rc[1]] = 'B'
            if pre_direc == direc:
                escape(turn, next_R_rc, next_B_rc, direc)
            else:
                escape(turn+1, next_R_rc, next_B_rc, direc)
            board[next_R_rc[0]][next_R_rc[1]] = '.'
            board[next_B_rc[0]][next_B_rc[1]] = '.'
            board[R_r][R_c] = 'R'
            board[B_r][B_c] = 'B'


N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

for r in range(N):
    for c in range(M):
        if board[r][c] == 'R':
            R = (r, c)
        elif board[r][c] == 'B':
            B = (r, c)
# print('----------', turn, '-----------')
# for q in range(N):
#     print(board[q])
ans = 11
escape(1, R, B, None)
if ans > 10:
    print(-1)
else:
    print(ans)
