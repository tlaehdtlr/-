def div_con(L, R):
    if L == R:
        return A[L]

    mid = (L + R)//2

    left = div_con(L, mid)
    right = div_con(mid+1, R)

    left_sum = left*min(A[L:mid+1])
    right_sum = right*min(A[mid+1:R+1])

    cur = (left+right)*min(A[L:R+1])
    print(L, R, cur)
    return max(left_sum, right_sum, cur)
    # return max([left_sum, L, mid+1], [right_sum, mid+1, R], [
    #     cur, L, R], key=lambda lst: lst[0])


N = int(input())
A = list(map(int, input().split()))
# ans_sum, ans_l, ans_r = div_con(0, N-1)
ans = div_con(0, N-1)
print(ans)
# print(A[ans_l:ans_r+1])
