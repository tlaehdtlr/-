def R_cal():
    global c_num
    for r in range(100):
        # A 로 옮길 것
        record = dict()
        for c in range(100):
            val = A[r][c]
            A[r][c] = 0
            if val:
                if record.get(val):
                    record[val] += 1
                else:
                    record[val] = 1
        if not record:
            continue

        # 정리
        tem = sorted(record.items(), key=lambda x: (x[1], x[0]))
        tem_len = len(tem)*2
        if tem_len > 100:
            tem_len = 100

        for i in range(tem_len//2):
            for j in range(2):
                val = tem[i][j]
                A[r][2*i+j] = val
        if c_num < tem_len:
            c_num = tem_len


def C_cal():
    global r_num
    for c in range(100):
        record = dict()
        for r in range(100):
            val = A[r][c]
            A[r][c] = 0
            if val:
                if record.get(val):
                    record[val] += 1
                else:
                    record[val] = 1
        if not record:
            continue

        tem = sorted(record.items(), key=lambda x: (x[1], x[0]))
        tem_len = len(tem)*2
        if tem_len > 100:
            tem_len = 100

        for i in range(tem_len//2):
            for j in range(2):
                val = tem[i][j]
                A[2*i+j][c] = val
        if r_num < tem_len:
            r_num = tem_len


R, C, K = map(int, input().split())
A = [[0]*100 for _ in range(100)]
for i in range(3):
    copy = list(map(int, input().split()))
    for j in range(3):
        A[i][j] = copy[j]

r_num = c_num = 3
time = 0
while True:
    if A[R-1][C-1] == K:
        print(time)
        break
    if time == 100:
        print(-1)
        break
    time += 1
    if r_num >= c_num:
        R_cal()
    else:
        C_cal()
