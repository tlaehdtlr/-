def dfs(board, cnt):
    candi = 0
    if cnt == 5:
        for r in range(N):
            candi = max(candi, max(board[r]))
        return candi

    copy = []
    for i in range(N):
        copy.append(board[i][:])

    for direc in range(4):
        candi = max(candi, dfs(move(copy,direc),cnt+1))

    return candi


def move(board, direc):
    copy = [[0]*N for _ in range(N)]
    if direc == 0:      # 왼쪽으로
        for r in range(N):
            row = [0]*N
            cur = 0
            flag = False     # 전에거랑 합치기 가능?
            for val in board[r][:]:
                if val:
                    if flag and row[cur-1] == val:
                        row[cur-1] = val*2
                        flag = False
                    else:
                        row[cur] = val
                        cur+=1
                        flag=True
            copy[r] = row[:]

    elif direc == 1:      # 오른쪽으로
        for r in range(N):
            row = [0]*N
            cur = N-1
            flag = False
            for val in board[r][::-1]:
                if val:
                    if flag and row[cur + 1] == val:
                        row[cur + 1] = val * 2
                        flag = False
                    else:
                        row[cur] = val
                        cur -= 1
                        flag = True
            copy[r] = row[:]

    elif direc == 2:      # 위으로
        for c in range(N):
            col = [0]*N
            cur = 0
            flag = False
            for r in range(N):
                val = board[r][c]
                if val:
                    if flag and col[cur - 1] == val:
                        col[cur - 1] = val * 2
                        flag = False
                    else:
                        col[cur] = val
                        cur += 1
                        flag = True
            for cr in range(N):
                copy[cr][c] = col[cr]

    else:       #밑으로
        for c in range(N):
            col = [0] * N
            cur = N-1
            flag = False
            for r in range(N-1,-1,-1):
                val = board[r][c]
                if val:
                    if flag and col[cur + 1] == val:
                        col[cur + 1] = val * 2
                        flag = False
                    else:
                        col[cur] = val
                        cur -= 1
                        flag = True

            for cr in range(N):
                copy[cr][c] = col[cr]

    return copy


N = int(input())
origin = [list(map(int, input().split())) for _ in range(N)]
ans = dfs(origin,0)
print(ans)