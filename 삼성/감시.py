# 0 빈칸 / 6 벽 / 1~5 cctv / - 감시영역
# 동서남북
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]


def watch(r, c, direc, check):
    n_check = check.copy()
    while 0 <= r < N and 0 <= c < M:
        if office[r][c] == 6:
            break
        if office[r][c] == 0:
            n_check.add((r, c))
        r += dr[direc]
        c += dc[direc]
    return n_check


def DFS(cur, end, check):
    global ans
    if cur == end:
        ans = min(ans, blank - len(check))
        return

    r, c, tv = cctv[cur]
    if tv == 1:
        for direc in range(4):
            n_check = watch(r, c, direc, check)
            DFS(cur+1, end, n_check)
    elif tv == 2:
        for direc_1, direc_2 in (0, 1), (2, 3):
            n_check = watch(r, c, direc_1, check) | watch(r, c, direc_2, check)
            DFS(cur+1, end, n_check)
    elif tv == 3:
        for direc_1, direc_2 in (0, 2), (0, 3), (1, 2), (1, 3):
            n_check = watch(r, c, direc_1, check) | watch(r, c, direc_2, check)
            DFS(cur+1, end, n_check)
    else:
        for direc_1, direc_2, direc_3 in (0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3):
            n_check = watch(r, c, direc_1, check) | watch(
                r, c, direc_2, check) | watch(r, c, direc_3, check)
            DFS(cur+1, end, n_check)


N, M = map(int, input().split())
office = [list(map(int, input().split())) for _ in range(N)]
cctv = []
check = set()
blank = 0
for r in range(N):
    for c in range(M):
        if 0 < office[r][c] < 6:
            if office[r][c] == 5:
                for direc in range(4):
                    check = watch(r, c, direc, check)
            else:
                cctv.append((r, c, office[r][c]))
        elif office[r][c] == 0:
            blank += 1

ans = 98765
DFS(0, len(cctv), check)
print(ans)
