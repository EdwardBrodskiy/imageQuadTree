import cv2
from converter import *

image_name = 'scenery2.jpg'

image_cv2 = cv2.imread(f'sample-imgs/{image_name}')

maker = Converter(image_cv2)

quad_image = maker.quadify_image(100)

result = cv2.imwrite(f'output/{image_name}', quad_image)

if result:
    print('File saved successfully')
else:
    print('Error in saving file')

cv2.imshow("Image display", quad_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
