
# метод прогонки подходит для трехдиагональной матрицы

diag_up = [-1, -1, 2, -4, 0]  # c

diag_center = [2, 8, 12, 18, 10]  # b

diag_down = [0, -3, -5, -6, -5]  # a

B = [-25, 72, -69, -156, 20]  # d

for i in range(len(diag_center)):
    diag_center[i] *= -1

p = [0, diag_up[0] / diag_center[0]]  # p1
q = [0, -B[0] / diag_center[0]]  # q1

for i in range(2, len(B)):
    p.append(diag_up[i - 1] / (diag_center[i - 1] - diag_down[i - 1] * p[i - 1]))
    q.append((diag_down[i - 1] * q[i - 1] - B[i - 1]) / (diag_center[i - 1] - diag_down[i - 1] * p[i - 1]))

# print(p)
# print(q)
u = [0] * len(B)
u[len(B) - 1] = round((B[-1] - diag_down[-1] * q[-1]) / (diag_down[-1] * p[-1] - diag_center[-1]))

for i in range(len(B)-1, 0, -1):
    u[i-1] = round(p[i] * u[i] + q[i])

print("ОТВЕТ:", u)