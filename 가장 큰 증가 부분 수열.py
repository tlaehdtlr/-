def bi_section(val):
    L, R = 0, len(arr)-1
    while L <= R:
        M = (L+R)//2
        if arr[M] < val:
            L = M+1
        # 같으면 L은 가만있어야지
        else:
            R = M-1
    return L


N = int(input())
A = list(map(int, input().split()))
arr = [A[0]]
abandon = [[]]
ans = 0
for i in range(1, N):
    if arr[-1] < A[i]:
        arr.append(A[i])
        abandon.append([])
    else:
        idx = bi_section(A[i])
        abandon[idx].append(arr[idx])
        arr[idx] = A[i]
    ans = max(ans, sum(arr))
print(abandon)
print(arr)
print(ans)
