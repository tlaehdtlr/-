import sys
input = sys.stdin.readline

N = int(input())

cur_max, cur_2, cur_1 = 0, 0, 0
for _ in range(N):
    wine = int(input())
    cur_max, cur_2, cur_1 = max(
        cur_max, cur_2, cur_1), cur_max + wine, cur_2 + wine
print(max(cur_max, cur_2, cur_1))
