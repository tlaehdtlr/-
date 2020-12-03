import time
# 이거는 생각해보니 중복이 많긴해
# (1,2), (2,4) 이렇게 했으면서 나중에 또 (2,4),(1,2) 이런식으로 돼
# 이럴바에는 조합이 낫겠다 야

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


def set_col(cnt):
    global ans, a
    a+=1
    if check():
        ans = cnt
        return
    if cnt+1 >= ans:
        return
    for r in range(H):
        c=0
        while c<N-1:
            if ladder[r][c]:
                c+=2
            elif ladder[r][c+1]:
                c+=3
            else:
                ladder[r][c], ladder[r][c+1] = 1,-1
                set_col(cnt+1)
                ladder[r][c], ladder[r][c + 1] = 0, 0
                c+=1



st = time.time()
N, M, H = map(int, input().split())

ladder = [[0]*N for _ in range(H+1)]
# row, col(+1과 연결)
for _ in range(M):
    r,c = map(lambda x:int(x)-1, input().split())
    ladder[r][c], ladder[r][c+1] = 1, -1

ans = 4
a=1
set_col(0)

if ans == 4:
    print(-1)
else:
    print(ans)
end = time.time()
print(a)
print('시간:', end-st)