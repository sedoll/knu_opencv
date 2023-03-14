# plt 영상 출력

import cv2
from matplotlib import pyplot as plt

def handle_key_press(event): # 키보드 이벤트 처리 함수
    if event.key == 'escape':
        cap.release()
        plt.close()

def handle_close(): # 윈도우 딛기 이벤트 처리 함수
    print('Close figure!')
    cap.release()
    
cap = cv2.VideoCapture(0)

plt.ion() # 대화모드 설정
fig = plt.figure(figsize=(10, 6)) # 화면의 크기를 10x6 인치로 설정
plt.axis('off')

fig.canvas.manager.set_window_title('Video Capture')
fig.canvas.mpl_connect('key_press_event', handle_key_press)
fig.canvas.mpl_connect('close_event', handle_close)

ret, frame = cap.read() # 첫 프레임 캡처

im = plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

while True:
    ret, frame = cap.read()
    
    if not ret:
        break
    
    # plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)) 
    im.set_array(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)) # 이걸 사용하는게 더 빠르다.
    
    # fig.canvas.draw_idle() 
    fig.canvas.draw() # 화면 갱신, 이걸 사용하는게 더 빠르다.
    fig.canvas.flush_events() # gui 이벤트 처리
    
if cap.isOpened():
    cap.release()