# https://www.acmicpc.net/problem/2630

import sys
input = sys.stdin.readline

def make_paper(sr,sc,er,ec):
    if sr == er:
        return paper[sr][sc]

    mr = (sr+er)//2
    mc = (sc+ec)//2

    fir = make_paper(sr,sc,mr,mc)
    sec = make_paper(sr,mc+1,mr,ec)
    thir = make_paper(mr+1,sc,er,mc)
    four = make_paper(mr+1,mc+1,er,ec)
    if fir==sec==thir==four:
        return fir
    else:
        for color in fir,sec,thir,four:
            if color != None:
                color_wb[color]+=1
        return None


N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
color_wb = [0,0]
one = make_paper(0,0,N-1,N-1)

if one != None:
    color_wb[one]+=1
print(color_wb[0])
print(color_wb[1])