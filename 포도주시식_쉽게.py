import sys
input = sys.stdin.readline

N = int(input())
wines = []
for _ in range(N):
    wines.append(int(input()))

dp = [0]*N
if N < 3:
    print(sum(wines))
else:
    dp[0] = wines[0]
    dp[1] = wines[0] + wines[1]
    for idx in range(2, N):
        # 전에꺼 안마시는 경우, 전전꺼 안마시는 경우
        dp[idx] = max(dp[idx-2], dp[idx-3]+wines[idx-1])+wines[idx]
        # 이전 2개를 연속으로 마시는게(연속 안 마셨을 수도 있긴함) 이득인지 확인
        dp[idx] = max(dp[idx-1], dp[idx])

    print(max(dp))
