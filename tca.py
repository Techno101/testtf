from picamera import PiCamera
#from time import sleep
#import takepic
#import resizeimg
import os
import cv2
import face_recognition

def takeImage():
    cam = cv2.VideoCapture(0)
    cv2.namedWindow("test")

    while True:
        ret, frame = cam.read()
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        face_locations = face_recognition.face_locations(small_frame)
        
        if len(face_locations) > 0:
            save_img = frame.copy()
        
        for top, right, bottom, left in face_locations:
            # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            
        
        cv2.imshow("test", frame)
        if not ret:
            break
        k = cv2.waitKey(1)

        if k%256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            cam.release()
            return None
        elif k%256 == 32:
            # SPACE pressed
            return save_img

    cv2.destroyAllWindows()


maxdim = 320

# Main Function
cwd = os.getcwd()
if not os.path.isdir("images"):
    os.mkdir("images")
os.chdir("images")
while True:
    name = input("Enter your name without spaces; empty to finish ")
    if len(name) == 0:
        break
    if not os.path.isdir(name):
        os.mkdir(name)
    os.chdir(name)
    count = 0
    while True:
        img = takeImage()
        if img is None:
            break
        img_name = name + str(count) + ".jpg"

        status = cv2.imwrite(img_name, img)
        count += 1
        #rs(nameDir, maxdim)
    os.chdir("..")
    cv2.destroyAllWindows()
    
