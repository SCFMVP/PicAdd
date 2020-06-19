# -*- coding: utf-8 -*-

import tkinter as tk  # 使用Tkinter前需要先导入

# 第1步，实例化object，建立窗口window
from tkinter import filedialog

import cv2

window = tk.Tk()
# 第2步，给窗口的可视化起名字
window.title('图形识别填充 V1.0')
# 第3步，设定窗口的大小(长 * 宽)
window.geometry('500x800')  # 这里的乘是小x   wigth * height
window.configure(bg='#696969')

# 回调函数
def hit_me():
    lb1.pack()


def get_picPath(event):
    Filepath = filedialog.askopenfilename()  # 获得选择好的文件
    print('Filepath:', Filepath)


'''
绘制控件布局
'''
# ==================选择图片=================
# 提示标签
lb1 = tk.Label(window,  text='选择图片:', bg='#696969', fg='white', font=('Arial', 10), width=30, height=2)
# lb1.pack()
# 选择图片画布
canvas1 = tk.Canvas(window, bg='#696969',  width=200, height=200)
canvas1.bind("<B1-Motion>", get_picPath)
image_file1 = tk.PhotoImage(file='qq.png')    # jpg显示貌似有问题
# todo: 图像比例, jpg格式问题
image = canvas1.create_image(0, 0, anchor='nw', image=image_file1)
# canvas1.pack()
lb1.grid(row=0, column=0)
canvas1.grid(row=1, column=0)
# ==================输入字符=================
# 提示标签
lb2 = tk.Label(window, text='填充内容:', bg='#696969',  fg='white', font=('Arial', 10))
# lb2.pack()
# 字符输入框
eStr = tk.Text(window, show=None, bg='#696969', fg='white',  font=('Arial', 8), height=14, width=40)   # 显示成密文形式
# eStr.pack()
lb2.grid(row=0, column=1)
eStr.grid(row=1, column=1)
# ==================确定轮廓=================
# 提示标签
lb3 = tk.Label(window, text='确定轮廓:', bg='#696969',  fg='white', font=('Arial', 10), width=30, height=2)
# lb3.pack()
# 轮廓画布
canvas2 = tk.Canvas(window, bg='#696969',  width=200, height=200)
image_file2 = tk.PhotoImage(file='qq.png')    # jpg显示貌似有问题
image = canvas2.create_image(0, 0, anchor='nw', image=image_file2)
# canvas2.pack()
lb3.grid(row=2, column=0)
canvas2.grid(row=3, column=0)
# ==================设置像素=================
lb4 = tk.Label(window, text='像素设置:', bg='#696969',  fg='white', font=('Arial', 10), width=30, height=2)
# lb4.pack()
lb4.grid(row=2, column=1)
# ==================设置颜色=================
lb5 = tk.Label(window, text='颜色设置:', bg='#696969',  fg='white', font=('Arial', 10), width=30, height=2)
# lb5.pack()
lb5.grid(row=3, column=1)
# ==================填充字符=================
# 提示文字
lb6 = tk.Label(window, text='生成结果:', bg='#696969',  fg='white', font=('Arial', 10), width=30, height=2)
# lb6.pack()
# 按钮
b = tk.Button(window, text='生成', font=('Arial', 12), width=10, height=1, command=hit_me)
# b.pack()
# b.grid(row=1, column=2, padx=10, pady=10, ipadx=10, ipady=10)
# 结果画布
canvas3 = tk.Canvas(window, bg='#696969',  width=200, height=200)
image_file3 = tk.PhotoImage(file='wx.png')    # jpg显示貌似有问题
image = canvas3.create_image(0, 0, anchor='nw', image=image_file3)
# canvas3.pack()
lb6.grid(row=4, column=0)
b.grid(row=4, column=1)
canvas3.grid(row=5, column=0)

# 第6步，主窗口循环显示
window.mainloop()
