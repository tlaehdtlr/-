def get_length(shark):
    visit = [[0]*N for _ in range(N)]
    cur = [shark]
    length = 0
    shortest = []
    visit[shark[0]][shark[1]] = 1
    while cur:
        length += 1
        next = []
        for r, c in cur:
            for nr, nc in (r+1, c), (r-1, c), (r, c+1), (r, c-1):
                if not (0 <= nr < N and 0 <= nc < N):
                    continue
                if visit[nr][nc] or (nr, nc) in impossible:
                    continue
                if (nr, nc) in possible:
                    shortest.append((nr, nc))
                next.append((nr, nc))
                visit[nr][nc] = 1
        if shortest:
            return shortest, length
        cur = next
    return False


N = int(input())
sea = [list(map(int, input().split())) for _ in range(N)]

# 먹힌 물고기 좌표
attacked = set()
# 크기 : {(좌표)}
fishes = dict()
# 상어 위치
shark_locat = (0, 0)
# 상어 크기, 얼마 먹었는지
shark_size = [2, 0]

for r in range(N):
    for c in range(N):
        if sea[r][c] == 9:
            shark_locat = (r, c)
        elif sea[r][c]:
            if fishes.get(sea[r][c]):
                fishes[sea[r][c]].add((r, c))
            else:
                fishes[sea[r][c]] = {(r, c)}

possible = set()  # 먹을거
impossible = set()  # 못지나감
for fish_size, rc in fishes.items():
    if fish_size < shark_size[0]:
        possible = possible | rc
    elif fish_size > shark_size[0]:
        impossible = impossible | rc

time = 0
while possible:
    res = get_length(shark_locat)
    if not res:
        break

    shortest, length = res
    # 제일 가까운 놈으로
    shortest.sort(key=lambda x: (x[0], x[1]))
    nr, nc = shortest[0]

    # 물고기 제거
    possible.discard((nr, nc))
    shark_locat = (nr, nc)

    # 먹음
    shark_size[1] += 1
    if shark_size[0] == shark_size[1]:
        shark_size[0] += 1
        shark_size[1] = 0
        for fish_size, rc in fishes.items():
            if fish_size == shark_size[0]-1:
                possible = possible | rc
            elif fish_size == shark_size[0]:
                impossible = impossible - rc
    time += length

print(time)
