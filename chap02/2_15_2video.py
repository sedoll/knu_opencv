# plt 애니메이션 클래스 상속

import cv2
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

# Video 클래스를 정의하며, animation 모듈의 FuncAnimation 클래스를 상속받는다.
class Video(animation.FuncAnimation):
    
    # Video 클래스의 생성자 함수이다. 매개변수로 device, fig, frames, interval, repeat_delay, blit, **kwargs를 받는다.
    # device: 카메라 장치 번호. 디폴트값은 0이다.
    # fig: subplot을 만들기 위한 matplotlib figure 객체. 디폴트값은 None이다.
    # frames: 애니메이션의 프레임 수. 디폴트값은 None이다.
    # interval: 애니메이션의 갱신 주기(ms). 디폴트값은 80ms이다.
    # repeat_delay: 애니메이션 반복 지연시간(ms). 디폴트값은 5ms이다.
    # blit: 블리팅 여부. 디폴트값은 False이다.
    # **kwargs: 추가적인 인수들을 받는다.
    def __init__(self, device=0, fig = None, frames = None, interval = 80, 
                 repeat_delay = 5, blit = False, **kwargs):
        
        # 만약 fig가 None이라면, fig와 ax를 생성한다. subplot을 만들기 위해 subplots() 함수를 사용하며, 1행 2열, figsize가 (10, 5)인 subplot을 생성한다.
        # 생성된 subplot들의 window_title을 'Video capture'로 설정
        if fig is None:
            self.fig, self.ax = plt.subplots(1, 2, figsize=(10, 5))
            self.fig.canvas.manager.set_window_title('Video capture')
            
            # subplot(ax[0])의 위치와 축을 설정한다.
            self.ax[0].set_position([0, 0, 0.5, 1])
            self.ax[0].axis('off')
            
            # subplot(ax[1])도 위치와 축을 설정한다.
            self.ax[1].set_position([0.5, 0, 0.5, 1])
            self.ax[1].axis('off')
            
            # 상속받은 FuncAnimation 클래스의 생성자 함수를 호출한다.
            # 첫 번째 매개변수로 self.fig, 두 번째 매개변수로 self.updateFrame 함수를 전달한다.
            # init_func는 애니메이션의 첫 프레임을 생성하기 위해 호출되는 함수이다. Video 클래스에서는 self.init 함수가 이 역할을 한다.
            # frames는 애니메이션의 프레임 수이다.
            # interval: 애니메이션의 갱신 주기(ms) 이다.
            # repeat_delay: 애니메이션 반복 지연시간(ms) 이다.
            # blit: 블리팅 여부 이다.
            # **kwargs: 추가적인 인수들을 받는다.
            super(Video, self).__init__(self.fig, self.updateFrame, init_func = self.init, frames = frames, 
                                    interval = interval, blit = blit, repeat_delay = repeat_delay, **kwargs)
            self.cap = cv2.VideoCapture(device)
            print('start capture')
    
    # 이 클래스에서 애니메이션을 초기화하기 위해 사용되는 메소드입니다. 
    # cv2.VideoCapture 객체를 사용하여 초기 프레임을 캡처합니다. 
    # 프레임이 성공적으로 캡처되면, imshow() 메소드를 사용하여 초기화된 그림 객체를 반환합니다
    def init(self):
        ret, self.frame = self.cap.read()
        if ret:
            self.im0 = self.ax[0].imshow(cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB), aspect='auto')
            self.im1 = self.ax[1].imshow(np.zeros(self.frame.shape, self.frame.dtype), aspect='auto')
        print('start capture ...')
    
    # updateFrame 메소드는 애니메이션을 업데이트하는 데 사용됩니다. 
    # 이 메소드는 매 프레임마다 실행됩니다. 이 메소드는 cv2.VideoCapture 객체를 사용하여 프레임을 캡처하고,
    # imshow() 메소드를 사용하여 각 subplot을 업데이트합니다.
    def updateFrame(self, k): # 프레임 갱신
        # global gray
        ret, self.frame = self.cap.read()
        if ret:
            self.im0.set_array(cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB))
            gray = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
            self.im1.set_array(cv2.merge((gray, gray, gray)))

    def close(self): # 종료
        if self.cap.isOpened():
            self.cap.release()
        print('finish capture.')

camera = Video()
plt.show()
camera.close()