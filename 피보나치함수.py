T = int(input())
for _ in range(T):
    N = int(input())
    if N == 0:
        print(1, 0, end=' ')
    elif N == 1:
        print(0, 1, end=' ')
    else:
        nums = [[0, 0] for _ in range(N+1)]
        nums[0][0] = 1
        nums[1][1] = 1
        for num in range(2, N+1):
            nums[num][0] = nums[num-2][0] + nums[num-1][0]
            nums[num][1] = nums[num-2][1] + nums[num-1][1]
        # print(nums)
        print(nums[N][0], nums[N][1], end=' ')
    print()
