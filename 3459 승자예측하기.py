

for tc in range(1, 1+int(input())):
    N = int(input())
    A = {1}
    ans = ''
    # print('@@@@@@@@@@@@@@@@@@@@')
    for _ in range(60):
        # print('-----------------')
        B = set()
        possible_A = False
        for num in A:
            if 2*num > N:
                possible_A = True
            B.add(2*num)
            B.add(2*num+1)
        if possible_A:
            for b in B:
                if b <= N:
                    possible_A = False
                    break
        # print('A턴 끝')
        # print(A)
        # print(B)
        if possible_A:
            ans = 'Bob'
            break

        A = set()
        possible_B = False
        for num in B:
            if 2*num > N:
                possible_B = True
            A.add(2*num)
            A.add(2*num+1)
        if possible_B:
            for a in A:
                if a <= N:
                    possible_B = False
                    break
        # print('B턴 끝')
        # print(A)
        # print(B)
        if possible_B:
            ans = 'Alice'
            break
    print('#', tc, ans)
