import time


class Node:
    def __init__(self, num):
        self.num = num
        self.head = None
        self.tail = []
        # self.cnt = 1

    # head한테 푸쉬함
    def push(self, Tail):
        self.tail.append(Tail)
        # self.cnt += Tail.cnt
        Tail.head = True

    def find(self):
        if not self.tail:
            cnt += 1
            if cnt == K:
                pass
        return


N, K = map(int, input().split())
A = [0] + list(map(int, input().split()))

start = time.time()

dp = [[0]*(N+1) for _ in range(N+1)]
longest = 1

# 루트 역할
root = Node(0)
nodes = [root] + [0]*N
for a in range(1, N+1):
    nodes[a] = Node(A[a])

for i in range(N, 0, -1):
    max_i = 1
    for j in range(i, N+1):
        if i == j:
            dp[i][j] = 1

        elif A[i] < A[j]:
            candi_long = dp[j][0] + 1
            dp[i][j] = candi_long
            if max_i < candi_long:
                max_i = candi_long

    for k in range(i, N+1):
        if dp[i][k] == max_i:
            nodes[i].push(nodes[k])

    dp[i][0] = max_i
    if longest < max_i:
        longest = max_i

for node in range(1, N+1):
    if nodes[node].tail:
        nodes[node].tail.sort(key=lambda NODE: NODE.num)
    if nodes[node].head:
        continue

# 첫번째 놈들 찾고 정렬
st = []
cnt = 0
for node in range(1, N+1):

    if nodes[node].head:
        continue
    # 긴 놈 찾기
    if nodes.


for r in range(1, N+1):
    for c in range(1, N+1):
        if dp[r][c] == longest:
            create_LIS(r, c, longest)
if len(LIS) < K:
    print(-1)
else:
    # LIS.sort(key=lambda x: tuple(x[i] for i in range(len(x))))
    # LIS.sort(key=lambda x: tuple(x[i] for i in range(longest)))
    for a in LIS[K-1]:
        print(str(a), end=' ')

end = time.time()
# for q in LIS:
#     print(q)
print()
print('---------------')
print(len(LIS))
print('소요시간 : ', end-start)
