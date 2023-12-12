import numpy as np


A = [[0, 2],
     [1, 0]
]

B = [-2, 0]

C = [[1, -2],
     [1, 0]
]

V = np.dot(A,B,)
print("V = ",V)

D = np.dot(A,C)
print("D =",D)


print(np.array(B).T)
print(np.array(B))

a = np.arange(100)
print("a = ",a)
a.reshape(5,5,4)
print("a = ",a)

a = np.random.randint(3, size=(2, 2))
print("a= \n",a, end="\n")

b = np.random.randint(5, size=(2, 4))
print("b= \n",b, end="\n")

z = np.dot(a,b)
print("z= \n",z, end="\n")

d = np.eye(3)
print("d= \n",d, end="\n")

d = np.eye(3, 5)
print("d= \n",d, end="\n")
# a = np.arange(3*4*5*6).reshape((3,4,5,6))
# print("a = ",a)
# b = np.arange(3*4*5*6)[::-1].reshape((5,4,6,3))
# print("b = ",b)
# np.dot(a, b)[2,3,2,1,2,2]

