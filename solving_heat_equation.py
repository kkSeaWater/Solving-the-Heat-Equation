#Tannous, Edward Charbel - 397122
object_length = 1
gamma = 0.01 # thermal diffusivity constant

# collecting input from the user
h = float(input("Enter h: "))
dt = float(input("Enter dt: "))

import numpy as np
# how many heat points to be calculated
# length divided by step size
points = int(object_length / h)

if points < 1:
  raise ValueError("h is too large")

# essentially simulation length
time_steps = 10000
# u array explained in document
u = np.zeros((time_steps, points))

# boundary #1
u[0, 0] = 0
# middle boundary is an initial condition
u[0, :] = 10 * np.sin(np.pi * np.arange(1, points+1) * h / object_length)
u[-1, 0] = 0 # boundary #2

for t in range(time_steps - 1): # for every time
    for x in range(1, points - 1): # for every x
        # update equation
        u[t+1, x] = u[t, x] + gamma * h**2 * (u[t, x+1] - 2*u[t, x] + u[t, x-1])

import matplotlib.pyplot as plt
# plot assignments
x = np.linspace(0, object_length, points)
t = np.linspace(0, time_steps * dt, time_steps)
X, T = np.meshgrid(x, t)
fig = plt.figure()

# plotting
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, T, u, cmap='Reds')
ax.set_xlabel('x')
ax.set_ylabel('t')
ax.set_zlabel('Temperature')
plt.show()

# stability check
if h**2 / (2 * gamma) > dt:
    print("WARNING")
