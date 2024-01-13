import cv2
import numpy as np
from matplotlib import pyplot as plt

# a 
# 원본 이미지 불러오기
# img = cv2.imread('c:/data/lena.jpg', cv2.IMREAD_GRAYSCALE) # lena 사진
img = cv2.imread('c:/data/moon2.jpg', cv2.IMREAD_GRAYSCALE) # 달 사진
# img = cv2.resize(img, (350, 350)) # 사진 크기 조절

cv2.imshow('a', img) # 원본 출력

# 원본에 가우시안 흐림 처리
blur_g = cv2.GaussianBlur(img, ksize=(3, 3), sigmaX=0.0)

# b 
# 라플라시안 함수 사용
# 원본에 라플라시안 바로 적용, 블러 처리한 이미지 보다 미분 오차 증가
laplacian = cv2.Laplacian(img, cv2.CV_8U)
# laplacian = cv2.Laplacian(img, cv2.CV_32F)
# laplacian = np.uint8(np.absolute(laplacian)) # cv2.CV_32F numpy 이용해 절대값화
# laplacian = cv2.convertScaleAbs(laplacian) # cv2.CV_32F convertScaleAbs 이용해 절대값화

# 블러 처리한 이미지에 라플라시안 적용
# 라플라시안 필터를 사용할 때에는 미분 오차 감소를 위해 가우시안 블러 처리를 한 이미지를 사용한다.
# laplacian = cv2.Laplacian(blur_g, cv2.CV_8U, ksize=1)

# 직접 구현한 라플라시안 필터에 적용, ksize = 1
laplacian_kernel = np.array([[0, 1, 0], 
                      [1, -4, 1], 
                      [0, 1, 0]])
laplacian2 = cv2.filter2D(img, cv2.CV_8U, laplacian_kernel)
cv2.imshow('b', laplacian) # 라플라시안 적용된 이미지 출력
# cv2.imshow('b2', laplacian2)

# c 
# 원본 - 라플라시안
Mlaplacian = cv2.subtract(img, laplacian)
Mlaplacian2 = cv2.subtract(img, laplacian2)
cv2.imshow('c', Mlaplacian)
# cv2.imshow('c2', Mlaplacian2)

# d 
# 원본에 소벨 필터 적용
# opencv 함수 이용한 소벨 필터 적용
sobelx = cv2.Sobel(img, cv2.CV_32F, 1, 0, ksize=3) # x 축 미분
sobely = cv2.Sobel(img, cv2.CV_32F, 0, 1, ksize=3) # y 축 미분

# 직접 구현한 소벨 필터 적용
# sobelx_kernel = np.array([[-1, 0, 1], 
#                    [-2, 0, 2],
#                    [-1, 0, 1]])
# sobely_kernel = np.array([[-1, -2, -1], 
#                    [0, 0, 0],
#                    [1, 2, 1]])
# sobelx2 = cv2.filter2D(img, cv2.CV_32F, sobelx_kernel)
# sobely2 = cv2.filter2D(img, cv2.CV_32F, sobely_kernel)

mag = cv2.magnitude(sobelx, sobely) # 2D 백터의 크기 계산
# mag2 = cv2.magnitude(sobelx2, sobely2)
sobel = cv2.normalize(mag, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U) # 정규화
# sobel2 = cv2.normalize(mag2, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)
cv2.imshow('d', sobel)
# cv2.imshow('d2', sobel2)

# e 소벨 필터 적용된 이미지를 평균 블러 처리, 5x5
# opencv 함수 이용
sobel_blur = cv2.blur(sobel, ksize=(5, 5))
cv2.imshow('e', sobel_blur)

# 직접 구현
avg_kernel = np.ones((5,5),np.float32)/25
sobel_blur2 = cv2.filter2D(sobel, -1, avg_kernel) # -1은 입력된 영상과 동일한 타입으로 출력
# cv2.imshow('e', sobel_blur)
# cv2.imshow('e2', sobel_blur2)

# f 
# 원본과 합칠 이미지 생성
# 라플라시안 필터와 소벨 필터로부터 얻은 이미지의 가중치를 곱하고 gamma를 더한다
mask = cv2.addWeighted(Mlaplacian, 0.5, sobel_blur, 0.5, -50)
cv2.imshow('f', mask)

# g 
# 원본과 필터 이미지 합치기
sharp = cv2.add(img, mask)
cv2.imshow('g', sharp)

# h
# power law 적용 공식: C * r**y
y = [0.5, 1.5, 2.5, 4.0] # 감마 값, 클 수록 어둡다, 낮을 수록 밝다
for i in range(len(y)):
    result = np.array(255*(sharp/255)**y[i], dtype='uint8') # dtype='uint8' 고정
    cv2.imshow(f'h{i}', result) # 개선된 이미지

result = np.array(255*(sharp/255)**y[1], dtype='uint8')
img_cal = cv2.calcHist(images=[img], channels=[0], mask=None, histSize=[64], ranges=[0, 256])
result_cal = cv2.calcHist(images=[result], channels=[0], mask=None, histSize=[64], ranges=[0, 256])

# 히스토그램 평활화
# 필터를 이용해 개선한 영상과 어떤 차이가 있는지 비교하기 위해서 사용함
# 칼라이미지를 사용할 경우 주석처리
hist = cv2.equalizeHist(img)
hist_cal = cv2.calcHist(images=[hist], channels=[0], mask=None, histSize=[64], ranges=[0, 256])

cv2.imshow('equalizeHist(a)', hist ) # 칼라 이미지일 경우 주석처리
cv2.imshow('h', result)

fig, ax = plt.subplots(1, 3, figsize=(10, 5))

ax[0].plot(img_cal, color='r')
ax[1].plot(hist_cal, color='b') # 칼라 이미지일 경우 주석 처리
ax[2].plot(result_cal, color='g') 
plt.show()

cv2.waitKey()
cv2.destroyAllWindows()