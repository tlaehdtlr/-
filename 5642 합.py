T = int(input())
for tc in range(1,1+T):
    N = int(input())
    nums = list(map(int, input().split()))
    new_nums = [nums[0]]
    # 전부 -인 경우 있는 경우 고려하자
    nums_minus = []
    if nums[0] < 0:
        nums_minus.append(nums[0])
    for num in nums[1:]:
        if num < 0: nums_minus.append(num)
        if num*new_nums[-1] >= 0:
            new_nums[-1] = num + new_nums[-1]
        else:
            new_nums.append(num)
    if nums_minus:
        ans = max(nums_minus)
    else:
        ans = 0
    new_N = len(new_nums)
    idx = 0
    cur = 0
    while idx < new_N:
        if cur + new_nums[idx] >= 0:
            cur += new_nums[idx]
            ans = max(ans, cur)
        else:
            cur = 0
        idx += 1

    print('#{} {}'.format(tc, ans))