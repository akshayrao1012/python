import cv2
import numpy as np

blank_image = np.zeros((512,512,3),np.uint8)

######################################################################################################
from datetime import datetime
dateTimeObj = datetime.now()
timeObj = dateTimeObj.time()

# dateTimeObj.microsecond -- microsecond value in int
# dateTimeObj.second -- seconds value in int
# dateTimeObj.minute -- minute value in int
# dateTimeObj.hour -- hour value in int
# dateTimeObj.day -- day value in int
# dateTimeObj.month -- month value in int
# dateTimeObj.year -- year value in int

ss = "."
msec = str(dateTimeObj.microsecond)
msec_ini = msec[:3]
sec = str(dateTimeObj.second)
mins = str(dateTimeObj.minute)
hrs = str(dateTimeObj.hour)
day = str(dateTimeObj.day)
mon = str(dateTimeObj.month)
year = str(dateTimeObj.year)

time_stamp_now = msec_ini + ss + sec + ss + mins + ss + hrs + ss + day + ss + mon + ss + year

#print(time_stamp_now)
######################################################################################################

cv2.putText(blank_image,time_stamp_now,(100,500),cv2.FONT_HERSHEY_COMPLEX,1,(0,64,128),1)


cv2.imshow("blank_image",blank_image)
cv2.waitKey(0)