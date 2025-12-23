import matplotlib.pyplot as plt
import numpy as np

def Nf(z, f, df):
    return z - f(z)/df(z)

def runNewton(z, f, df, N, epsilon):
    for i in range(N):
        if df(z) == 0:
            return z, i
        z = Nf(z, f, df)
        if abs(f(z)) <= epsilon:
            return z, i
    return z, N

N = 20
epsilon = 0.0000000001
f = lambda z: z**4 -0.84*z**2-0.16
df = lambda z: 4*z**3 -2*0.84*z

dx = 0.001
dy = 0.001
rx = (-1, 1)
ry = (-1, 1)

X, Y = np.meshgrid(np.arange(rx[0], rx[1], dx), np.arange(ry[0], ry[1], dy))
Z = X + 1j*Y

roots = np.zeros(Z.shape, dtype=complex)
iterations = np.zeros(Z.shape, dtype=int)

exact_roots = np.array([], dtype=complex)
base_colors = np.empty((0, 3), dtype=float)
cmap = plt.cm.get_cmap('tab10')

for i in range(Z.shape[0]):
    for j in range(Z.shape[1]):
        z, it = runNewton(Z[i,j], f, df, N, epsilon)
        roots[i,j] = z
        iterations[i,j] = it
        if it < N:
            tol = 1e-6
            if exact_roots.size == 0:
                exact_roots = np.append(exact_roots, z)
                new_color = cmap(0)[:3]
                base_colors = np.vstack([base_colors, new_color])
            else:
                if not np.any(np.abs(exact_roots - z) < tol):
                    exact_roots = np.append(exact_roots, z)
                    new_color = cmap((exact_roots.size - 1) % 10)[:3]
                    base_colors = np.vstack([base_colors, new_color])

colors = np.zeros(Z.shape + (3,), dtype=float) 

for i in range(Z.shape[0]):
    for j in range(Z.shape[1]):
        dists = np.abs(roots[i,j] - exact_roots)
        idx = np.argmin(dists)
        base_color = base_colors[idx]

        intensity = iterations[i,j] / N
        color = base_color * (1 - 0.5 * intensity)
        colors[i,j] = color

plt.figure(figsize=(8,8))
plt.imshow(colors, extent=(rx[0], rx[1], ry[0], ry[1]), origin='lower')
plt.xlabel("Re(z)")
plt.ylabel("Im(z)")
plt.show()
