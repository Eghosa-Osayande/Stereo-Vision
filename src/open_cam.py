import cv2 as cv
import numpy as np
import time

left= 2
right=1

cap = cv.VideoCapture(left)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 640)
cap.set(cv.CAP_PROP_FRAME_WIDTH, 480)


cap2 = cv.VideoCapture(right)
cap2.set(cv.CAP_PROP_FRAME_HEIGHT, 640)
cap2.set(cv.CAP_PROP_FRAME_WIDTH, 480)



while True:
    _, img1 = cap.read()
    img1=cv.flip(img1, 2)
    cv.imshow('Left', img1)
    
    _, img2 = cap2.read()
    img2=cv.flip(img2, 2)
    cv.imshow('Right', img2)
    
    key=cv.waitKey(1)
    
    if key ==27:
        break

cap.release()
cap2.release()
cv.destroyAllWindows()


