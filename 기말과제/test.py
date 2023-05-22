import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('c:/data/1215.png', cv2.IMREAD_GRAYSCALE)
cumulative_hist = np.zeros((256, 1), dtype=np.float32)

a = cv2.calcHist(images=[img], channels=[0], mask=None, histSize=[256], ranges=[0, 256])

plt.plot(a)
plt.show()

image_files = ['c:/data/1215.png', 'c:/data/1216.png', 'c:/data/1218.png']

for image_file in image_files:
    # 이미지 로드
    image = cv2.imread(image_file)

    # 이미지의 히스토그램 계산
    hist = cv2.calcHist([image], [0], None, [256], [0, 256])

    # hist를 cumulative_hist와 동일한 차원으로 변경
    hist = hist.squeeze()  # 차원 축소
    hist = hist.reshape(-1, 1)  # 열 벡터로 변환
    
    # 누적 히스토그램 업데이트
    cumulative_hist += hist

cumulative_hist /= len(image_files)

plt.plot(cumulative_hist)
plt.show()