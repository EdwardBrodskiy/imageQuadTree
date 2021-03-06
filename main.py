import cv2
from converter import *

image_name = input('Enter file name: ')

image_cv2 = cv2.imread(f'input-images/{image_name}')

maker = Converter(color_count_method=Converter.color_count_differing)

maker.set_image(image_cv2)

quad_image = maker.quadify_image(7)

result = cv2.imwrite(f'sample-images/{image_name}', quad_image)

if result:
    print('File saved successfully')
else:
    print('Error in saving file')

# cv2.imshow("Result display", quad_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
