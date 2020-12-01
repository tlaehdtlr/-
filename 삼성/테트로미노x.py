import sys
sys.stdin = open('./삼성/test.txt', 'r')
input = sys.stdin.readline

# 2x3 , 3x2 , 1x4, 4x1 고고
# 6칸


def rectangle(r, c, rc):
    rect_rc = [(r, c, paper[r][c])]
    if rc == 23:
        for nr, nc in (r, c+1), (r, c+2), (r+1, c), (r+1, c+1), (r, c+2):
            rect_rc.append((nr, nc, paper[nr][nc]))
    else:
        for nr, nc in (r, c+1), (r+1, c), (r+1, c+1), (r+2, c), (r+2, c+1):
            rect_rc.append((nr, nc, paper[nr][nc]))
    if sum(list(zip(*rect_rc))[2]) > ans:
        combi(rect_rc)


# 4칸으로
def combi(rect_rc, cur=[], num=0):
    global ans
    if num == 4:
        res = sum(list(zip(*cur))[2])
        if res < ans:
            return
        if check_link(cur):
            ans = res
        return

    for r, c, point in rect_rc:
        if (r, c, point) in cur:
            continue
        combi(rect_rc, cur+[(r, c, point)], num+1)


# 연결 확인
def check_link(lst_rc):
    check = []
    for r, c, point in lst_rc:
        check.append((r, c))
    link = [check[0]]

    for r, c in link:
        for nr, nc in (r+1, c), (r-1, c), (r, c+1), (r, c-1):
            if (nr, nc) in check:
                if (nr, nc) not in link:
                    link.append((nr, nc))

    if len(link) == 4:
        return True
    else:
        return False


N, M = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(N)]

ans = 0
# 1x4
for r in range(N):
    for c in range(M-3):
        ans = max(ans, sum(paper[r][c:c+4]))
# 4x1
con_paper = list(zip(*paper))
for r in range(M):
    for c in range(N-3):
        ans = max(ans, sum(con_paper[r][c:c+4]))

# 2x3
for r in range(N-1):
    for c in range(M-2):
        rectangle(r, c, 23)

# 3x2
for r in range(N-2):
    for c in range(M-1):
        rectangle(r, c, 32)

print(ans)
