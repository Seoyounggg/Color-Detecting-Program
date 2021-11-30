# mask_generator.py
# 2016732047 / 홍서영
# 2018.11.28
# 컴퓨터언어 프로젝트

from tkinter.filedialog import *
from tkinter import *
from PIL import ImageTk, Image
import numpy as np
import cv2 as cv
import tkinter


# hsv_는 클릭한 픽셀의 hsv 값들이 저장될 리스트입니다.
hsv_ = []

# result는 저장될 이미지의 파일명입니다.
result = ''

# count는 사용자가 마우스를 클릭한 횟수를 저장하는 변수입니다.
count = 0

# path는 불러올 이미지의 위치입니다.
path = ''


# 윈도우의 상단에 있는 메뉴 중 파일 열기를 하는 함수입니다.
def func_open():

    global photo, img_color, filename, path, width, height

    try:
        filename = askopenfilename(parent=window, filetypes=(("JPG 파일", "*.jpg"), ("모든 파일", "*.*")))
        if filename != '':
            photo = ImageTk.PhotoImage(file=filename)
            path_ = filename.split('/')
            path = './'+path_[-2]+'/'+path_[-1]

            with Image.open(filename) as img:
                width, height = img.size

            #img_color는 사용자가 선택한 이미지 파일을 색으로 읽은 값을 numpy.ndarray로 저장한 변수입니다.
            img_color = cv.imread(path)

            # 윈도우의 좌측에 이미지 파일을 올리기위한 부분입니다.
            canvas.create_image(width // 2, height // 2, image=photo)
    except KeyError:
        pass


# 윈도우의 상단에 있는 메뉴 중 프로그램을 종료하는 함수입니다.
def func_exit():
    window.quit()
    window.destroy()


# 윈도우에서의 마우스 클릭 이벤트를 받아 클릭한 부분의 픽셀 값을 받아 mask 이미지를 생성하는 함수입니다.
def clickMouse(event):

    # txt는 윈도우에 몇 번 클릭했는지를 보여주는 변수입니다.
    txt = ""
    
    global hsv, img_mask, count, img_hsv, filename, result, path

    if path != '':

            # 마우스의 좌측 버튼을 클릭할 때마다 clickMouse 함수가 실행됩니다.
        if event.num == 1:

                # 3회 이상 클릭할 경우 클릭 횟수 초과하였다고 윈도우에 표시됩니다.
            if count >= 3:
                txt += "클릭 횟수 초과"
            else:
                    # 클릭할 때마다 count의 수가 증가하게 됩니다.
                count += 1

                    # 클릭된 이미지 부분의 픽셀 값을 color 라는 변수에 저장한 뒤 rgb 값을 hsv 값으로 변환시킵니다.
                color = img_color[event.y, event.x]
                one_pixel = np.array([[color]])
                hsv = cv.cvtColor(one_pixel, cv.COLOR_BGR2HSV)[0][0]

                    # hsv_ (리스트)에 해당 픽셀의 hsv 값을 저장합니다.
                hsv_.append(list(hsv))
                txt += str(count)+"회 클릭"

                    # 총 3개의 hsv값을 가지게 되면 mask_bound 함수를 실행시킵니다.
                if len(hsv_) == 3:
                    img_hsv = cv.cvtColor(img_color, cv.COLOR_BGR2HSV)
                    img_mask = mask_bound()
                    ''' 
                        filename은 사용자가 연 파일의 경로가 포함된 이름입니다.
                            따라서 파일명만 저장하기 위해 idx 변수를 이용하여 사용자가 선택한 파일명을 가져옵니다.
                    '''
                    idx = filename.rfind('/')
                        
                        # mask 이미지의 저장명은 result_'사용자가 선택한 파일명' 입니다.
                    result = 'result_' + filename[idx + 1:]
                    cv.imwrite(result, img_mask)
                else:
                    pass
            label1.configure(text=txt)


# mask_bound는 흰색과 검은색으로 구분되는 이미지를 만들어주는 함수입니다.
def mask_bound():
    global hsv_, img_hsv

    hsv_h = []
    hsv_s = []
    hsv_v = []

    if len(hsv_) == 3:
        for h, s, v in hsv_:

            # hsv_에 있는 각각의 h, s, v 값을 따로 hsv_h, hsv_s, hsv_v로 구분하여 저장합니다.
            hsv_h.append(h)
            hsv_s.append(s)
            hsv_v.append(v)

        # h,s,v 값들의 각각의 평균과 표준편차를 구합니다.
        h_mean = np.mean(hsv_h)
        h_std = np.std(hsv_h)
        s_mean = np.mean(hsv_s)
        s_std = np.std(hsv_s)
        v_mean = np.mean(hsv_v)
        v_std = np.std(hsv_v)

        # 경로로 볼 색의 하한값과 상한값을 각각 lower_color, upper_color로 저장합니다.
        lower_color = np.array([h_mean - 40*h_std, s_mean - 40*s_std, v_mean - 40*v_std])
        upper_color = np.array([h_mean + 40*h_std, s_mean + 40*s_std, v_mean + 40*v_std])

        # 이미지에서 하한값과 상한값 사이에 드는 부분은 모두 흰색으로 아닌 부분은 검은색으로 바꿔줍니다.
        img_mask = cv.inRange(img_hsv, lower_color, upper_color)
    return img_mask


# show는 3회 클릭 후 만들어진 mask 이미지를 윈도우의 우측에 보여주는 함수입니다.
def show():

    global result

    if result != "":
        photo_2 = ImageTk.PhotoImage(file=result)
        pLabel2.configure(image=photo_2)
        pLabel2.image = photo_2
    else:
        pass


# window라는 윈도우를 생성합니다.
window = Tk()
window.geometry("500x400")
window.title("Color Detecting Program")
label1 = Label(window, text="총 3회를 클릭하세요.")
label1.place(x=200, y=20)

# 윈도우의 우측에 클릭 결과 만들어진 이미지가 보일 위치를 지정합니다.
photo_2 = PhotoImage()
pLabel2 = Label(window, image=photo_2)
pLabel2.place(x=270, y=50)

# 마우스 왼쪽 버튼이 눌렸을 때 clickMouse 함수를 실행시키고 사용자가 선택한 이미지가 보일 위치를 지정합니다.
canvas = tkinter.Canvas(window, width=200, height=256)
canvas.place(x=20, y=50)
canvas.bind("<Button-1>", clickMouse)

# 'SHOW'라는 버튼을 누르면 윈도우의 우측에 클릭 결과 만들어진 이미지가 나타납니다.
button = Button(window, text = 'SHOW', command=show)
button.place(x=225, y=350)

# 윈도우의 상단에 파일이라는 상위 메뉴와 열기와 종료로 구성된 하위 메뉴를 만들어줍니다.
mainMenu = Menu(window)
window.config(menu=mainMenu)
fileMenu = Menu(mainMenu, tearoff=0)
mainMenu.add_cascade(label="파일", menu=fileMenu)
fileMenu.add_command(label="열기", command=func_open)
fileMenu.add_command(label="종료", command=func_exit)

window.mainloop()
