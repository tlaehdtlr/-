import sys
input = sys.stdin.readline

N = int(input())
wines = []
for _ in range(N):
    wines.append(int(input()))

if N < 3:
    print(sum(wines))
else:
    # 전전, 전 (전전+전 제외), 안마시는 경우도 추가...
    ans = [0]*N
    ans[0] = (wines[0], wines[0], 0)
    ans[1] = (wines[1], wines[0]+wines[1], wines[0])
    max_ans = ans[1][1]
    for idx in range(2, N):
        ans[idx] = (max(ans[idx-2]) + wines[idx], max(ans[idx-1][0], ans[idx-1][2]) +
                    wines[idx], max(max(ans[idx-2]), max(ans[idx-1])))
        max_ans = max(max_ans, max(ans[idx]))
    # print(wines)
    # print(ans)
    print(max_ans)
