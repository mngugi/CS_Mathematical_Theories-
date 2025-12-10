import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.widgets import Slider

# initial vectors
v1 = np.array([2, 1, 1])
v2 = np.array([1, 2, 0.5])

# figure + 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# sliders UI area
plt.subplots_adjust(bottom=0.35)

# result
v_sum = v1 + v2

# draw arrows
q1 = ax.quiver(0, 0, 0, 0, 0, 0, color='blue')
q2 = ax.quiver(0, 0, 0, 0, 0, 0, color='red')
q3 = ax.quiver(0, 0, 0, 0, 0, 0, color='green')

# sliders
ax_v1_x = plt.axes([0.2, 0.25, 0.65, 0.03])
ax_v1_y = plt.axes([0.2, 0.20, 0.65, 0.03])
ax_v1_z = plt.axes([0.2, 0.15, 0.65, 0.03])

ax_v2_x = plt.axes([0.2, 0.10, 0.65, 0.03])
ax_v2_y = plt.axes([0.2, 0.05, 0.65, 0.03])
ax_v2_z = plt.axes([0.2, 0.00, 0.65, 0.03])

s_v1_x = Slider(ax_v1_x, 'v1_x', -3, 3, valinit=v1[0])
s_v1_y = Slider(ax_v1_y, 'v1_y', -3, 3, valinit=v1[1])
s_v1_z = Slider(ax_v1_z, 'v1_z', -3, 3, valinit=v1[2])

s_v2_x = Slider(ax_v2_x, 'v2_x', -3, 3, valinit=v2[0])
s_v2_y = Slider(ax_v2_y, 'v2_y', -3, 3, valinit=v2[1])
s_v2_z = Slider(ax_v2_z, 'v2_z', -3, 3, valinit=v2[2])

def animate(frame):
    global q1, q2, q3
    for q in [q1, q2, q3]:
        q.remove()

    # live slider values
    v1_new = np.array([s_v1_x.val, s_v1_y.val, s_v1_z.val])
    v2_new = np.array([s_v2_x.val, s_v2_y.val, s_v2_z.val])

    t = frame/50

    # animated head-to-tail
    q1 = ax.quiver(0,0,0, v1_new[0]*t, v1_new[1]*t, v1_new[2]*t, color='blue')
    q2 = ax.quiver(v1_new[0]*t, v1_new[1]*t, v1_new[2]*t,
                   v2_new[0]*t, v2_new[1]*t, v2_new[2]*t, color='red')
    q3 = ax.quiver(0,0,0,
                   (v1_new[0]+v2_new[0])*t,
                   (v1_new[1]+v2_new[1])*t,
                   (v1_new[2]+v2_new[2])*t,
                   color='green')

    ax.set_xlim([-4,4])
    ax.set_ylim([-4,4])
    ax.set_zlim([-4,4])

ani = FuncAnimation(fig, animate, frames=60, interval=60)

plt.show()
