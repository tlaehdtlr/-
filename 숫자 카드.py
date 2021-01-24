# https://www.acmicpc.net/problem/10815

N = int(input())
N_card = list(map(int, input().split()))
M = int(input())
M_card = list(map(int, input().split()))

def sort_card(ldx,rdx):
    if ldx==rdx-1:
        return [N_card[ldx]]

    mdx = (ldx+rdx)//2
    l = sort_card(ldx,mdx)
    r = sort_card(mdx,rdx)

    merge = []
    mer_l = mer_r = 0
    l_len = len(l)
    r_len = len(r)
    while mer_l < l_len and mer_r < r_len:
        if l[mer_l] > r[mer_r]:
            merge.append(r[mer_r])
            mer_r += 1
        else:
            merge.append(l[mer_l])
            mer_l += 1

    if mer_l == l_len:
        merge += r[mer_r:r_len]
    else:
        merge += l[mer_l:l_len]

    return merge


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


N_card = sort_card(0,len(N_card))
for M_num in M_card:
    print(search(M_num,0,len(N_card)-1), end= ' ')
print()