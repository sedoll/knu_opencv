# 이건 딜레이는 조금 짧지만 프레임이 너무 낮음
from urllib.request import urlopen
import cv2
import numpy as np

# 웹브라우저를 통해 http://192.168.0.2:8080/
# 에 들어가서 영상 재생기를 자바스크립트로 한 다음에 
# 영상 이미지 주소 복사를 한 링크를 url에 복사
url = "http://192.168.0.2:8080/shot.jpg"

while True:
    
    # urllib를 사용하여 이미지를 가져오고 cv2 사용 가능한 형식으로 변환
    imgResp = urlopen(url)
    imgNp = np.array(bytearray(imgResp.read()), dtype=np.uint8)
    frame = cv2.imdecode(imgNp, -1)
    
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # 흑백으로 변경
    frame = cv2.resize(frame, (720, 480)) # 화면 크기 조정
    
    # OpenCV 창으로 출력
    cv2.imshow('IpWebCam', frame)
    
    key = cv2.waitKey(50)
    
    if key == 27:
        break
    
cv2.destroyAllWindows()