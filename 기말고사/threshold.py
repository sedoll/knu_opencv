Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # 201905153 오세훈
>>> # threshold
>>> import cv2
>>> import numpy as np
>>> src = cv2.imread(c:/data/heart10.jpg, cv2.IMREAD_GRAYSCALE)
SyntaxError: invalid syntax
>>> src = cv2.imread('c:/data/heart10.jpg', cv2.IMREAD_GRAYSCALE)
>>> cv2.imshow('src
	   
SyntaxError: EOL while scanning string literal
>>> cv2.imshow('src', src)
>>> ret, dst = cv2.threshold(src, 128, 255, cv2.THRESH_BINARY)
>>> cv2.imshow('dst2', dst)
>>> ret, dst = cv2.threshold(src, 150, 255, cv2.THRESH_BINARY)
>>> cv2.imshow('dst2', dst)
>>> ret, dst = cv2.threshold(src, 150, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
>>> cv2.imshow('dst3', dst)
>>> ret, dst = cv2.threshold(src, 120, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
>>> cv2.imshow('dst3', dst)
>>> # 적응형 임계값
>>> import cv2
>>> import numpy as np
>>> rc = cv2.imread(c:/data/srcThreshold.jpg, cv2.IMREAD_GRAYSCALE)
SyntaxError: invalid syntax
>>> src = cv2.imread('c:/data/srcThreshold.jpg', cv2.IMREAD_GRAYSCALE)
>>> cv2.imshow('src', src)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    cv2.imshow('src', src)
cv2.error: OpenCV(4.7.0) D:\a\opencv-python\opencv-python\opencv\modules\highgui\src\window.cpp:971: error: (-215:Assertion failed) size.width>0 && size.height>0 in function 'cv::imshow'

>>> src = cv2.imread('c:/data/srcThreshold.png', cv2.IMREAD_GRAYSCALE)
>>> cv2.imshow('src', src)
>>> ret, dst = cv2.threshold(src, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
>>> cv2.imshow('dst', dst)
>>> dst2 = cv2.adaptiveThreshold(src, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_, 51, 7)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    dst2 = cv2.adaptiveThreshold(src, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_, 51, 7)
AttributeError: module 'cv2' has no attribute 'THRESH_'
>>> dst2 = cv2.adaptiveThreshold(src, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 51, 7)
>>> cv2.imshow('dst2', dst2)
>>> 