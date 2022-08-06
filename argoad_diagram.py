import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10,11)
y = np.abs(x)


fig, ax = plt.subplots()

# making the top and right spine invisible:
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')

# moving bottom spine up to y=0 position:
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))

# moving left spine to the right to position x == 0:
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))


def rotate_plot(x, y, com_num):
    updated = list(map(lambda x : x*com_num, [complex(*i) for i in list(zip(x,y))]))
    return [i.real for i in updated], [i.imag for i in updated]

ax.plot(*rotate_plot(np.arange(-10,11), np.arange(-10,11), complex(2,1)))
plt.grid()
plt.show()
