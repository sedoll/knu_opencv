import cv2

# python 3.11 / opencv 4.7.0 이상에서 웹캠을 실행할 경우 이와 같이 실행
from cv2 import VideoCapture 
cap = VideoCapture(0)

cap = cv2.VideoCapture(0)

frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

while True:
    ret, frame = cap.read()
    
    if not ret:
        break
    
    key = cv2.waitKey(1)
    
    if key == 27:
        break
    
if cap.isOpened():
    cap.release()
cv2.destroyAllWindows()