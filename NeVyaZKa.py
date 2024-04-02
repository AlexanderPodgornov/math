import numpy as np

# A = N*N

A = np.array([[2.5, -0.9, 0.2],
              [-0.9, 3.8, -0.1],
              [0.2, -0.1, 0.9]])
B = np.array([-0.7, 2.5, 0.1])
# A = np.array([[4, -1, 1],
#               [-1, 5, -1],
#               [1, -1, -5]])
# B = np.array([3, 2, 6])
x = [0] * len(B)
r = np.dot(A, x) - B
t = 0
print(np.linalg.norm(r))
while np.linalg.norm(r) > 0.001:
    tay = np.dot(np.dot(A, r), r) / np.dot(np.dot(A, r), np.dot(A, r))
    #print(tay, "tayв")
    x = x - np.dot(tay, r)
    r = np.dot(A, x) - B
    t = t + 1
    #print(x)
print(x)
print(t)
#while
