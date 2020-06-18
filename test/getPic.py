import cv2
import numpy as np

# 两种图片读取方式:绝对路径,相对路径
# img = cv2.imread('E:\PycharmProjects\PicAdd\\test\key.jpg', 0)
img = cv2.imread('wx.png')  # 尾部加0则显示黑白

# 显示图像尺寸信息
sp = img.shape
print(sp)
height = sp[0]
width = sp[1]
print('width: %d \n height: %d \n' % (width, height))

# 显示图片
cv2.namedWindow('Image', 0)
cv2.resizeWindow('Image', width, height)
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
