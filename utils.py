import numpy as np
from matplotlib.lines import Line2D
from matplotlib.axes._axes import Axes

_lines_style = {'linestyle': '--', 'color': 'black'}


def draw_lines_to_point(ax: Axes, x_end, y_end):
    '''
    Строим перпендикуляры к точке, заданной x_end и y_end
    '''
    x_start = ax.get_xlim()[0]
    y_start = ax.get_ylim()[0]
    line_from_x = Line2D([x_end, x_end], [y_start, y_end], **_lines_style)
    line_from_y = Line2D([x_start, x_end], [y_end, y_end], **_lines_style)
    ax.add_line(line_from_x)
    ax.add_line(line_from_y)
    if x_end not in (xticks := ax.get_xticks()):
        ax.set_xticks(np.append(xticks, x_end))
    if y_end not in (yticks := ax.get_yticks()):
        ax.set_yticks(np.append(yticks, y_end))
