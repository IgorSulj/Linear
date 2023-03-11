from matplotlib.lines import Line2D
from matplotlib.axes._axes import Axes

def draw_lines_to_point(ax: Axes, x_start, x_end, y_start, y_end):
    line_from_x = Line2D([x_end, x_end], [y_start, y_end])
    line_from_y = Line2D([x_start, x_end], [y_end, y_end])
    ax.add_line(line_from_x)
    ax.add_line(line_from_y)
