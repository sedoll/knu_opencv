Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # 0714 kmeans
>>> import cv2
>>> import numpy as np
>>> src = cv2.imread('c:/data/hand.jpg')
>>> hsv = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
>>> data = src.resahpe((-1, 3)).astype(np.float32)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    data = src.resahpe((-1, 3)).astype(np.float32)
AttributeError: 'numpy.ndarray' object has no attribute 'resahpe'
>>> data = src.reshape((-1, 3)).astype(np.float32)
>>> K=2
>>> term_crit=(cv2.TERM_CRITERIA_EPS+cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
>>> ret, labels, centers = cv2.kmeans(dtat, K, None, term_crit, 5, cv2.KMEANS_RANDOM_CENTERS)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    ret, labels, centers = cv2.kmeans(dtat, K, None, term_crit, 5, cv2.KMEANS_RANDOM_CENTERS)
NameError: name 'dtat' is not defined
>>> ret, labels, centers = cv2.kmeans(data, K, None, term_crit, 5, cv2.KMEANS_RANDOM_CENTERS)
>>> print(centers.shape)
(2, 3)
>>> print(labels.shape)
(230400, 1)
>>> print(ret)
62989312.60092831
>>> centers = np.uint8(centers)
>>> res = centers[labels.flatten()]
>>> dst = res.reshape(src.shape)
>>> cv2.imshow('dst', dst)
>>> # 7.15 레이블링
>>> 
>>> import cv2
>>> import numpy as np
>>> src = cv2.imread('c:/data/circles.jpg')
>>> gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
>>> ret, res = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY_INV)
>>> ret, labels = cv2.connectedComponents(res)
>>> print(ret)
4
>>> dst = np.zeros(src.shape, dtype=src.dtype)
>>> for i in range(1, ret):
	r = np.random.randint(256)
	g = np.random.randint(256)
	b = np.random.randint(256)
	dst[labels==i] = [b, g, r]

	
>>> cv2.imshow('res', res)
>>> cv2.imshow('dst', dst)
>>> cv2.imshow('dst', dst)
>>> cv2.imshow('dst', dst)
>>> # 7.16 레이블링
>>> import cv2
>>> import numpy as np
>>> src = cv2.imread('c:/data/circles.jpg')
>>> gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
>>> ret, res = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY_INV)
>>> ret, labels, stats, centroids = cv2.connectedComponentsWithStats(res)
>>> print(ret)
4
>>> print(labels)
[[0 0 0 ... 0 0 0]
 [0 0 0 ... 0 0 0]
 [0 0 0 ... 0 0 0]
 ...
 [0 0 0 ... 0 0 0]
 [0 0 0 ... 0 0 0]
 [0 0 0 ... 0 0 0]]
>>> print(stats)
[[     0      0    512    512 222719]
 [   308     86    125    125  12281]
 [   153    145    152    152  18152]
 [   292    338    107    107   8992]]
>>> print(centroids)
[[247.77339607 258.80937863]
 [370.         148.        ]
 [228.5        220.50534376]
 [345.00077847 390.99477313]]
>>> dst = np.zeros(src.shape, dtype=src.dtype)
>>> for i in range(1, int(ret)):
	r = np.random.randint(256)
	g = np.random.randint(256)
	b = np.random.randint(256)
	dst[labels==i] = [b, g, r]

	
>>> for i in range(1, int(ret)):
	x, y, width, height, area = stats[i]
	cv2.rectangle(dst, (x, y), (x+width, y+height), (0, 0, 255), 2)
	cx, cy = centroids[i]
	cv2.circle(dst, (int(cx), int(cy)), 5, (255, 0, 0), -1)

	
array([[[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        ...,
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]],

       [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        ...,
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]],

       [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        ...,
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]],

       ...,

       [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        ...,
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]],

       [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        ...,
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]],

       [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        ...,
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]], dtype=uint8)
array([[[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        ...,
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]],

       [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        ...,
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]],

       [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        ...,
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]],

       ...,

       [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        ...,
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]],

       [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        ...,
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]],

       [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        ...,
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]], dtype=uint8)
array([[[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        ...,
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]],

       [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        ...,
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]],

       [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        ...,
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]],

       ...,

       [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        ...,
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]],

       [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        ...,
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]],

       [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        ...,
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]], dtype=uint8)
array([[[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        ...,
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]],

       [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        ...,
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]],

       [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        ...,
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]],

       ...,

       [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        ...,
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]],

       [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        ...,
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]],

       [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        ...,
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]], dtype=uint8)
array([[[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        ...,
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]],

       [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        ...,
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]],

       [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        ...,
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]],

       ...,

       [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        ...,
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]],

       [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        ...,
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]],

       [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        ...,
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]], dtype=uint8)
array([[[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        ...,
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]],

       [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        ...,
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]],

       [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        ...,
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]],

       ...,

       [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        ...,
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]],

       [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        ...,
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]],

       [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        ...,
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]], dtype=uint8)
>>> cv2.imshow('src', src)
>>> cv2.imshow('dst', dst)
>>> cv2.imshow('src', src)
>>> 