def creation(N, cur, add_num, order, len_N):
    global ans
    if ans: return
    if order == -1:
        if cur + add_num == N:
            ans = cur
        return

    check = cur+add_num
    for num in range(order+1):
        check += 9*(10**num) +9
    if check < N:
        return

    max_num = 9
    if order == len_N-1: max_num = N//(10**order)
    for i in range(max_num+1):
        creation(N, cur + i*(10**order), add_num+i, order-1, len_N)


if __name__ == '__main__':
    N = int(input())
    ans = 0
    len_N = len(str(N))
    creation(N, 0, 0, len_N-1, len_N)
    print(ans)