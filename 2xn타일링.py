n = int(input())
if n < 3:
    tile = [0, 1, 2]
    print(tile[n] % 10007)
else:
    tile = [0]*(n+1)
    tile[1], tile[2] = 1, 2
    for i in range(3, n+1):
        tile[i] += tile[i-1] + tile[i-2]
    print(tile[n] % 10007)
