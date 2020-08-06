def iterate_cartesian(iter0, iter1):
    for i in iter0:
        for j in iter1:
            yield i, j


def iterate_in_steps(x, y, nx, ny, step=2):
    for offset_x, offset_y in iterate_cartesian(range(step), range(step)):
        for i, j in iterate_cartesian(range(x + offset_x, nx, step), range(y + offset_y, ny, step)):
            yield i, j

