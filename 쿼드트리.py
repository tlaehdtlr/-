def div_con(sr, sc, er, ec):
    if sr == er and sc == ec:
        return video[sr][sc]

    mr, mc = (sr+er)//2, (sc+ec)//2

    one = div_con(sr, sc, mr, mc)
    two = div_con(sr, mc+1, mr, ec)
    three = div_con(mr+1, sc, er, mc)
    four = div_con(mr+1, mc+1, er, ec)
    if one == two == three == four == '0' or one == two == three == four == '1':
        if len(one) == 1:
            return one
        return '('+one+')'
    return '('+one+two+three+four+')'


N = int(input())
video = [list(input()) for _ in range(N)]
print(div_con(0, 0, N-1, N-1))
