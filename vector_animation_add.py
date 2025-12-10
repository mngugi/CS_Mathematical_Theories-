import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# define vectors
v1 = np.array([2, 1])
v2 = np.array([1, 2])

fig, ax = plt.subplots()
ax.set_xlim(0, 4)
ax.set_ylim(0, 4)

# plot empty arrows (will update)
arrow1 = ax.arrow(0,0,0,0, head_width=0.1)
arrow2 = ax.arrow(0,0,0,0, head_width=0.1)
arrow_sum = ax.arrow(0,0,0,0, head_width=0.1)

# animation function
def update(frame):
    ax.clear()
    ax.set_xlim(0, 4)
    ax.set_ylim(0, 4)

    t = frame/50

    # gradually draw arrows
    ax.arrow(0,0, v1[0]*t, v1[1]*t, head_width=0.1, color='blue')
    ax.arrow(v1[0]*t,v1[1]*t, v2[0]*t, v2[1]*t, head_width=0.1, color='red')

    # sum vector
    ax.arrow(0,0, (v1[0]+v2[0])*t, (v1[1]+v2[1])*t, head_width=0.1, color='green')

    ax.text(0.2,3.5,"Adding Vectors", fontsize=14)

ani = animation.FuncAnimation(fig, update, frames=50, interval=60)

plt.show()
