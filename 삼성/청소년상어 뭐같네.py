# 12시부터 반시계
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, -1, -1, -1, 0, 1, 1, 1]


def move_fish(pre_locat_fishes, pre_sea):
    locat_fishes = pre_locat_fishes[:]
    sea = dict()
    for i, j in pre_sea.items():
        sea[i] = j
    for num in range(1, 17):
        rc = locat_fishes[num]
        # 물고기 죽음 ㅠㅠ
        if not rc:
            continue
        r, c = rc
        _, direc = sea[(r, c)]

        for d in range(8):
            n_direc = (direc + d) % 8
            nr, nc = r+dr[n_direc], c+dc[n_direc]
            if not (0 <= nr < 4 and 0 <= nc < 4):
                continue
            other = sea[(nr, nc)]
            if other:
                other_num, other_direc = other
                if other_num == 0:
                    continue  # 상어
                sea[(r, c)] = [other_num, other_direc]
                locat_fishes[other_num] = (r, c)
            else:
                # 빈칸
                sea[(r, c)] = None
            # 물고기 이동
            sea[(nr, nc)] = [num, n_direc]
            locat_fishes[num] = (nr, nc)
            break
    return locat_fishes, sea


def shark(locat_fishes, sea, res, dep):
    global ans
    ans = max(res, ans)
    pre_locat_fishes, pre_sea = move_fish(locat_fishes, sea)

    r, c = pre_locat_fishes[0]
    _, direc = pre_sea[(r, c)]

    nr, nc = r+dr[direc], c+dc[direc]
    while (0 <= nr < 4 and 0 <= nc < 4):
        # copy
        locat_fishes = pre_locat_fishes[:]
        sea = dict()
        for i, j in pre_sea.items():
            sea[i] = j
        other = sea[(nr, nc)]
        if other:
            other_num, other_direc = other
            sea[(r, c)] = []
            locat_fishes[other_num] = None
            # 사냥
            sea[(nr, nc)] = [0, other_direc]
            locat_fishes[0] = (nr, nc)
            shark(locat_fishes, sea, res+other_num, dep+1)
        nr, nc = nr+dr[direc], nc+dc[direc]


origin = [list(map(int, input().split())) for _ in range(4)]
sea = dict()
locat_fishes = [(0, 0)]*17
for i in range(4):
    for j in range(4):
        sea[(i, j)] = [origin[i][2*j], origin[i][2*j+1]-1]
        locat_fishes[origin[i][2*j]] = (i, j)


ans = sea[(0, 0)][0]
locat_fishes[sea[(0, 0)][0]] = None
sea[(0, 0)] = [0, sea[(0, 0)][1]]

shark(locat_fishes, sea, ans, 1)
print(ans)
