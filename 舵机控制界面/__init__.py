"""
    标题：机械臂界面
    时间：2020.02.15
    作者：Sunqk
"""
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
import tkinter.font as tkFont

def tkimg_resized(img, w_box, h_box, keep_ratio=True):
	"""对图片进行按比例缩放处理"""
	w, h = img.size

	if keep_ratio:
		if w > h:
			width = w_box
			height = int(h_box * (1.0 * h / w))

		if h >= w:
			height = h_box
			width = int(w_box * (1.0 * w / h))
	else:
		width = w_box
		height = h_box

	img1 = img.resize((width, height), Image.ANTIALIAS)
	tkimg = ImageTk.PhotoImage(img1)
	return tkimg
def image_label(frame, img, width, height, keep_ratio=True):
	"""输入图片信息，及尺寸，返回界面组件"""
	if isinstance(img, str):
		_img = Image.open(img)
	else:
		_img = img
	lbl_image = tk.Label(frame, width=width, height=height)

	tk_img = tkimg_resized(_img, width, height, keep_ratio)
	lbl_image.image = tk_img
	lbl_image.config(image=tk_img)
	return lbl_image


def show_confirm(message=""):
	"""
		True  : yes
		False : no
	"""
	return messagebox.askyesno("确认框", message)



a=None
def main():
    window = tk.Tk()                        # 创建窗口
    window.geometry("700x400")              # 窗体尺寸设置
    window.iconbitmap("Money.ico")          # 窗体左上角图标设置
    window.title("机械臂抓取控制界面")
    window.resizable(True, True)            # 设置窗体不可改变大小

    #背景图选择并放置
    img=ImageTk.PhotoImage(file="bg1.png")
    canvas = tk.Canvas(window, width=1000, height=800)
    canvas.create_image(300, 200, image=img)
    canvas.pack(expand=tk.YES, fill=tk.BOTH)

    def show_title(self):                     #窗口边框消失、复原函数
        global a
        a=not a
        window.overrideredirect(a)
    def close(self):                          #窗口退出函数
        if show_confirm("确认退出吗 ?"):
            window.quit()


    #**************************标题设置开始处*****************************
    f1 = tk.Frame(canvas)
    #图像按钮 1
    im1 = image_label(f1, "laugh.jpg", 86, 86, False)
    im1.configure(bg="Teal")
    im1.bind('<Button-1>',show_title)
    im1.pack(side=tk.LEFT, anchor=tk.NW, fill=tk.Y)
    #标题背景、字体......
    ft1 = tkFont.Font(family="微软雅黑", size=24, weight=tkFont.BOLD)
    tk.Label(f1, text="欢迎来到机械臂控制界面", height=2, fg="white", font=ft1, bg="Teal") \
        .pack(side=tk.LEFT, expand=tk.YES, fill=tk.X)
    #图像按钮 2
    im2 = image_label(f1, "close.png", 86, 86, False)
    im2.configure(bg="Teal")
    im2.bind('<Button-1>',close)
    im2.pack(side=tk.RIGHT, anchor=tk.NW, fill=tk.Y)

    f1.pack(fill=tk.X)
    #**************************标题设置结束*****************************

# ---------------------------------------------------------------------
# 两个功能按钮组的设置
# ---------------------------------------------------------------------

    # ‘手动抓取’和‘自动抓取’功能按钮所调用的函数
    def shou_dong():
        Wd_1()
    def zi_dong():
        Wd_2()
    # 子窗口一
    def Wd_1():
        Wd=tk.Toplevel()
        Wd.geometry("%dx%d" % (800,620))        # 窗体尺寸
        Wd.title("手动抓取界面")                 # 窗体标题
        Wd.grab_set()
        Wd.resizable(True, True)

        frame = tk.Frame(Wd, height=20,bg="Goldenrod")
        ft0 = tkFont.Font(family="微软雅黑", size=18, weight=tkFont.BOLD)
        tk.Label(frame, font=ft0, bg="Chocolate", fg="white", text="请手动调控机械臂的各个舵机参数") \
            .pack(padx=20)
        frame.pack(fill=tk.X)

        ft1 = tkFont.Font(family="微软雅黑", size=12, weight=tkFont.BOLD)
        ft2 = tkFont.Font(family="微软雅黑", size=14, weight=tkFont.BOLD)

        #右边绿框(画布形式)
        canvas = tk.Canvas(frame, bg='green', height=238, width=450)
        # 定义多边形参数，然后在画布上画出指定图形
        x0, y0, x1, y1 = 100, 100, 150, 150
        line = canvas.create_line(x0 - 50, y0 - 50, x1 - 50, y1 - 50)  # 画直线
        oval = canvas.create_oval(x0 + 120, y0 + 50, x1 + 120, y1 + 50, fill='yellow')  # 画圆 用黄色填充
        arc = canvas.create_arc(50, 150, 100, 200, start=0, extent=180,fill='red')  # 画扇形 从0度打开收到180度结束
        rect = canvas.create_rectangle(330, 30, 330 + 20, 30 + 20,fill='blue')  # 画矩形正方形
        triangle = canvas.create_polygon(208,135,222,43,268,95,fill='DeepPink')

        canvas.pack(side=tk.RIGHT,anchor=tk.N)


        #舵机一框区
        v_1 = tk.StringVar()
        v_2 = tk.StringVar()
        v_3 = tk.StringVar()
        v_4 = tk.StringVar()
        v_5 = tk.StringVar()
        v_6 = tk.StringVar()

        f_dj1 = tk.Frame(frame)
        tk.Label(f_dj1, font=ft2, text="一号舵机:").pack(side=tk.LEFT, anchor=tk.W, padx=10)
        f_dj1.pack(fill=tk.Y, anchor=tk.W, pady=5)
        p_dj1 = tk.Spinbox(f_dj1, from_=0, to=300, width=19,textvariable=v_1, font=ft1)
        p_dj1.pack(side=tk.LEFT, padx=10)
        # 舵机二框区
        f_dj2 = tk.Frame(frame)
        tk.Label(f_dj2, font=ft2, text="二号舵机:").pack(side=tk.LEFT, anchor=tk.W, padx=10)
        f_dj2.pack(fill=tk.Y, anchor=tk.W, pady=5)
        p_dj2 = tk.Spinbox(f_dj2, from_=0, to=300, width=19,textvariable=v_2, font=ft1)
        p_dj2.pack(side=tk.LEFT, padx=10)
        # 舵机三框区
        f_dj3 = tk.Frame(frame)
        tk.Label(f_dj3, font=ft2, text="三号舵机:").pack(side=tk.LEFT, anchor=tk.W, padx=10)
        f_dj3.pack(fill=tk.Y, anchor=tk.W, pady=5)
        p_dj3 = tk.Spinbox(f_dj3, from_=0, to=300, width=19,textvariable=v_3, font=ft1)
        p_dj3.pack(side=tk.LEFT, padx=10)
        # 舵机四框区
        f_dj4 = tk.Frame(frame)
        tk.Label(f_dj4, font=ft2, text="四号舵机:").pack(side=tk.LEFT, anchor=tk.W, padx=10)
        f_dj4.pack(fill=tk.Y, anchor=tk.W, pady=5)
        p_dj4 = tk.Spinbox(f_dj4, from_=0, to=300, width=19,textvariable=v_4, font=ft1)
        p_dj4.pack(side=tk.LEFT, padx=10)
        # 舵机五框区
        f_dj5 = tk.Frame(frame)
        tk.Label(f_dj5, font=ft2, text="五号舵机:").pack(side=tk.LEFT, anchor=tk.W, padx=10)
        f_dj5.pack(fill=tk.Y, anchor=tk.W, pady=5)
        p_dj5 = tk.Spinbox(f_dj5, from_=0, to=300, width=19,textvariable=v_5, font=ft1)
        p_dj5.pack(side=tk.LEFT, padx=10)
        # 舵机六框区
        f_dj6 = tk.Frame(frame)
        tk.Label(f_dj6, font=ft2, text="六号舵机:").pack(side=tk.LEFT, anchor=tk.W, padx=10)
        f_dj6.pack(fill=tk.Y, anchor=tk.W, pady=5)
        p_dj6 = tk.Spinbox(f_dj6, from_=0, to=300, width=19,textvariable=v_6, font=ft1)
        p_dj6.pack(side=tk.LEFT, padx=10)


        #---------------------------彩虹边框------------------------------------
        tk.Frame(Wd, width=25, bg="OrangeRed").pack(side=tk.LEFT, fill=tk.Y)
        tk.Frame(Wd, height=25, bg="OrangeRed").pack(side=tk.TOP, fill=tk.X)
        tk.Frame(Wd, height=25, bg="OrangeRed").pack(side=tk.BOTTOM, fill=tk.X)
        tk.Frame(Wd, width=25, bg="OrangeRed").pack(side=tk.RIGHT, fill=tk.Y)

        tk.Frame(Wd, width=25, bg="Orange").pack(side=tk.LEFT, fill=tk.Y)
        tk.Frame(Wd, height=25, bg="Orange").pack(side=tk.TOP, fill=tk.X)
        tk.Frame(Wd, height=25, bg="Orange").pack(side=tk.BOTTOM, fill=tk.X)
        tk.Frame(Wd, width=25, bg="Orange").pack(side=tk.RIGHT, fill=tk.Y)

        tk.Frame(Wd, width=25, bg="Gold").pack(side=tk.LEFT, fill=tk.Y)
        tk.Frame(Wd, height=25, bg="Gold").pack(side=tk.TOP, fill=tk.X)
        tk.Frame(Wd, height=25, bg="Gold").pack(side=tk.BOTTOM, fill=tk.X)
        tk.Frame(Wd, width=25, bg="Gold").pack(side=tk.RIGHT, fill=tk.Y)

        tk.Frame(Wd, width=25, bg="Yellow").pack(side=tk.LEFT, fill=tk.Y)
        tk.Frame(Wd, height=25, bg="Yellow").pack(side=tk.TOP, fill=tk.X)
        tk.Frame(Wd, height=25, bg="Yellow").pack(side=tk.BOTTOM, fill=tk.X)
        tk.Frame(Wd, width=25, bg="Yellow").pack(side=tk.RIGHT, fill=tk.Y)

        tk.Frame(Wd, width=25, bg="GreenYellow").pack(side=tk.LEFT, fill=tk.Y)
        tk.Frame(Wd, height=25,bg="GreenYellow").pack(side=tk.TOP, fill=tk.X)
        tk.Frame(Wd, height=25, bg="GreenYellow").pack(side=tk.BOTTOM, fill=tk.X)
        tk.Frame(Wd, width=25, bg="GreenYellow").pack(side=tk.RIGHT, fill=tk.Y)

        tk.Frame(Wd, width=65, bg="Cyan").pack(side=tk.LEFT, fill=tk.Y)
        tk.Frame(Wd, height=20, bg="Cyan").pack(side=tk.TOP, fill=tk.X)
        tk.Frame(Wd, height=20, bg="Cyan").pack(side=tk.BOTTOM, fill=tk.X)
        tk.Frame(Wd, width=65, bg="Cyan").pack(side=tk.RIGHT, fill=tk.Y)
        #-------------------------------------------------------------------------

        Bt=tk.Canvas(Wd,bg="Cyan")
        Bt.pack(side=tk.TOP, padx=0, pady=0)
        def reset():
            v_1.set("0")
            v_2.set("0")
            v_3.set("0")
            v_4.set("0")
            v_5.set("0")
            v_6.set("0")

        tk.Button(Bt,text='复位', width=15, height=1, bg="MediumPurple", font=ft2,command=reset)\
            .pack(padx=10,anchor=tk.W,side=tk.LEFT)
        tk.Button(Bt, text='应用', width=15, height=1, bg="MediumPurple", font=ft2, command=reset) \
            .pack(padx=10, anchor=tk.W, side=tk.RIGHT)


    def Wd_2():
        Wd = tk.Toplevel()
        Wd.geometry("%dx%d" % (800, 620))  # 窗体尺寸
        Wd.title("手动抓取界面")  # 窗体标题
        Wd.grab_set()
        Wd.resizable(True, True)

        frame = tk.Frame(Wd, height=20, bg="Bisque")
        ft0 = tkFont.Font(family="微软雅黑", size=18, weight=tkFont.BOLD)
        tk.Label(frame, font=ft0, bg="Khaki", fg="black", text="请自动调控机械臂参数") \
            .pack(padx=20)
        frame.pack(fill=tk.X)


    #**********主界面按钮设置*************
    ft2 = tkFont.Font(family="微软雅黑", size=14, weight=tkFont.BOLD)
    tk.Button(canvas, text="手动抓取", bg="cadetblue", command=shou_dong, font=ft2, height=2, fg="white", width=15) \
        .pack(side=tk.LEFT, expand=tk.YES, anchor=tk.CENTER, padx=5)
    tk.Button(canvas, text="自动抓取", bg="cadetblue", command=zi_dong, font=ft2, height=2, fg="white", width=15) \
        .pack(side=tk.RIGHT, expand=tk.YES, anchor=tk.CENTER, padx=5)
    #********************************
    window.mainloop()
    #window.body()  # 调用body()函数
if __name__ == '__main__':
    main()