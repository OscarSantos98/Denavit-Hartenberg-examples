import numpy as np
import sympy as sp
from sympy import sin, cos, nsimplify
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from tabulate import tabulate

# Symbolic
a10, a11, a12, a13, a1, a2, a3, a4 = sp.symbols('a10 a11 a12 a13 a1 a2 a3 a4')
th1, th2, th3, th4, d1, d2, d3, d4 = sp.symbols('th1 th2 th3 th4 d1 d2 d3 d4')
L1, L2, L3, L4 = sp.symbols('L1 L2 L3 L4')
a1_v = sp.Matrix([a10, a11, a12, a13])
a_v = sp.Matrix([a1, a2, a3, a4])
th_v = sp.Matrix([th1, th2, th3, th4])
d_v = sp.Matrix([d1, d2, d3, d4])

# 1
data = [
    [1, 0, 'a1', 0, chr(952) + '1'],
    [2, np.pi / 2, 0, 'd2', 0],
    [3, 0, 0, 'L3', np.pi / 2],
    [4, '-'+chr(952) + '3', 0, 'a4', 0]
]
data2 = [
    [1, 0, 5, 0, th1],
    [2, np.pi / 2, 0, d2, 0],
    [3, 0, 0, 10, np.pi / 2],
    [4, -th3, 0, 4, 0]
]
data3 = [
    [1, 0, 5, 0, 30 * np.pi / 180],
    [2, np.pi / 2, 0, 10, 0],
    [3, 0, 0, 10, np.pi / 2],
    [4, -45 * np.pi / 180, 0, 4, 0]
]
xmin=-3
xmax=18
ymin=-22
ymax=2
zmin=-2
zmax=2

# # 2
# data = [
#     [1, 0, 0, 'd2', chr(952) + '1'],
#     [2, '-' + chr(952) + '2', 0, 'a2', - np.pi / 2],
#     [3, 0, 'd3', 0, 0],
#     [4, 0, 'a3', 0, 0]
# ]
# data2 = [
#     [1, 0, 0, 10, th1],
#     [2, -th2, 0, 3, - np.pi / 2],
#     [3, 0, d3, 0, 0],
#     [4, 0, 4, 0, 0]
# ]
# data3 = [
#     [1, 0, 0, 10, 30 * np.pi / 180],
#     [2, -45 * np.pi / 180, 0, 3, - np.pi / 2],
#     [3, 0, 10, 0, 0],
#     [4, 0, 4, 0, 0]
# ]
# xmin = -4
# xmax = 10
# ymin = -10
# ymax = 5
# zmin = -2
# zmax = 24

# # 3
# data = [
#     [1, 0, 0, 'd2', chr(952) + '1'],
#     [2, '-'+chr(952) + '2', 0, 'a2', 0],
#     [3, '-'+chr(952) + '3', 0, 'a3', 0],
#     [4, 0, 0, 0, 0]
# ]
# data2 = [
#     [1, 0, 0, 10, th1],
#     [2, -th2, 0, 8, 0],
#     [3, -th3, 0, 5, 0],
#     [4, 0, 0, 0, 0]
# ]
# data3 = [
#     [1, 0, 0, 10, 30 * np.pi / 180],
#     [2, -45 * np.pi / 180, 0, 8, 0],
#     [3, -45 * np.pi / 180, 0, 5, 0],
#     [4, 0, 0, 0, 0]
# ]
# xmin = -8
# xmax = 8
# ymin = -1
# ymax = 11
# zmin = -1
# zmax = 19

print(tabulate(data, headers=['Eslabón', chr(
    945) + 'i-1', 'ai-1', 'di', chr(952) + 'i']))
print()

# Symbolic
a1_s = a1_v.subs([(a13, data[3][1]), (a12, data[2][1]), (a11, data[1][1]), (a10, data[0][1])])
a_s = a_v.subs([(a4, data[3][2]), (a3, data[2][2]), (a2, data[1][2]), (a1, data[0][2])])
d_s = d_v.subs([(d4, data[3][3]), (d3, data[2][3]), (d2, data[1][3]), (d1, data[0][3])])
th_s = th_v.subs([(th4, data[3][4]), (th3, data[2][4]), (th2, data[1][4]), (th1, data[0][4])])
# Numeric and symbolic
a1_ns = a1_v.subs([(a10, data2[0][1]), (a11, data2[1][1]), (a12, data2[2][1]), (a13, data2[3][1])])
a_ns = a_v.subs([(a1, data2[0][2]), (a2, data2[1][2]), (a3, data2[2][2]), (a4, data2[3][2])])
d_ns = d_v.subs([(d1, data2[0][3]), (d2, data2[1][3]), (d3, data2[2][3]), (d4, data2[3][3])])
th_ns = th_v.subs([(th1, data2[0][4]), (th2, data2[1][4]), (th3, data2[2][4]), (th4, data2[3][4])])

# Numeric for the plot
a1_n = a1_v.subs([(a10, data3[0][1]), (a11, data3[1][1]),
                  (a12, data3[2][1]), (a13, data3[3][1])])
a_n = a_v.subs([(a1, data3[0][2]), (a2, data3[1][2]),
                (a3, data3[2][2]), (a4, data3[3][2])])
d_n = d_v.subs([(d1, data3[0][3]), (d2, data3[1][3]),
                (d3, data3[2][3]), (d4, data3[3][3])])
th_n = th_v.subs([(th1, data3[0][4]), (th2, data3[1][4]),
                  (th3, data3[2][4]), (th4, data3[3][4])])

T_o = []
T_s = []
T_ns = []
T = []
for i in range(4):
    T_o.append(sp.Matrix([
        [cos(th_v[i]), -sin(th_v[i]), 0, a_v[i]],
        [sin(th_v[i]) * cos(a1_v[i]), cos(th_v[i]) *
         cos(a1_v[i]), -sin(a1_v[i]), -sin(a1_v[i]) * d_v[i]],
        [sin(th_v[i]) * sin(a1_v[i]), cos(th_v[i]) *
         sin(a1_v[i]), cos(a1_v[i]), cos(a1_v[i]) * d_v[i]],
        [0, 0, 0, 1],
    ])
    )
    T_s.append(sp.Matrix([
        [cos(th_s[i]), -sin(th_s[i]), 0, a_s[i]],
        [sin(th_s[i]) * cos(a1_s[i]), cos(th_s[i]) *
         cos(a1_s[i]), -sin(a1_s[i]), -sin(a1_s[i]) * d_s[i]],
        [sin(th_s[i]) * sin(a1_s[i]), cos(th_s[i]) *
         sin(a1_s[i]), cos(a1_s[i]), cos(a1_s[i]) * d_s[i]],
        [0, 0, 0, 1],
    ])
    )
    T_ns.append(sp.Matrix([
        [cos(th_ns[i]), -sin(th_ns[i]), 0, a_ns[i]],
        [sin(th_ns[i]) * cos(a1_ns[i]), cos(th_ns[i]) *
         cos(a1_ns[i]), -sin(a1_ns[i]), -sin(a1_ns[i]) * d_ns[i]],
        [sin(th_ns[i]) * sin(a1_ns[i]), cos(th_ns[i]) *
         sin(a1_ns[i]), cos(a1_ns[i]), cos(a1_ns[i]) * d_ns[i]],
        [0, 0, 0, 1],
    ])
    )
    T.append(sp.Matrix([
        [cos(th_n[i]), -sin(th_n[i]), 0, a_n[i]],
        [sin(th_n[i]) * cos(a1_n[i]), cos(th_n[i]) *
         cos(a1_n[i]), -sin(a1_n[i]), -sin(a1_n[i]) * d_n[i]],
        [sin(th_n[i]) * sin(a1_n[i]), cos(th_n[i]) *
         sin(a1_n[i]), cos(a1_n[i]), cos(a1_n[i]) * d_n[i]],
        [0, 0, 0, 1],
    ])
    )

print()
print('Matrices:')
print('Original symbolic matrix')
print(T_o)
print('\nSymbolic matrix with the table')
print(T_s)
print('\nSymbolic and substitution')
print(T_ns)

T01 = T_ns[0]
T02 = T01 * T_ns[1]
T03 = T02 * T_ns[2]
T04 = T03 * T_ns[3]
print(f"Substituting in T01, T12, T23, T34")
print('T01\n',nsimplify(T01,tolerance=1e-10,rational=True))
print('T02\n',nsimplify(T02,tolerance=1e-10,rational=True))
print('T03\n',nsimplify(T03,tolerance=1e-10,rational=True))
print('Final position of the end effector with respect to {0}')
print('T04\n',nsimplify(T04,tolerance=1e-10,rational=True))

print(f"\nNow Substituting all {chr(945)}, a, d and {chr(952)} values in T01, T12, T23, T34")

a = 0
b = 1
for mat in T:
    print('T' + str(a) + str(b))
    print(mat, '\n')
    a += 1
    b += 1

T01 = T[0]
T02 = T01 * T[1]
T03 = T02 * T[2]
T04 = T03 * T[3]
print('T01\n',T01)
print('T02\n',T02)
print('T03\n',T03)
print('T04\n',T04)

# Define unit vectors
i0 = sp.Matrix([1, 0, 0, 1])
j0 = sp.Matrix([0, 1, 0, 1])
k0 = sp.Matrix([0, 0, 1, 1])

print()
print('Homogeneous Transformations shape')
print(T01.shape)
print('Unit vectors shape')
print(i0.shape)

i01 = T01 * i0
j01 = T01 * j0
k01 = T01 * k0

i02 = T02 * i0
j02 = T02 * j0
k02 = T02 * k0

i03 = T03 * i0
j03 = T03 * j0
k03 = T03 * k0

i04 = T04 * i0
j04 = T04 * j0
k04 = T04 * k0

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.quiver(0, 0, 0, i0[0], i0[1], i0[2], color='red')
ax.quiver(0, 0, 0, j0[0], j0[1], j0[2], color='green')
ax.quiver(0, 0, 0, k0[0], k0[1], k0[2], color='blue')

# [1]
ax.plot3D(np.linspace(float(0), float(T01[0, 3])), np.linspace(float(0), float(T01[1, 3])), np.linspace(float(0), float(T01[2, 3])))
ax.quiver(T01[0,3], T01[1,3], T01[2,3], i01[0] - T01[0,3], i01[1] - T01[1,3], i01[2] - T01[2,3], color='red')
ax.quiver(T01[0,3], T01[1,3], T01[2,3], j01[0] - T01[0,3], j01[1] - T01[1,3], j01[2] - T01[2,3], color='green')
ax.quiver(T01[0,3], T01[1,3], T01[2,3], k01[0] - T01[0,3], k01[1] - T01[1,3], k01[2] - T01[2,3], color='blue')

# [2]
ax.plot3D(np.linspace(float(T01[0,3]), float(T02[0,3])), np.linspace(float(T01[1,3]), float(T02[1,3])), np.linspace(float(T01[2,3]), float(T02[2,3])))
ax.quiver(T02[0,3], T02[1,3], T02[2,3], i02[0] - T02[0,3], i02[1] - T02[1,3], i02[2] - T02[2,3], color='red')
ax.quiver(T02[0,3], T02[1,3], T02[2,3], j02[0] - T02[0,3], j02[1] - T02[1,3], j02[2] - T02[2,3], color='green')
ax.quiver(T02[0,3], T02[1,3], T02[2,3], k02[0] - T02[0,3], k02[1] - T02[1,3], k02[2] - T02[2,3], color='blue')
# [3]
ax.plot3D(np.linspace(float(T02[0,3]), float(T03[0,3])), np.linspace(float(T02[1,3]), float(T03[1,3])), np.linspace(float(T02[2,3]), float(T03[2,3])))
ax.quiver(T03[0,3], T03[1,3], T03[2,3], i03[0] - T03[0,3], i03[1] - T03[1,3], i03[2] - T03[2,3], color='red')
ax.quiver(T03[0,3], T03[1,3], T03[2,3], j03[0] - T03[0,3], j03[1] - T03[1,3], j03[2] - T03[2,3], color='green')
ax.quiver(T03[0,3], T03[1,3], T03[2,3], k03[0] - T03[0,3], k03[1] - T03[1,3], k03[2] - T03[2,3], color='blue')
# [4]
ax.plot3D(np.linspace(float(T03[0,3]), float(T04[0,3])), np.linspace(float(T03[1,3]), float(T04[1,3])), np.linspace(float(T03[2,3]), float(T04[2,3])))
ax.quiver(T04[0,3], T04[1,3], T04[2,3], i04[0] - T04[0,3], i04[1] - T04[1,3], i04[2] - T04[2,3], color='red')
ax.quiver(T04[0,3], T04[1,3], T04[2,3], j04[0] - T04[0,3], j04[1] - T04[1,3], j04[2] - T04[2,3], color='green')
ax.quiver(T04[0,3], T04[1,3], T04[2,3], k04[0] - T04[0,3], k04[1] - T04[1,3], k04[2] - T04[2,3], color='blue')
ax.set_title('3D Plot')
ax.set_xlabel('Eje X_0')
ax.set_ylabel('Eje Y_0')
ax.set_zlabel('Eje Z_0')
ax.set_xlim(xmin, xmax)
ax.set_ylim(ymin, ymax)
ax.set_zlim(zmin, zmax)
plt.show()
