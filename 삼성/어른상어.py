import sys
input = sys.stdin.readline


def move(alive, direc_shark, rc_shark, info_rc, time):
    occupied = set()
    next_alive = [0]*(M+1)
    next_direc_shark = [0]*(M+1)
    next_rc_shark = [(0, 0)]*(M+1)
    # 복사해야함
    next_info_rc = dict()
    for b, c in info_rc.items():
        next_info_rc[b] = c

    # 1번부터~
    for num in range(1, M+1):
        if not alive[num]:
            continue  # 이번 턴은 alive를 봐야해
        r, c = rc_shark[num]
        cur_direc = direc_shark[num]

        # 냄새없는칸 찾기
        flag = False
        for direc in priority_direc[num][cur_direc]:
            nr, nc = r+dr[direc], c+dc[direc]
            if not (0 <= nr < N and 0 <= nc < N):
                continue
            # 갈수있니?
            if info_rc[(nr, nc)][1] < time:
                flag = True
                # 중복 상어
                # 나는 번호 작은것부터 움직여서 만약 저기 있다면 걍 얘가 죽는거임
                if (nr, nc) in occupied:
                    break
                next_alive[num] = 1
                occupied.add((nr, nc))
                # 이긴 놈의 역사
                next_info_rc[(nr, nc)] = (num, time+K)
                next_direc_shark[num] = direc
                next_rc_shark[num] = (nr, nc)
                break
        # 갈데 없으면 자신 왔던칸
        if not flag:
            for direc in priority_direc[num][cur_direc]:
                nr, nc = r+dr[direc], c+dc[direc]
                if not (0 <= nr < N and 0 <= nc < N):
                    continue
                if info_rc[(nr, nc)][0] == num:
                    next_alive[num] = 1
                    occupied.add((nr, nc))
                    next_info_rc[(nr, nc)] = (num, time+K)
                    next_direc_shark[num] = direc
                    next_rc_shark[num] = (nr, nc)
                    break
    # 종료
    if sum(next_alive) == 1:
        return False
    return (next_alive, next_direc_shark, next_rc_shark, next_info_rc)


# 상하 좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

N, M, K = map(int, input().split())
sea = [list(map(int, input().split())) for _ in range(N)]
direc_shark = [0] + list(map(lambda x: int(x)-1, input().split()))
priority_direc = [[]]
for num in range(M):
    priority_direc.append(
        [list(map(lambda x:int(x)-1, input().split())) for _ in range(4)])

info_rc = dict()
alive = [0] + [1]*M
rc_shark = [(0, 0)]*(M+1)
for r in range(N):
    for c in range(N):
        num = sea[r][c]
        if num:
            rc_shark[num] = (r, c)
            # 상어번호, 없어지는 시간(다녀간 시간 + K)
            info_rc[(r, c)] = (num, K)
        else:
            info_rc[(r, c)] = (0, 0)
time = 0
while time < 1001:
    time += 1
    res = move(alive, direc_shark, rc_shark, info_rc, time)
    if not res:
        break
    alive, direc_shark, rc_shark, info_rc = res

if time > 1000:
    print(-1)
else:
    print(time)
