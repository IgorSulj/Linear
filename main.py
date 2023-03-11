import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from data import x, y, a, b
from utils import draw_lines_to_point

matplotlib.rc('font', size=18)

fig, ax = plt.subplots()

ax.plot(x, y, marker='o', label='Исходные данные')

long_x = np.append(x, [3.05])
ax.plot(long_x, a*long_x + b,
        label=f'Приближённая линейная зависимость\n'
              f'(y$\\approx${a:.2f}x+{b:.2f})')
ax.legend()
ax.set_xlabel('Объём производства, у.е.', labelpad=20.)
ax.set_ylabel('Затраты, тыс. руб.', labelpad=20.)

draw_lines_to_point(ax, 3., a * 3. + b)

plt.show()
