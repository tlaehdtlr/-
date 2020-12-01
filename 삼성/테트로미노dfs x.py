# 4칸이기 때문에 한번에 3방향씩 나가는 일은 신경쓸 필요없음 max 2칸씩
def tetro(rc, point, num, pre):
    global ans
    if num == 4:
        ans = max(ans, point)
        return
    elif num > 4:
        return

    n_rc = []
    for r, c in rc:
        n_point = point
        n_num = num
        for nr, nc in (r+1, c), (r-1, c), (r, c-1), (r, c+1):
            if not (0 <= nr < N and 0 <= nc < M):
                continue
            if check[nr][nc] or (nr, nc) in pre:
                continue
            n_rc.append((nr, nc))

    for n_num in range(len(n_rc)):
        res = combi(n_rc, n_num)
        if res:
            n_rc, n_point, n_pre = res
            tetro(rc+n_rc, point+n_point, num+n_num, pre+n_pre)


def combi(rc, point, num, cur, dep):
    if num == dep:
        return rc, point, num, cur
    for i in rc:
        if i in cur:
            continue
        r, c = i
        res = combi(rc, point+paper[r][c], num+1, cur+[(r, c)])
    return


N, M = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(N)]
check = [[0]*M for _ in range(N)]
ans = 0
for r in range(N):
    for c in range(M):
        check[r][c] = 1
        tetro([(r, c)], paper[r][c], 1, [(r, c)])
print(ans)
