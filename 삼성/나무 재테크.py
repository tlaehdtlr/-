import time

def year():
    # 봄, 여름, 겨울
    next = []
    for r in range(N):
        for c in range(N):
            if trees[r][c]:
                spend, nutriments, next_rc = spring(r, c)
                # 양분 정산
                earth[r][c] += (nutriments - spend)
                next.append((r,c,next_rc))
            earth[r][c] += A[r][c]

    # 가을
    for r, c, next_tree in next:
        if next_tree:
            for nr, nc in (r - 1, c), (r - 1, c + 1), (r, c + 1), (r + 1, c + 1), (r + 1, c), (r + 1, c - 1), (r, c - 1), (r - 1, c - 1):
                if not (0 <= nr < N and 0 <= nc < N): continue
                trees[nr][nc].append([1, next_tree])


def spring(r,c):
    spend = 0
    nutriments = 0
    next = 0
    death = len_trees = len(trees[r][c])
    trees[r][c].sort()
    for idx in range(len_trees):
        tree = trees[r][c][idx]
        age, cnt = tree
        if idx < death:
            if spend + cnt*age <= earth[r][c]:
                spend += cnt*age
                # 번식 가능?
                if age % 5 == 4: next += cnt
            else:
                alive = 0
                death = idx
                while alive<cnt:
                    if spend + age <= earth[r][c]:
                        spend += age
                        alive += 1
                    else:
                        break
                nutriments += (age//2)*(cnt-alive)
                tree[1] = alive
                if age % 5 == 4: next += alive
            tree[0] += 1
        # 이미 초과
        else:
            nutriments+=cnt*(age//2)


    trees[r][c] = trees[r][c][:death+1]
    return spend, nutriments, next


# 땅, 나무, 시간
N, M, K = map(int, input().split())

st = time.time()


# 나무
trees = [[[] for _ in range(N)] for _ in range(N)]


A = []
for _ in range(N):
    A.append(list(map(int, input().split())))

for _ in range(M):
    r, c, age = map(int, input().split())
    trees[r-1][c-1].append([age,1])

earth = [[5]*N for _ in range(N)]

for cc in range(K):
    year()

ans = 0
for r in range(N):
    for c in range(N):
        for age, cnt in trees[r][c]:
            ans+=cnt

print(ans)

end = time.time()
print('시간:', end-st)

'''
10 2 1000
100 100 100 100 100 100 100 100 100 100
100 100 100 100 100 100 100 100 100 100
100 100 100 100 100 100 100 100 100 100
100 100 100 100 100 100 100 100 100 100
100 100 100 100 100 100 100 100 100 100
100 100 100 100 100 100 100 100 100 100
100 100 100 100 100 100 100 100 100 100
100 100 100 100 100 100 100 100 100 100
100 100 100 100 100 100 100 100 100 100
100 100 100 100 100 100 100 100 100 100
1 1 3
5 5 2
'''
