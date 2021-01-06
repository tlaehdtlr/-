# https://www.acmicpc.net/problem/1780

import sys
input = sys.stdin.readline

def cut(sr,sc,er,ec):
    if sr == er-1:
        if paper[sr][sc] == -1:
            return (1,0,0)
        if paper[sr][sc] == 0:
            return (0,1,0)
        if paper[sr][sc] == 1:
            return (0,0,1)
    dist = (er-sr)//3
    mr1 = sr+dist
    mr2 = mr1+dist
    mc1 = sc+dist
    mc2 = mc1+dist
    minus = zero = plus = 0
    sq = []
    sq.append(cut(sr,sc,mr1,mc1))
    sq.append(cut(sr,mc1,mr1,mc2))
    sq.append(cut(sr,mc2,mr1,ec))
    sq.append(cut(mr1,sc,mr2,mc1))
    sq.append(cut(mr1,mc1,mr2,mc2))
    sq.append(cut(mr1,mc2,mr2,ec))
    sq.append(cut(mr2,sc,er,mc1))
    sq.append(cut(mr2,mc1,er,mc2))
    sq.append(cut(mr2,mc2,er,ec))

    for m,z,p in sq:
        minus += m
        zero += z
        plus += p
    if zero == plus == 0:
        return (1,0,0)
    elif minus == plus ==0:
        return (0,1,0)
    elif minus == zero ==0:
        return (0,0,1)
    else:
        return (minus,zero,plus)


N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
ans = cut(0,0,N,N)
print(ans[0])
print(ans[1])
print(ans[2])