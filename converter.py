import numpy as np


class Converter:
    def __init__(self, img: np.ndarray):
        self.__img = img.copy()
        self.__output_img = img.copy()
        self.__progress = 0

    def set_image(self, img: np.ndarray):
        self.__img = img.copy()

    def quadify_image(self, max_colors):
        print('    25   50   75   100')
        self.__output_img = self.__img.copy()
        width, height, *_ = self.__output_img.shape
        self._quad(0, 0, width, height, max_colors, 0)
        print(' | Complete')
        return self.__output_img

    def _update_progress(self, new_progress):
        temp = self.__progress
        self.__progress += new_progress
        if temp // 0.05 < self.__progress // 0.05:
            print('#', end='')


    def _quad(self, x, y, nx, ny, max_colors, depth):
        colors = set()
        width = nx - x
        height = ny - y
        for i in range(x, nx):
            for j in range(y, ny):
                colors.add(str(self.__output_img[i, j, :]))
                if len(colors) > max_colors:
                    break
            if len(colors) > max_colors:
                break

        if len(colors) <= max_colors:
            # pixel_to_color_ratio = width * height / len(colors)
            self.__output_img[x: nx, y: ny, :] = np.mean(self.__output_img[x: nx, y: ny, :], axis=(0, 1)) # * pixel_to_color_ratio
            self._update_progress(0.25 ** depth)
        elif width > 4 and height > 4:
            mx, my = width // 2 + x, height // 2 + y
            self._quad(x, y, mx, my, max_colors, depth + 1)
            self._quad(mx, y, nx, my, max_colors, depth + 1)
            self._quad(x, my, mx, ny, max_colors, depth + 1)
            self._quad(mx, my, nx, ny, max_colors, depth + 1)
