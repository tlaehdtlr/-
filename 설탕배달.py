N = int(input())
candi = [-1]*5001
candi[0] = 0

for i in range(N+1):
    if i+5 < 5001 and candi[i] > -1:
        if candi[i+5] < 0:
            candi[i+5] = candi[i]+1
        elif candi[i+5] > candi[i] + 1:
            candi[i+5] = candi[i]+1
    if i+3 < 5001 and candi[i] > -1:
        if candi[i+3] < 0:
            candi[i+3] = candi[i]+1
        elif candi[i+3] > candi[i] + 1:
            candi[i+3] = candi[i]+1
print(candi[N])
