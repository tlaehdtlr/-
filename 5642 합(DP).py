T = int(input())
for tc in range(1,1+T):
    N = int(input())
    nums = list(map(int, input().split()))

    nums_sum = nums[:]
    for i in range(1,N):
        if nums_sum[i-1] > 0:
            nums_sum[i] += nums_sum[i-1]
    ans = max(nums_sum)
    print('#{} {}'.format(tc, ans))