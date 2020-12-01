def go(populations):
    change = False
    for r in range(N):
        for c in range(N):
            if not change:
                if A[r][c] != populations[check[r][c]]:
                    change = True
                A[r][c] = populations[check[r][c]]
            else:
                A[r][c] = populations[check[r][c]]
    if change:
        return True
    else:
        return False


def organization(res, num):
    whole_popul = 0
    nums_countries = 0
    cur = [res]
    check[res[0]][res[1]] = num
    while cur:
        next = []
        for r, c in cur:
            popul = A[r][c]
            whole_popul += popul
            nums_countries += 1
            for nr, nc in (r+1, c), (r-1, c), (r, c+1), (r, c-1):
                if not (0 <= nr < N and 0 <= nc < N):
                    continue
                if check[nr][nc]:
                    continue
                if L <= abs(popul - A[nr][nc]) <= R:
                    next.append((nr, nc))
                    check[nr][nc] = num
        cur = next
    whole_popul = whole_popul//nums_countries
    return whole_popul


def check_countries():
    num = 0
    populations = [0]
    for r in range(N):
        for c in range(N):
            if not check[r][c]:
                num += 1
                populations.append(organization((r, c), num))
    return go(populations)


N, L, R = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

for ans in range(2001):
    check = [[0]*N for _ in range(N)]
    if not check_countries():
        break

print(ans)
