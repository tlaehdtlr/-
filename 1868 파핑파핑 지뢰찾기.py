# 0 인 지점 우선으로 찍어봐야한다
def find_zero_preprocess(N, origin, check_origin):
    start_point = []
    for i in range(N):
        for j in range(N):
            if origin[i][j]=='.':
                num_mine = check_8(i,j,N)
                if not num_mine:
                    start_point.append((i,j))
                origin[i][j] = num_mine
            else:
                check_origin[i][j] = True
    return start_point


dr = [-1,-1,0,1,1,1,0,-1]
dc = [0,1,1,1,0,-1,-1,-1]
def check_8(r,c,N):
    mine = 0
    for d in range(8):
        nr = r + dr[d]
        nc = c + dc[d]
        if not (0 <= nr < N and 0 <= nc < N): continue
        if origin[nr][nc] == '*':
            mine += 1
    return mine


def expand(origin, check_origin, N, r, c):
    start=[(r,c)]
    check_origin[r][c] = True
    while start:
        next = []
        for r,c, in start:
            for d in range(8):
                nr = r + dr[d]
                nc = c + dc[d]
                if not (0 <= nr < N and 0 <= nc < N): continue
                if check_origin[nr][nc]: continue
                check_origin[nr][nc] = True
                value = origin[nr][nc]
                if value == 0:
                    next.append((nr,nc))
        start = next


T = int(input())
for tc in range(1,1+T):
    N = int(input())
    origin = [list(input()) for _ in range(N)]
    check_origin = [[False]*N for _ in range(N)]

    start_point = find_zero_preprocess(N, origin, check_origin)

    ans = 0
    for r,c, in start_point:
        if check_origin[r][c]:continue
        expand(origin, check_origin, N, r, c)
        ans += 1

    for i in range(N):
        for j in range(N):
            if not check_origin[i][j]:
                ans += 1
    print('#{} {}'.format(tc, ans))