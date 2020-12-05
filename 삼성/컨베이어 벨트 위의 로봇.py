import time as aaa

def solve():
    # 컨베길이, 종료 칸
    N, K = map(int, input().split())

    st = aaa.time()

    A = list(map(int, input().split()))
    robot = [False] * 2 * N
    NN = 2 * N
    broken = 0
    time = 0
    while True:
        time+=1
        ## 1
        A = [A[-1]] + A[:NN - 1]
        robot = [robot[-1]] + robot[:NN - 1]
        robot[N-1] = False

        #2
        for idx in range(N - 2, -1, -1):
            if robot[idx] and not robot[idx + 1] and A[idx+1]:
                A[idx+1] -= 1
                if not A[idx+1]:
                    broken+=1
                robot[idx + 1] = robot[idx]
                robot[idx] = False
        robot[N - 1] = False

        #3
        if not robot[0] and A[0]:
            robot[0] = True
            A[0] -= 1
            if not A[0]:
                broken += 1
        # print(time)
        # print('로봇', robot)
        # print('내구', A)
        if broken>=K:
            print('시간:', aaa.time()-st)
            # print(robot)
            # print(A)
            return time

print(solve())
