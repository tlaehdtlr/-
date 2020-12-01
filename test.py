# LIS 만들기
def create_LIS(r, c, pre, candi=[]):
    if pre == 1:
        candi += [A[r]]
        candi.reverse()
        LIS.append(candi)
    for nc in range(1, c+1):
        if dp[c][nc] == pre-1:
            create_LIS(c, nc, pre-1, candi+[A[r]])


N, K = map(int, input().split())
A = [0] + list(map(int, input().split()))

dp = [[0]*(N+1) for _ in range(N+1)]
longest = 1

for i in range(1, N+1):
    max_i = 1
    for j in range(1, i+1):
        if i == j:
            dp[i][j] = 1

        elif A[i] > A[j]:
            candi_long = dp[j][0] + 1
            dp[i][j] = candi_long
            if max_i < candi_long:
                max_i = candi_long

    dp[i][0] = max_i
    if longest < max_i:
        longest = max_i

LIS = []
for r in range(1, N+1):
    for c in range(1, N+1):
        if dp[r][c] == longest:
            create_LIS(r, c, longest)

if len(LIS) < K:
    print(-1)
else:
    LIS.sort(key=lambda x: tuple(x[i] for i in range(longest)))
    for a in LIS[K-1]:
        print(str(a), end=' ')
