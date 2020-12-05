import time
def check():
    for c in range(N):
        nc = c
        r = -1
        while r<H-1:
            r += 1
            nc += ladder[r][nc]
        if c != nc:
            return False
    return True


def set_col(cnt,pre):
    global ans, a
    a+=1
    if check():
        ans = cnt
        return
    if cnt+1 >= ans:
        return
    for cur in range(pre+1,len_horizon):
        r,c = horizon[cur]
        if not ladder[r][c] and not ladder[r][c+1]:
            ladder[r][c], ladder[r][c + 1] = 1,-1
            set_col(cnt+1, cur)
            ladder[r][c], ladder[r][c + 1] = 0, 0



st = time.time()
N, M, H = map(int, input().split())

ladder = [[0]*N for _ in range(H+1)]
# row, col(+1과 연결)
for _ in range(M):
    r,c = map(lambda x:int(x)-1, input().split())
    ladder[r][c], ladder[r][c+1] = 1, -1

# 번호를 다 정해주자 그러면 중복없이 계산이 가능하겠지
horizon = []
for r in range(H):
    for c in range(N-1):
        if not ladder[r][c] and not ladder[r][c+1]:
            horizon.append((r,c))
len_horizon = len(horizon)

ans = 4
a=1

set_col(0,-1)

if ans == 4:
    print(-1)
else:
    print(ans)
end = time.time()
print('호출횟수:',a)
print('시간:', end-st)
