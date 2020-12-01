import sys
input = sys.stdin.readline

N = int(input())
# RGB
houses_RGB = [list(map(int, input().split())) for _ in range(N)]
for house_num in range(1, N):
    r, g, b = houses_RGB[house_num]
    r += min(houses_RGB[house_num-1][1], houses_RGB[house_num-1][2])
    g += min(houses_RGB[house_num-1][0], houses_RGB[house_num-1][2])
    b += min(houses_RGB[house_num-1][0], houses_RGB[house_num-1][1])
    houses_RGB[house_num] = [r, g, b]
print(min(houses_RGB[-1]))
