import cv2
import numpy as np

blank_image = np.zeros((512,512,3),np.uint8)

cv2.imshow("blank_image",blank_image)
cv2.waitKey(0)