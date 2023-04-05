# result4 까지 맞음

import cv2
import numpy as np

# 이미지 불러오기
img = cv2.imread('c:/data/lena.jpg', cv2.IMREAD_GRAYSCALE)
blur_g = cv2.GaussianBlur(img, ksize=(3, 3), sigmaX=1.0)

# 라플라시안 필터 적용
laplacian = cv2.Laplacian(blur_g, cv2.CV_8U)
laplacian = cv2.convertScaleAbs(laplacian)
laplacian = cv2.normalize(laplacian, None, 0, 255, cv2.NORM_MINMAX)
Mlaplacian = cv2.subtract(img, laplacian) # 원본에서 라플라시안 필터 값을 뺀 이미지

# 소벨 필터 적용
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
mag = cv2.magnitude(sobelx, sobely) # 2D 백터의 크기 계산
sobel = cv2.normalize(mag, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)
sobel = cv2.GaussianBlur(sobel, ksize=(5, 5), sigmaX=1.0)

# 라플라시안 필터와 소벨 필터로부터 얻은 이미지를 합치기
result = cv2.addWeighted(Mlaplacian, 0.5, sobel, 0.5, 0)

# 임계값(threshold) 이하인 부분을 0으로 만들기
thresh = 60  # 임계값(threshold) 설정
_, result2 = cv2.threshold(result, thresh, 255, cv2.THRESH_TOZERO)

# result3
result3 = cv2.addWeighted(img, 1.0, result2, 0.5, 0)

# 23.04.05현재 result3 까지 맞게 함
# result4 / result3 이미지를 받아서 어두운 부분을 조금 밝게 하도록 조정해보기

# 결과 출력
cv2.imshow('src', img)
cv2.imshow('lap', laplacian)
cv2.imshow('Mlap', Mlaplacian)
cv2.imshow('sobel', sobel)
cv2.imshow('result1', result)
cv2.imshow('Result2', result2)
cv2.imshow('result3', result3)
# cv2.imshow('result4', result4)
cv2.waitKey(0)
cv2.destroyAllWindows()