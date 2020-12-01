T=int(input())
for tc in range(1,1+T):
    N = int(input())

    nums_str = ''

    while len(nums_str) != N:
        nums_str += ''.join(map(str, input().split()))

    ## 정수 0부터 가능한지 체크
    ans = '-1'
    while True:
        ans = str(int(ans) + 1)
        len_ans = len(ans)
        success = False
        for idx in range(0,N-len_ans+1):
            if ans == nums_str[idx:idx+len_ans]:
                success=True
                break
        if not success:
            break

    print('#{} {}'.format(tc, int(ans)))