# метод Холецкого или метод квадратного корня для симметрической квадратной матрицы, когда матрица положительно
# определенная, то есть ++ ... + определители положительные
from math import sqrt

A = [[2, 1, 4],
     [1, 1, 3],
     [4, 3, 14]]

B = [16, 12, 52]
# A = [[4, 5, 6],
#      [5, 9, 2],
#      [6, 2, 100]]
#
# B = [10, 20, 30]

n = len(B)
u = [[0 for j in range(n)] for i in range(n)]

# u[0][0] = sqrt(A[0][0])
# for i in range(1, n):
#     u[i][0] = A[0][i] / u[0][0]
# print(u)

for i in range(n):  # от 1 до n-1 в питоне, в математике от 2 до n
    summ = 0
    for k in range(i):
        #print(f'u[k][i] == {u[k][i]}')
        summ = summ + pow(u[k][i], 2)
    # print('==')
    # print(u)
    # print(f"sqrt({A[i][i]} - {summ}) == {sqrt(A[i][i] - summ)}")
    # print("A[i][i] ==", A[i][i], "   summ ==", summ, "   A[i][i] - summ ==", A[i][i] - summ)
    # print('=======================')
    # print('=====', "summ", summ, "sqrt(x)", A[i][i] - summ)
    u[i][i] = sqrt(A[i][i] - summ)

    for j in range(1, n):
        if j > i:
            summ = 0
            for k in range(i):
                summ = summ + u[k][i] * u[k][j]
            u[i][j] = (1 / u[i][i]) * (A[i][j] - summ)
        elif j < i:
            u[i][j] = 0
# ранее верно находит u

ut = [[u[i][j] for j in range(n)] for i in range(n)]
for i in range(n):
    for j in range(i):
        ut[i][j], ut[j][i] = ut[j][i], ut[i][j]
# далее ut - транспонированная

# for (int i = 2 - 1; i >= 0; i = i - 1) {
#     X[i] = B[i] / A[i][i];
#     for (int c = i - 1; c >= 0; c = c - 1) {
#         B[c] = B[c] - A[c][i] * X[i];
#     }
# }


# обратный ход
y = [0] * n
for i in range(n):
    y[i] = B[i] / ut[i][i]
    for c in range(1, n):
        B[c] = B[c] - ut[c][i] * y[i]
#print(f'y = {y}')

x = [0] * n
for i in range(n-1, -1, -1):
    x[i] = y[i] / u[i][i]
    for c in range(i-1, -1, -1):
        y[c] = y[c] - u[c][i] * x[i]
print(f'ОТВЕТ = {x}')

# print(u)
# print("===")
# print(ut)



print(A)
ans = []
for i in range(n):
    summ = 0
    for j in range(n):
        summ = summ + A[i][j] * x[j]
    ans.append(summ)

print(ans)
