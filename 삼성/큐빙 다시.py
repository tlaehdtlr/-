# 이건 그냥 노가다임
# 시계 반시계는 시계 3번 돌리는걸로 하자

# 그냥 안할래 도라이인가

face_U = [['w']*3 for _ in range(3)]
face_D = [['y']*3 for _ in range(3)]
face_F = [['r']*3 for _ in range(3)]
face_B = [['o']*3 for _ in range(3)]
face_L = [['g']*3 for _ in range(3)]
face_R = [['b']*3 for _ in range(3)]

def rotate_U():
    new_U = [[0]*3 for _ in range(3)]
    new_U[0][0], new_U[0][1], new_U[0][2] = face_U[2][0], face_U[1][0], face_U[0][0]
    new_U[2][0], new_U[1][0], new_U[0][0] = face_U[2][2], face_U[2][1], face_U[2][0]
    new_U[2][2], new_U[2][1], new_U[2][0] = face_U[0][2], face_U[1][2], face_U[2][2]
    new_U[0][2], new_U[1][2], new_U[2][2] = face_U[0][0], face_U[0][1], face_U[0][2]
    new_U[1][1] = face_U[1][1]
    for i in range(3):
        face_U[i] = new_U[i][:]
    # 12시부터 시계방향
    new_B = face_L[0][:]
    new_L = face_F[0][:]
    new_F = face_R[0][:]
    new_R = face_B[0][:]
    face_B[0] = new_B[:]
    face_L[0] = new_L[:]
    face_F[0] = new_F[:]
    face_R[0] = new_R[:]
face_U[0][2] = 99
face_U[1][2] = 88
rotate_U()
print('U')
for q in range(3):
    print(face_U[q])

print('B')
for q in range(3):
    print(face_B[q])

print('R')
for q in range(3):
    print(face_R[q])

print('F')
for q in range(3):
    print(face_F[q])

print('L')
for q in range(3):
    print(face_L[q])


print('U')
for q in range(3):
    print(face_U[q])
