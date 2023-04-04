# 참고
# https://www.youtube.com/watch?v=5l0y-LMM1c0&ab_channel=MadePython
# 23.04.04 e 단계 까지는 맞게 함

import cv2
import numpy as np

src = cv2.imread('c:/data/bone_test.png', cv2.IMREAD_GRAYSCALE)
# src = cv2.imread('c:/data/lena.jpg', cv2.IMREAD_GRAYSCALE)
src = cv2.resize(src, (300, 400))
blur_g = cv2.GaussianBlur(src, ksize=(3, 3), sigmaX=1.0)
cv2.imshow('src', src)
cv2.imshow('blur_g', blur_g)

# a
# 라플라시안
# 블러 처리 후 적용하는 이유는 미분을 하면 잡음이 증폭되기에 잡음을 감소기키기 위함이다.
lap = cv2.Laplacian(blur_g, cv2.CV_8U) # 블러 처리 후 라플라시안 적용
# cv2.imshow('lap', lap)

# b
# 정규화
dst_l = cv2.convertScaleAbs(lap) # 각각의 값을 절대값화시키고 정수화 시키는 작업
dst_l = cv2.normalize(dst_l, None, 0, 255, cv2.NORM_MINMAX)

# c
dst_l = cv2.subtract(src, dst_l) # 원본에서 라플라시안 필터 값을 뺀 이미지
cv2.imshow('dst_l', dst_l)

# d
# 소벨
# gx, gy 계산
gx = cv2.Sobel(src, cv2.CV_32F, 1, 0, ksize=3) # x에 대한 미분
gy = cv2.Sobel(src, cv2.CV_32F, 0, 1, ksize=3) # y에 대한 미분

# x방향 미분과 y방향 미분을 따로 계산하고 벡터라는 것으로 묶은 것이 그래디언트
mag = cv2.magnitude(gx, gy) # 2D 백터의 크기 계산
dst_s = cv2.normalize(mag, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U) # 정규화
cv2.imshow('dst_s', dst_s)

# e
blur_s = cv2.GaussianBlur(dst_s, ksize=(5, 5), sigmaX=1.0)
cv2.imshow('blur_s', blur_s)

# f
dst_ls = cv2.multiply(dst_l, blur_s)

ret_l, dlt = cv2.threshold(dst_l, 50, 255, cv2.THRESH_TOZERO)
ret_s, bst = cv2.threshold(blur_s, 50, 255, cv2.THRESH_TOZERO)
dst_ls = cv2.multiply(bst, dlt)
# dst_ls = cv2.equalizeHist(dst_ls)///

# result = cv2.addWeighted(dst_ls, 0.5, src, 0.5, 0)
# result = cv2.normalize(result, None, 200, 255, cv2.NORM_MINMAX, dtype=-1)
# result = cv2.equalizeHist(dst_ls)
cv2.imshow('dst_ls', dst_ls)
# cv2.imshow('result', result)

cv2.waitKey()
cv2.destroyAllWindows()


