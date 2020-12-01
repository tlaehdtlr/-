# N개 재료 절반씩, A, B 맛의 차이 최소
# 재료 조합 시너지!
# 음식맛의 차이 최솟값 찾기
def combi_ingre(nums_choice, next_idx):
    global ans, N, A_ingre
    if nums_choice == N//2:
        sum_A = cal_synergy(A_ingre)

        B_ingre = [False]*N
        for q in range(N):
            if not A_ingre[q]:
                B_ingre[q] = True
        sum_B = cal_synergy(B_ingre)
        ans = min(ans, abs(sum_A - sum_B))
        return

    for i in range(next_idx, N):
        A_ingre[i] = True
        combi_ingre(nums_choice + 1, i+1)
        A_ingre[i] = False


def cal_synergy(choice):
    global N, synergy
    sum_synergy = 0
    for i in range(N):
        if choice[i]:
            for j in range(N):
                if choice[j]:
                    sum_synergy += synergy[i][j]
    return sum_synergy


if __name__ == '__main__':
    T = int(input())
    for tc in range(1,1+T):
        N = int(input())
        synergy = [0]*N
        for i in range(N):
            synergy[i] = list(map(int, input().split()))
        ans = 99999
        A_ingre = [False]* N
        A_ingre[0] = True
        combi_ingre(1, 1)
        print('#{} {}'.format(tc, ans))