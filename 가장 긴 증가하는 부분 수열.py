N = int(input())
A = list(map(int, input().split()))
array = [1]*N
for i in range(1, N):
    for j in range(0, i):
        if A[i] > A[j] and array[i] < array[j]+1:
            array[i] = array[j]+1
print(max(array))
