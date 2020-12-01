N = int(input())
tri = [[] for _ in range(N)]
for i in range(N):
    tri[i] = list(map(int, input().split()))

for layer in range(1, N):
    for idx in range(len(tri[layer])):
        if idx == 0:
            tri[layer][0] += tri[layer-1][0]
        elif idx == len(tri[layer])-1:
            tri[layer][idx] += tri[layer-1][idx-1]
        else:
            tri[layer][idx] += max(tri[layer-1][idx-1], tri[layer-1][idx])

print(max(tri[-1]))
