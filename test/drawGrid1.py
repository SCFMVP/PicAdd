# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 14:23:32 2018
@author: Later
内容：
绘制网格
@from:
"""
import cv2
from PIL import Image,ImageDraw

img = cv2.imread('qq.png', cv2.IMREAD_GRAYSCALE)
# 显示图像尺寸信息
sp = img.shape
print(sp)
height = sp[0]
width = sp[1]
print(' width: %d \n height: %d \n' % (width, height))

# Candy算子-----貌似效果最好
canny = cv2.Canny(img, 50, 100)

# # 绘制网格PIL
# im = Image.open("qq.png")
# draw = ImageDraw.Draw(im)  # 实例化一个对象
# draw.line((0, 0) + im.size, fill=128, width=5)  # 线的起点和终点，线宽
# draw.line((0, im.size[1], im.size[0], 0), fill=128)
# draw.line((0, im.size[1]/2)+(im.size[0]/2, im.size[1]), fill=128, width=5)
# im.show()

# # 绘制直线CV2 : https://blog.csdn.net/u011520181/article/details/83999786
# # img = cv2.imread('qq.png', cv2.IMREAD_GRAYSCALE)
# ptStart = (0, 0)
# ptEnd = (256, 256)
# point_color = (66, 66, 66)  # BGR
# thickness = 3
# lineType = 4
# cv2.line(canny, ptStart, ptEnd, point_color, thickness, lineType)

point_color = (66, 66, 66)  # BGR
thickness = 1
lineType = 4
strSize = 5  # 字符size: strSize*strSie
# 绘制网格
for i in range(height//strSize):
    lineId = i*strSize
    ptStart = (0, lineId)  # 画横线
    ptEnd = (width, lineId)
    cv2.line(canny, ptStart, ptEnd, point_color, thickness, lineType)
for i in range(width//strSize):
    lineId = i*strSize
    ptStart = (lineId, 0)  # 画竖线
    ptEnd = (lineId, height)
    cv2.line(canny, ptStart, ptEnd, point_color, thickness, lineType)


# 显示图像
cv2.imshow('canny', canny)
cv2.waitKey(0)
cv2.destroyAllWindows()