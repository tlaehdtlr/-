def bi_section(val):
    left, right = 0, len(arr)
    while left <= right:
        middle = (left+right)//2
        if arr[middle] < val:
            left = middle+1
        else:
            right = middle-1
    return left


N = int(input())
A = list(map(int, input().split()))
arr = [A[0]]
for i in range(1, N):
    if arr[-1] < A[i]:
        arr.append(A[i])
    else:
        idx = bi_section(A[i])
        arr[idx] = A[i]
print(len(arr))
