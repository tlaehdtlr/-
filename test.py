# https://www.acmicpc.net/problem/10815

N = int(input())
N_card = list(map(int, input().split()))
M = int(input())
M_card = list(map(int, input().split()))

def search(num, l,r):
    while l<=r:
        m = (l+r)//2
        if num == N_card[m]:
            return 1
        elif num < N_card[m]:
            r = m - 1
        else:
            l = m + 1
    return 0


N_card.sort()
for M_num in M_card:
    print(search(M_num,0,len(N_card)-1), end=' ')
print()