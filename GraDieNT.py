import numpy as np

# A = N*N симметричная положительно определенная матрица (выполняется не более, чем за N итераций)
A = np.array([[2.5, -0.9, 0.2],
              [-0.9, 3.8, -0.1],
              [0.2, -0.1, 0.9]])
B = np.array([-0.7, 2.5, 0.1])

# A = np.array([[4, -1, 1],
#               [-1, 5, -1],
#               [1, -1, -5]])
# B = np.array([3, 2, 6])
x = [0] * len(B)
r = np.array(B - np.dot(A, x))

k = r
t = 0

print(np.linalg.norm(r))
while np.linalg.norm(r) > 0.001:
    t = t + 1
    alpha = np.dot(r, r) / np.dot(np.dot(A, k), k)
    x = x - np.dot(alpha, k)
    r_old = r
    r = r - np.dot(np.dot(alpha, A), k)
    beta = np.dot(r, r) / np.dot(r_old, r_old)
    k = r + np.dot(beta, k)
    #print(x)
print(x)
print(t)
#while
