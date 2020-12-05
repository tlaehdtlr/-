import sys, time
input = sys.stdin.readline

# R(100) C(100) M(100x100)
def fish(king):
    for r in range(R):
        if sea[r][king]:
            s,d,z = sea[r][king]
            sea[r][king] = []
            sharks.pop(z)
            return z
    return 0

def move():
    new = [[[] for _ in range(C)] for _ in range(R)]
    print(sorted(sharks.items())[::-1])
    for num, rc in sorted(sharks.items())[::-1]:
        r,c = rc
        print('origin', num, r, c)
        s,d,z = sea[r][c]


        rs, cs = s%(2*(R-1)), s%(2*(C-1))
        print('rs,cs',rs,cs)
        r += rs*dr[d]
        c += cs*dc[d]
        if r>=R:
            if r>2*(R-1):
                r = r - 2*(R-1)
            else:
                r = 2*(R-1)-r
                d=0
        elif r<0:
            if r < -(R-1):
                r = -r - (R-1)
            else:
                r = -r
                d=1
        if c>=C:
            if c>2*(C-1):
                c = c - 2*(C-1)
            else:
                c = 2*(C-1)-c
                d=3
        elif c<0:
            if c < -(C-1):
                c = -c - (C-1)
            else:
                c = -c
                d=2

        print(r,c)
        if new[r][c]:
            sharks.pop(num)
            # print('먹힘')

        else:
            sharks[num] = [r,c]
            new[r][c] = [s,d,z]

    return new


R, C, M = map(int, input().split())

st = time.time()

sea = [[[] for _ in range(C)] for _ in range(R)]
# 위, 아래, 오른, 왼
dr = [-1,1,0,0]
dc = [0,0,1,-1]

sharks = dict()

for _ in range(M):
    # 위치, 속력, 이동방향, 크기
    r,c,s,d,z = map(int, input().split())
    sea[r-1][c-1] = [s,d-1,z]
    sharks[z] = [r-1,c-1]

ans = 0
king = 0

while king < C:
    print('-----움직이기 전-----')
    print(king, ans)
    for q in range(R):
        print(sea[q])

    ans += fish(king)
    new = move()
    sea = new
    print('움직임')
    print(king, ans)
    for q in range(R):
        print(sea[q])

    king+=1

print(ans)
# print(len(sharks.keys()))
print('시간:', time.time()-st)

'''
테케 만드는 코드
z = 0
s,d = 1000,0
for r in range(1,101):
    for c in range(1,101):
       z+=1
       d+=1
       d = d%4+1
       print(r,c,s,d,z, end=' ')
       print()

'''