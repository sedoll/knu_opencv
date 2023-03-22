# 교수님 책 버전, 이게 딜레이는 있지만 프레임은 더 잘나옴
from urllib.request import urlopen
import cv2
import numpy as np
import time

url = "http://192.168.0.2:8080/video"

cap = cv2.VideoCapture(url)

# frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
#               int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
# print(frame_size)

while True:
    ret, frame = cap.read()
    
    if not ret:
        print('not ret')
        break
    
    frame = cv2.resize(frame, (480, 270))
    
    cv2.imshow('frame', frame)
    
    key = cv2.waitKey(25)
    if key == 27:
        break
    
if cap.isOpened():
    cap.release()

cv2.destroyAllWindows()