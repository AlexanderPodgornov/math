# метод подходит для квадратных матриц, так как в методе используется разложение A = L + D + U, где диагональ не нулевая
# а также должно быть диагональное преобладание (A[i][i] больше суммы модулей элементов в строке)
import copy
import math

# A = [[10, 1, -1],
#      [1, 10, -1],
#      [-1, 1, 10]]
#
# B = [11, 10, 10]
A = [[4, -1, 1],
     [-1, 5, -1],
     [1, -1, -5]]
B = [3, 2, 6]

n = len(B)
x = [0] * n
new_x = [0] * n
t = 0
while True:
    t = t + 1
    x = new_x.copy()
    for k in range(n):
        summ = 0
        for i in range(n):
            if i < k:
                summ = summ + A[k][i] * new_x[i]
            elif i > k:
                summ = summ + A[k][i] * x[i]
        new_x[k] = (B[k] / A[k][k]) - (1 / A[k][k]) * summ
    # print(f'iter = {t} {new_x} - обновленный вектор, {x} - прежний вектор')
    arr = []
    for k in range(n):
        arr.append(abs(new_x[k] - x[k]))
    # if max(arr) < 0.0001:
    #     print(t, "итераций")
    #     break
    if max(arr) < 0.001:
        print(t, "итераций")
        break
    # print("delta = ", max(arr))
    # print('==========')

print("ОТВЕТ: ", new_x)
