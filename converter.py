import numpy as np
from customIterTools import *
from progress.bar import IncrementalBar


class Converter:

    def __init__(self, color_count_method=None):
        if color_count_method:
            self.color_count_method = color_count_method
        else:
            self.color_count_method = self.color_count_all

        self.__img = None
        self.__output_img = None
        self.__progress = 0
        self.__progress_bar = None

    def set_image(self, img: np.ndarray):
        self.__img = img.copy()

    def quadify_image(self, max_colors):
        self.__progress_bar = IncrementalBar('Render Progress', suffix='%(percent)d%%')

        self.__output_img = self.__img.copy()
        width, height, *_ = self.__output_img.shape
        self._quad(0, 0, width, height, max_colors, 0)

        self.__progress_bar.finish()
        return self.__output_img

    def _update_progress(self, new_progress):
        temp = self.__progress
        self.__progress += new_progress
        self.__progress_bar.goto(self.__progress * 100)
        if temp // 0.05 < self.__progress // 0.05:
            print('#', end='')

    def _quad(self, x, y, nx, ny, max_colors, depth):

        width = nx - x
        height = ny - y

        num_of_colors = self.color_count_method(self.__output_img, x, y, nx, ny, max_colors)

        if num_of_colors <= max_colors:
            # pixel_to_color_ratio = width * height / num_of_colors
            self.__output_img[x: nx, y: ny, :] = np.mean(self.__output_img[x: nx, y: ny, :],
                                                         axis=(0, 1))  # * pixel_to_color_ratio
            self._update_progress(0.25 ** depth)
        else:
            mx, my = width // 2 + x, height // 2 + y
            self._quad(x, y, mx, my, max_colors, depth + 1)
            self._quad(mx, y, nx, my, max_colors, depth + 1)
            self._quad(x, my, mx, ny, max_colors, depth + 1)
            self._quad(mx, my, nx, ny, max_colors, depth + 1)

    @staticmethod
    def color_count_all(img, x, y, nx, ny, max_colors):
        colors = set()
        for i, j in iterate_cartesian(range(x, nx), range(y, ny)):
            colors.add(str(img[i, j, :]))
            if len(colors) > max_colors:
                return len(colors)

        return len(colors)

    @staticmethod
    def color_count_differing(img, x, y, nx, ny, max_colors):
        colors = []
        for i, j in iterate_in_steps(x, y, nx, ny, step=(ny - y) // 8):
            pixel_color = img[i, j, :]
            for color in colors:
                if ((color - pixel_color) ** 2).sum() < 256:
                    break
            else:
                colors.append(pixel_color)
                if len(colors) > max_colors:
                    return len(colors)
        return len(colors)
