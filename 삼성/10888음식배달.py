def delivery(cur):
    global ans
    cost = 0
    check = [[0] * N for _ in range(N)]
    for r, c in cur:
        cost += town[r][c]
        check[r][c] = 1
    dist = 0
    while cur:
        dist+=1
        next = []
        for r,c in cur:
            for nr,nc in (r-1,c),(r+1,c),(r,c-1),(r,c+1):
                if not (0<=nr<N and 0<=nc<N): continue
                if check[nr][nc]: continue
                if town[nr][nc] == 1:
                    cost += dist
                next.append((nr,nc))
                check[nr][nc] = 1
        cur = next
        if cost >= ans:
            return
    ans = cost


def combi(cur, num, idx):
    if num > len(rest): return
    if num>0:
        res[num].append(cur)
    for i in range(idx,len(rest)):
        combi(cur+[rest[i]], num+1, i+1)


T = int(input())
for tc in range(1,1+T):
    N = int(input())
    town = [list(map(int, input().split())) for _ in range(N)]
    ans = 9999*9999
    rest = []
    for r in range(N):
        for c in range(N):
            if town[r][c] > 1:
                rest.append((r, c))
    res = dict()
    for i in range(len(rest)+1):
        res[i] = []
    combi([], 0, 0)
    for j in range(len(rest),0,-1):
        if res[j]:
            for cur in res[j]:
                delivery(cur)

    print('#{} {}'.format(tc, ans))
