import cv2
import numpy as np


def quad(img: np.ndarray, x, y, nx, ny, max_colors):
    colors = set()
    width = nx - x
    height = ny - y
    for i in range(x, nx):
        for j in range(y, ny):
            colors.add(str(img[i, j, :]))
            if len(colors) > max_colors:
                break
        if len(colors) > max_colors:
            break

    if len(colors) <= max_colors:
        mean = np.array([0, 0, 0])
        for i in range(x, nx):
            for j in range(y, ny):
                mean += img[i, j, :]
        mean //= width * height
        img[x: nx, y: ny, :] = np.repeat([np.repeat([mean], ny - y, axis=0)], nx - x, axis=0)
    elif width > 4 and height > 4:
        mx, my = width // 2 + x, height // 2 + y
        quad(img, x, y, mx, my, max_colors)
        quad(img, mx, y, nx, my, max_colors)
        quad(img, x, my, mx, ny, max_colors)
        quad(img, mx, my, nx, ny, max_colors)


image_name = 'scenery.jpg'

image_cv2 = cv2.imread(f'sample-imgs/{image_name}')

width, height, *_ = image_cv2.shape

quad(image_cv2, 0, 0, width, height, 1000)

print(image_cv2.size)

result = cv2.imwrite(f'output/{image_name}', image_cv2)
if result:
    print('File saved successfully')
else:
    print('Error in saving file')

cv2.imshow("Image display", image_cv2)
cv2.waitKey(0)
cv2.destroyAllWindows()
