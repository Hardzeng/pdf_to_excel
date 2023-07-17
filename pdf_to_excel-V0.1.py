import tkinter as tk
from tkinter import filedialog,simpledialog



def creat_surface():
#创建界面窗口函数

    root=tk.Tk()  #创建Tk()类的实例已经名为root的顶层窗口

    #创建大小为300*240 坐标x=200,y=200的窗口
    root.title("需求文件") #定义窗口名字为需求文件
    root.geometry('300x240+200+200') #窗口大小
    file_path=filedialog.askdirectory()
    print('文件路径为：',file_path)

    root.withdraw() #文件选取之后，隐藏tk主窗口

    keyword = simpledialog.askstring('','请输入分割关键词：',initialvalue='关键词')
    print('分割关键词为：',keyword)
    root.destroy()  #窗口执行完毕即结束销毁
    # root.mainloop() #窗口执行完毕不结束  需要按ctrl+c
    return(keyword)
print(keyword)

creat_surface()

