left = {(0,0):0, (0,-2):5, (-1,-1):10, (1,-1):10, (-1,0):7, (1,0):7, (-2,0):2, (2,0):2, (-1,1):1, (1,1):1}
down = {(0,0):0, (2,0):5, (1,-1):10, (1,1):10, (0,-2):2, (0,2):2, (0,-1):7, (0,1):7, (-1,-1):1, (-1,1):1}
right = {(0,0):0, (0,2):5, (-1,-1):1, (1,-1):1, (-2,0):2, (2,0):2, (-1,0):7, (1,0):7, (-1,1):10, (1,1):10}
up = {(0,0):0, (-2,0):5, (-1,-1):10, (-1,1):10, (0,-2):2, (0,2):2, (0,-1):7, (0,1):7, (1,-1):1, (1,1):1}
direc = [left, down, right, up]

def move(cur_direc, sr, sc, A, N):
    if cur_direc == 0:
        r,c = sr,sc-1
        ar, ac = r,c-1
    elif cur_direc == 1:
        r,c = sr+1,sc
        ar, ac = r+1,c
    elif cur_direc == 2:
        r,c = sr,sc+1
        ar, ac = r, c+1
    else:
        r,c = sr-1,sc
        ar, ac = r-1, c

    total = A[r][c]
    A[r][c] = 0
    subst = 0
    abandon = 0

    for drc, val in direc[cur_direc].items():
        dr,dc = drc
        new = total*val//100
        if not (0<= r+dr<N and 0<= c+dc < N):
            abandon += new
        else:
            A[r + dr][c + dc] += new
        subst += new

    if not (0<= ar <N and 0<= ac < N):
        abandon += total - subst
    else:
        A[ar][ac] += total - subst

    return r,c, abandon


def solve():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    length = 0
    cur_direc = -1
    sr,sc = N//2, N//2
    ans = 0
    while True:
        length += 1
        for _ in 1,2:
            cur_direc = (cur_direc + 1) % 4
            for _ in range(length):
                sr, sc, abandon = move(cur_direc, sr, sc, A, N)
                ans += abandon
        if length == N-1:
            break
    for _ in range(length):
        sr, sc, abandon = move(0, sr, sc, A, N)
        ans += abandon

    return ans


if __name__ == '__main__':
    print(solve())
