def solve():
    new = [[[] for _ in range(N)] for _ in range(N)]
    #1
    for r in range(N):
        for c in range(N):
            if not board[r][c]:continue
            for fireball in board[r][c]:
                m,s,d = fireball
                nr,nc = r+s*dr[d], c+s*dc[d]
                if not (0<=nr<N):
                    nr = nr%N
                if not (0 <= nc < N):
                    nc = nc % N
                new[nr][nc].append([m,s,d])

    #2
    for r in range(N):
        for c in range(N):
            if len(new[r][c])<2: continue
            M,S,D =0, 0, new[r][c][0][2]
            S_cnt = 0
            D_flag = True
            for m,s,d in new[r][c]:
                M+=m
                S+=s
                S_cnt+=1
                if D_flag:
                    D_flag = (D%2 == d%2)
            M = M//5
            S = S//S_cnt
            if D_flag:
                D = [0,2,4,6]
            else:
                D = [1,3,5,7]
            new[r][c] = []
            if M:
                for new_f in range(4):
                    new[r][c].append([M,S,D[new_f]])
    return new


dr = [-1,-1,0,1,1,1,0,-1]
dc = [0,1,1,1,0,-1,-1,-1]

N,M,K = map(int, input().split())
board = [[[] for _ in range(N)] for _ in range(N)]

for _ in range(M):
    r,c,m,s,d = map(int, input().split())
    board[r-1][c-1].append([m,s,d])

for _ in range(K):
    new = solve()
    board = new

ans = 0
for r in range(N):
    for c in range(N):
        if board[r][c]:
            ans += sum(list(map(lambda x:x[0], board[r][c])))
print(ans)