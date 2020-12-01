T=int(input())
for tc in range(1,1+T):
    S = str(input())
    card = dict()
    ans = True
    for i in ['S','D','H','C']:
        card[i] = set(range(1,14))
    for j in range(0,len(S),3):
        t,x,y = S[j], int(S[j+1]), int(S[j+2])
        if x*10+y in card[t]: card[t].discard(x*10+y)
        else:
            ans = False
            break
    if ans:
        print('#{} {} {} {} {}'.format(tc, len(card['S']), len(card['D']), len(card['H']), len(card['C'])))
    else:
        print('#{} {}'.format(tc, 'ERROR'))
