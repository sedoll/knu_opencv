Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # canny
>>> import cv2
>>> src = cv2.imread('c:/data/lena.jpg', cv2.IMREAD_GRAYSACLE)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    src = cv2.imread('c:/data/lena.jpg', cv2.IMREAD_GRAYSACLE)
AttributeError: module 'cv2' has no attribute 'IMREAD_GRAYSACLE'
>>> edges1 = cv2.Canny('edges1', edges1)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    edges1 = cv2.Canny('edges1', edges1)
NameError: name 'edges1' is not defined
>>> edges1 = cv2.Canny(src, 50, 100)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    edges1 = cv2.Canny(src, 50, 100)
NameError: name 'src' is not defined
>>> src = cv2.imread('c:/data/lena.jpg', cv2.IMREAD_GRAYSACLE)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    src = cv2.imread('c:/data/lena.jpg', cv2.IMREAD_GRAYSACLE)
AttributeError: module 'cv2' has no attribute 'IMREAD_GRAYSACLE'
>>> src = cv2.imread('c:/data/lena.jpg')
>>> gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
>>> edges1 = cv2.Canny(gray, 50, 100)
>>> edges2=  c2.Canny(gray, 50, 200)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    edges2=  c2.Canny(gray, 50, 200)
NameError: name 'c2' is not defined
>>> edges2=  cv2.Canny(gray, 50, 200)
>>> cv2.imshow(edges1)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    cv2.imshow(edges1)
cv2.error: OpenCV(4.7.0) :-1: error: (-5:Bad argument) in function 'imshow'
> Overload resolution failed:
>  - imshow() missing required argument 'mat' (pos 2)
>  - imshow() missing required argument 'mat' (pos 2)
>  - imshow() missing required argument 'mat' (pos 2)

>>> cv2.imshow('edges1', edges1)
>>> cv2.imshow('edges2', edges2)
>>> 