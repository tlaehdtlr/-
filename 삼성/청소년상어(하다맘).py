dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, -1, -1, -1, 0, 1, 1, 1]


def move_shark(sea, fishes):
    r, c = fishes[0]

    return attack


def move_fish(sea, fishes):
    for num in range(1, 17):
        if fishes[num]:
            r, c = fishes[num]
            _, direc = sea[r][c]
            for d in range(8):
                nr, nc = r+dr[(direc+d) % 8], c+dc[(direc+d) % 8]
                if not (0 <= nr < 4 and 0 <= nc < 4):
                    continue
                if sea[nr][nc][0] == 0:
                    continue  # 상어
                tar_num, tar_direc = sea[nr][nc]
                fishes[num] = (nr, nc)
                fishes[tar_num] = (r, c)
                sea[r][c] = (tar_num, tar_direc)
                sea[nr][nc] = (num, (direc+d) % 8)
                break


def hunt(r, c, sea, fishes):
    num, direc = sea[r][c]
    pre_r, pre_c = fishes[0]
    fishes[0] = (r, c)
    fishes[num] = None
    sea[pre_r][pre_c] = (-1, -1)
    sea[r][c] = (0, direc)


def main(sea, fishes, attack, res):
    copy_sea = [[] for _ in range(4)]
    for q in range(4):
        copy_sea[q] = sea[q][:]
    copy_fishes = fishes[:]

    for r, c in attack:
        plus_res = copy_fishes[r][c]
        new_sea = [[] for _ in range(4)]
        for q in range(4):
            copy_sea[q] = copy_sea[q][:]
        new_fishes = copy_fishes[:]

        hunt(num, new_sea, new_fishes)
        move_fish(new_sea, new_fishes)
        n_attack = shark(new_sea, new_fishes)
        main(new_sea, new_fishes, n_attack, res+plus_res)


origin = [list(map(int, input().split())) for _ in range(4)]
# sea num, direc, 빈곳은 -1,-1
sea = [[] for _ in range(4)]
# 물고기들 좌표 상어 0번
fishes = [(0, 0) for _ in range(17)]
for r in range(4):
    for c in range(4):
        sea[r].append((origin[r][2*c], origin[r][2*c+1]-1))
        fishes[origin[r][2*c]] = (r, c)

attack = [(0, 0)]
print(fishes)
