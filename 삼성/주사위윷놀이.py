def start(cur, horses, score):
    global ans
    if cur == 10:
        ans = max(ans, score)
        return

    pre_horses = []
    for i in range(len(horses)):
        pre_horses.append(horses[i][:])

    for horse in range(4):
        if cur == 0 and horse != 0:
            continue
        # 여기 좀 멍청한 거 같은데...
        for i in range(len(horses)):
            horses[i] = pre_horses[i][:]
        num_dice = dice[cur]
        idx, num_path = horses[horse]

        # 도착한 애임
        if num_path == 0:
            continue
        # 각 분기점으로 갈 수 있게
        if num_path == 1:
            if idx == 5:
                idx = 0
                num_path = 2
            elif idx == 10:
                idx = 0
                num_path = 3
            elif idx == 15:
                idx = 0
                num_path = 4
            else:
                # 마지막 지점 겹치는지
                if idx + num_dice == 20:
                    if [3, 5] in horses:
                        continue
                # 도착함
                elif idx + num_dice > 20:
                    horses[horse] = [0, 0]
                    start(cur+1, horses, score)
                    continue

        if num_path in {2, 3, 4}:
            # 경로 바꿔주고 남은 다이스도 바꿔주고
            if idx + num_dice >= len(path[num_path]):
                num_dice = num_dice - (len(path[num_path]) - idx)
                num_path = 5
                idx = 0

        if num_path == 5:
            if idx + num_dice == 3:
                if [20, 1] in horses:
                    continue
            # 도착함
            elif idx + num_dice > 3:
                horses[horse] = [0, 0]
                start(cur+1, horses, score)
                continue

        # 같은 패스에서 도착할 곳에 말 있는지 확인
        if [idx + num_dice, num_path] in horses:
            continue
        # gogo
        horses[horse] = [idx + num_dice, num_path]
        start(cur+1, horses, score+path[num_path][idx+num_dice])


dice = list(map(int, input().split()))

# 1,2,3,4,5 번길 만들거다
path = dict()
path[1] = [i for i in range(0, 42, 2)]
path[2] = [10, 13, 16, 19]
path[3] = [20, 22, 24]
path[4] = [30, 28, 27, 26]
path[5] = [25, 30, 35, 40]

ans = 0
start(0, [[0, 1] for _ in range(4)], 0)
print(ans)
