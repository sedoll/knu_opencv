Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # 201905153 오세훈
>>> # pca 투영, 역투영
>>> import cv2
>>> import numpy as np
>>> X = np.array([[0, 0, 0, 100, 100, 150, -100, -150],
	      [0, 50, -50, 0, 30, 100, -20, -100]], dtype=np.float64)
>>> X = X.T
>>> mean, eigan = cv2.PCACompute(X, None)
>>> print(mean)
[[12.5   1.25]]
>>> print(eigan)
[[ 0.88390424  0.46766793]
 [-0.46766793  0.88390424]]
>>> Y = cv2.PCABackProject(X, mean, eigan)
>>> print(Y)
[[  12.5           1.25      ]
 [ -10.88339659   45.445212  ]
 [  35.88339659  -42.945212  ]
 [ 100.890424     48.01679318]
 [  86.86038605   74.53392038]
 [  98.31884282  159.79061378]
 [ -66.53706537  -63.19487798]
 [ -73.31884282 -157.29061378]]
>>> print(np.round(Y))
[[  12.    1.]
 [ -11.   45.]
 [  36.  -43.]
 [ 101.   48.]
 [  87.   75.]
 [  98.  160.]
 [ -67.  -63.]
 [ -73. -157.]]
>>> X2 = cv2.PCAProject(Y, mean, eigan)
>>> print(np.round(X2))
[[   0.    0.]
 [   0.   50.]
 [   0.  -50.]
 [ 100.    0.]
 [ 100.   30.]
 [ 150.  100.]
 [-100.  -20.]
 [-150. -100.]]
>>> np.allclose(X, X2)
True
>>> error = np.sqrt(np.sum((X-X2)**2))
>>> print(error)
6.194367960490402e-14
>>> X2 = X2.T
>>> print(X2)
[[   0.    0.    0.  100.  100.  150. -100. -150.]
 [   0.   50.  -50.    0.   30.  100.  -20. -100.]]
>>> error = np.sqrt(np.sum((X-X2)**2))
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    error = np.sqrt(np.sum((X-X2)**2))
ValueError: operands could not be broadcast together with shapes (8,2) (2,8) 
>>> X2 = X2.Y
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    X2 = X2.Y
AttributeError: 'numpy.ndarray' object has no attribute 'Y'
>>> X2 = X2.T
>>> # 역투영을 이용한 근사치
>>> k=1
>>> vk = eigan.copy()
>>> vk = [k:, :] = 0
SyntaxError: invalid syntax
>>> vk[k:, :] = 0
>>> xY = cv2.PCAProject(X, mean, eigan)
>>> Y = cv2.PCAProject(X, mean, eigan)
>>> xk = cv2.PCABackProject(Y, mean, vk)
>>> print(xk)
[[   2.2171991    -4.19056247]
 [  22.88588249    6.74510226]
 [ -18.4514843   -15.12622719]
 [  80.34586965   37.14680432]
 [  92.74707969   43.70820315]
 [ 160.74757171   79.68681716]
 [ -84.17894482  -49.90219514]
 [-156.31317352  -88.06794209]]
>>> print(np.round(xk))
[[   2.   -4.]
 [  23.    7.]
 [ -18.  -15.]
 [  80.   37.]
 [  93.   44.]
 [ 161.   80.]
 [ -84.  -50.]
 [-156.  -88.]]
>>> error = np.sqrt(np.sum((X-xk)**2))
>>> print(error)
88.51760505419699
>>> 