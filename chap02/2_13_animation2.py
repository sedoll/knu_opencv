# plt 애니메이션 출력 2

import cv2
from matplotlib import pyplot as plt
from matplotlib import animation

class Video:
    # 첫 프레임을 가져오기(맛보기용, 정보 확인용)
    def __init__(self, device=0):
        self.cap=cv2.VideoCapture(device)
        self.ret, self.frame = self.cap.read()
        self.im = plt.imshow(cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB))
        print('start capture ...')
        
    def updateFrame(self, k): # 프레임 갱신
        self.ret, self.frame = self.cap.read()
        self.im.set_array(cv2.cvtColor(camera.frame, cv2.COLOR_BGR2RGB))

    def close(self): # 종료
        if self.cap.isOpened():
            self.cap.release()
        print('finish capture.')

fig = plt.figure()
fig.canvas.manager.set_window_title('Video capture')
plt.axis('off')

camera = Video()
ani = animation.FuncAnimation(fig, camera.updateFrame, interval=50)
plt.show()
camera.close()