# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 14:23:32 2018
@author: Later
内容：
边缘检测(四种算子)
@from: https://blog.csdn.net/qq_33757398/article/details/89055245#1.%20Sobel%E7%AE%97%E5%AD%90
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage import measure, draw



img = cv2.imread('Test.png', cv2.IMREAD_GRAYSCALE)
# Sobel算子
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1)
sobelx = cv2.convertScaleAbs(sobelx)
sobely = cv2.convertScaleAbs(sobely)
sobelxy = cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0) # x+y=xy
# 显示图像
cv2.imshow('x', sobelx)
cv2.imshow('y', sobely)
cv2.imshow('xy', sobelxy)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Scharr算子
scharrx = cv2.Scharr(img, cv2.CV_64F, 1, 0)
scharry = cv2.Scharr(img, cv2.CV_64F, 0, 1)
scharrx = cv2.convertScaleAbs(scharrx)
scharry = cv2.convertScaleAbs(scharry)
scharrxy = cv2.addWeighted(scharrx, 0.5, scharry, 0.5, 0)
# 显示图像
cv2.imshow('x', sobelx)
cv2.imshow('y', sobely)
cv2.imshow('xy', sobelxy)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Laplacian算子
laplacian = cv2.Laplacian(img, cv2.CV_64F)
laplacian = cv2.convertScaleAbs(laplacian)
# 显示图像
cv2.imshow('laplacian', laplacian)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Candy算子-----貌似效果最好
canny = cv2.Canny(img, 50, 100)
# 显示图像
cv2.imshow('canny', canny)
cv2.waitKey(0)
cv2.destroyAllWindows()