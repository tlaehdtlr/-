def rotate(face, direc):
    global U, D, F, B, L, R
    # U - D 은 비슷한 뒤집힌 관계임 나머지도임
    # U, F, L를 기준으로 만든다
    if face == 'U':
        if direc == '+':
            num = 1
        else:
            num = 3
        for _ in range(num):
            # 시계
            U = move(U, F[0], 0, 0, 0, R[0], 0, 0,
                     0, B[0], 0, 0, 0, L[0], 0, 0, 0)

        # 반시계인데 이거 버리자
        # U = [i for i in list(map(list, zip(*U)))[::-1]]
    elif face == 'D':
        if direc == '+':
            num = 3
        else:
            num = 1
        for _ in range(num):
            D = move(D, F, 2, R, 2, B, 0, L, 0)


def move(f, a, a1, a2, a3, b, b1, b2, b3, c, c1, c2, c3, d, d1, d2, d3):
    global U, D, F, B, L, R
    f = [list(reversed(i)) for i in list(map(list, zip(*f)))]
    temp = a[a1], a[a2], a[a3]
    a[a1], a[a2], a[a3] = b[b1], b[b2], b[b3]
    b[b1], b[b2], b[b3] = c[c1], c[c2], c[c3]
    c[c1], c[c2], c[c3] = d[d1], d[d2], d[d3]
    d[d1], d[d2], d[d3] = temp
    print()
    for i in range(3):
        print(a[i])
    return f


T = int(input())
for _ in range(T):
    N = int(input())
    commands = list(map(str, input().split()))

    # U의 0,0을  0,0,0 꼭짓점으로 잡자
    # 초기 / 윗면 w / 아랫면 y / 앞면 r / 뒷면 o / 왼쪽 g / 오른 b /
    U = [['w']*3 for _ in range(3)]
    U[0][0] = 'y'
    U[1][2] = 'r'
    D = [['y']*3 for _ in range(3)]
    D[0][0] = 'g'
    D[1][2] = 'r'
    F = [['r']*3 for _ in range(3)]
    F[0][1] = 1
    F[2][0] = 2
    B = [['b']*3 for _ in range(3)]
    L = [['g']*3 for _ in range(3)]
    L[0][1] = 3
    L[2][0] = 4
    R = [['b']*3 for _ in range(3)]

    for i in range(3):
        print(U[i])
    print('변화')
    for command in commands:
        rotate(command[0], command[1])
    for i in range(3):
        print(U[i])
    print('F')
    for i in range(3):
        print(F[i])
    print('R')
    for i in range(3):
        print(L[i])
