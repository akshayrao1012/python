#successful folder save image
import cv2
cam = cv2.VideoCapture(1)
cv2.namedWindow("Image_Capture")

path = "D:\Workspace\code_space\github\Python\lets_time_stamp\image_folder"

while True:
    ############################################################################
    from datetime import datetime
    dateTimeObj = datetime.now()
    timeObj = dateTimeObj.time()
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
    # print(time_stamp_now)
    ############################################################################
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("Image_Capture", frame)

    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape pressed, so now closing")
        break
    elif k%256 == 32:
        # SPACE pressed
        image_name = path+"\{}.png".format(time_stamp_now)
        cv2.putText(frame, time_stamp_now, (100,450), cv2.FONT_HERSHEY_SIMPLEX , 1, (1, 1, 1), 2)
        cv2.imwrite(image_name, frame)
        print("image captured")
        print("{} written!".format(image_name))

cam.release()
cv2.destroyAllWindows()