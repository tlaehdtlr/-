def sum_sequence(K, N, cur_sum, subset, cur_idx):
    global ans
    if cur_sum > K: return
    if cur_sum == K:
        ans += 1
        return
    for i in range(cur_idx, N):
        if subset & (1<<i): continue
        sum_sequence(K, N, cur_sum + A[i], subset|(1<<i), i)

T = int(input())
for tc in range(1,T+1):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    sum_sequence(K, N, 0, 0, 0)
    print('#{} {}'.format(tc, ans))