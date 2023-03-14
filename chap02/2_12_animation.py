# plt 애니메이션 영상 출력

import cv2
from matplotlib import pyplot as plt
from matplotlib import animation

cap = cv2.VideoCapture(0) # 카메라 선택
fig = plt.figure(figsize=(10, 6)) # plt 크기 조정
fig.canvas.manager.set_window_title('Video capture') # plt title 지정
plt.axis('off') # 눈금자 표시 x

def init():
    global im
    retval, frame = cap.read() # 첫 프레임 캡처
    im = plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

def updateFrame(k): 
    retval, frame = cap.read()	# 프레임 읽어오기
    if retval:	# 읽어온것이 성공(True)하면
        im.set_array(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))	# 프레임 정보를 가지고 색상 변환 작업 진행

# interval : ms단위의 프레임 간 지연 시간
# animation함수로 fig창에 init으로 초기화하고 50 msec마다 updateFrame을 읽어옴
ani = animation.FuncAnimation(fig, updateFrame, init_func = init, interval = 50)

plt.show()

if cap.isOpened:
    cap.release()