import cv2 as cv
import numpy as np

iteration = 1
dirs= ['left_cam', 'right_cam']
# dirs=['left_cam_chess', 'right_cam_chess']


def save_image(*args):
    global iteration, dirs
    
    for no in range(2):
        cv.imwrite(f'{dirs[no]}/{iteration}.png', args[no])
    
    iteration += 1
    print('saved')

def reset():
    pass


left=1
right=2

cap = cv.VideoCapture(left)
cap.set(3, 640)
cap.set(4, 480)

cap2 = cv.VideoCapture(right)
cap2.set(3, 640)
cap2.set(4, 480)


while True:
    _, img1 = cap.read()
    img1=cv.flip(img1, 2)
    cv.imshow('Left', img1)

    
    _, img2 = cap2.read()
    img2=cv.flip(img2, 2)
    cv.imshow('Right', img2)
    
    key=cv.waitKey(1)
    
    if key ==32:
        save_image(img1, img2)
    if key ==27:
        break

cap.release()
cap2.release()
cv.destroyAllWindows()