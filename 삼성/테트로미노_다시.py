import time
poliomino_1 = [[(0,0), (1,0), (2,0), (3,0)],
                [(0,0), (0,1), (0,2), (0,3)],
                [(0,0),(1,0),(0,1),(1,1)],
                [(0,0),(0,1),(1,1),(0,2)],
                [(0,0),(0,1),(-1,1),(0,2)]]

# 좌우 대칭
poliomino_rev_1 = [[(0,0), (0,1), (0,2), (1,2)],
                    [(0,0), (0,1), (0,2), (-1,2)],
                    [(0,0), (1,0), (2,0), (2,1)],
                    [(0,0), (-1,0), (-2,0), (-2,1)],
                    [(0,0), (1,0), (1,1), (2,1)],
                    [(0,0), (0,1), (1,1), (1,2)],
                    [(0,0),(1,0),(1,1),(2,0)]]
poliomino_rev_2 = []
for polio in poliomino_rev_1:
    poliomino_rev_2.append(list(map(lambda x: (x[0], x[1]*(-1)), polio)))

polios = poliomino_1 + poliomino_rev_1 + poliomino_rev_2

def tetromino():
    cnt = 0
    for r in range(N):
        for c in range(M):
            for polio in polios:
                candi = 0
                for pr,pc in polio:
                    nr,nc = r+pr, c+pc
                    if not (0<=nr<N and 0<=nc<M): candi=0; break;
                    candi += board[nr][nc]
                cnt = max(cnt,candi)
    return cnt


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
# ans = 0


st = time.time()


ans = tetromino()
# for polio in poliomino_1:
#     ans = max(ans,tetromino(polio))
#
# for polio in poliomino_rev_1:
#     ans = max(ans,tetromino(polio))
#     ans = max(ans, tetromino(list(map(lambda x: (x[0], x[1]*(-1)), polio))))

print(ans)
