import sys
input = sys.stdin.readline

# 연결 리스트로 풀어봐야징


class Horse:
    def __init__(self, num, direc):
        self.num = num
        self.direc = direc
        self.up = None
        self.down = None
        self.up_num = 1


# 동서 북남
dr = [0, 0, 0, -1, 1]
dc = [0, 1, -1, 0, 0]


def move(horse, r, c, blue):
    direc = horse.direc

    nr, nc = r+dr[direc], c+dc[direc]
    if chess[nr][nc] == 0:
        init(horse)
        link(horse, nr, nc)

    elif chess[nr][nc] == 1:
        # 반전
        last = horse.down
        horse.down = horse.up
        horse.up = None
        horse.up_num = 1
        while horse.down:
            next = horse.down.down
            horse.down.down = horse.down.up
            horse.down.up = horse
            horse.down.up_num = 1 + horse.up_num
            horse = horse.down
        horse.down = last
        if last:
            last.up = horse
            last.up_num = 1 + horse.up_num

        init(horse)
        link(horse, nr, nc)

    else:
        # 오도가도 못함
        if blue:
            stop[horse.num] = 1
            return
        else:
            if direc == 1:
                direc = 2
            elif direc == 2:
                direc = 1
            elif direc == 3:
                direc = 4
            elif direc == 4:
                direc = 3
            horse.direc = direc
            move(horse, r, c, True)


# 이동 전에 연결 끊기
def init(horse):
    down_horse = horse.down
    if down_horse:
        horse.down = None
        down_horse.up = None
        # 남는 애들 숫자
        down_horse.up_num = 1
        while down_horse.down:
            down_horse.down.up_num = 1+down_horse.up_num
            down_horse = down_horse.down


# 좌표 업데이트
def go(horse, r, c):
    horses_rc[horse] = [r, c]
    up_horse = horse.up
    # 같이 가는 말 있으면 좌표 업댓
    while up_horse:
        horses_rc[up_horse] = [r, c]
        up_horse = up_horse.up


# 가서 연결
def link(horse, r, c):
    global flag
    # 그 위치에 제일 위 말 확인
    last_horse = None
    for adv, rc in horses_rc.items():
        if rc == [r, c]:
            # print('뭐냐고', adv.num, rc)
            while adv.up:
                adv = adv.up
            last_horse = adv

    go(horse, r, c)

    # 있으면 말 포개기
    if last_horse:
        horse.down = last_horse
        last_horse.up = horse
        last_horse.up_num = 1 + horse.up_num
        while last_horse.down:
            last_horse.down.up_num = 1 + last_horse.up_num
            last_horse = last_horse.down

        # 정답!!!
        if last_horse.up_num >= 4:
            flag = True
            return


N, K = map(int, input().split())
# 0 흰, 1 빨, 2 파
chess = [[2]*(N+2)]
for _ in range(N):
    chess.append([2] + list(map(int, input().split())) + [2])
chess.append([2]*(N+2))

horses = [0]*K
horses_rc = dict()
for i in range(K):
    r, c, direc = map(int, input().split())
    horse = Horse(i, direc)
    horses_rc[horse] = [r, c]
    horses[i] = horse
    horse.num = i

turn = 0

ans = -1
# 이동 불가 체크
stop = [0]*K

# 정답 체크
flag = False
while turn < 1000:
    turn += 1
    for horse in horses:
        r, c = horses_rc[horse][0], horses_rc[horse][1]
        move(horse, r, c, False)
    if flag:
        ans = turn
        break

    if sum(stop) == K:
        break
print(ans)
