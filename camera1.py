import cv2

cv2.namedWindow("preview")
cap = cv2.VideoCapture(0)
cap.set(3,640) # set Width
cap.set(4,480) # set Height

if cap.isOpened(): # try to get the first frame
    rval, frame = cap.read()
else:
    rval = False

while rval:
    cv2.imshow("preview", frame)
    rval, frame = cap.read()
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break
cv2.destroyWindow("preview")
