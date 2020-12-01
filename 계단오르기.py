import sys
input = sys.stdin.readline

N = int(input())
points = [0]*(N+1)
for i in range(1, 1+N):
    points[i] = int(input())
if N < 3:
    print(sum(points))
else:
    stairs = [[0, 0] for _ in range(N+1)]
    stairs[1] = [0, points[1]]
    stairs[2] = [points[2], points[1]+points[2]]
    for num in range(3, N+1):
        stairs[num] = [max(stairs[num-2])+points[num],
                       stairs[num-1][0]+points[num]]

    print(max(stairs[-1]))
