import sys
sys.stdin = open('./삼성/test.txt', 'r')
input = sys.stdin.readline

N = int(input())
rooms = list(map(int, input().split()))
# 총, 부
B, C = map(int, input().split())
ans = N
for num in rooms:
    num -= B
    if num < 1:
        continue
    ans += num//C
    if num % C:
        ans += 1
print(ans)
