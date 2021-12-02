# mask_generator.py
# 11.28.2018
# Project for "Computer Language" course

from tkinter.filedialog import *
from tkinter import *
from PIL import ImageTk, Image
import numpy as np
import cv2 as cv
import tkinter

hsv_ = []
result = ''
count = 0
path = ''

def func_open():
    global photo, img_color, filename, path, width, height
    try:
        filename = askopenfilename(parent=window, filetypes=(("JPG file", "*.jpg"), ("All files", "*.*")))
        if filename != '':
            photo = ImageTk.PhotoImage(file=filename)
            path_ = filename.split('/')
            path = './'+path_[-2]+'/'+path_[-1]

            with Image.open(filename) as img:
                width, height = img.size

            # read the selected image
            img_color = cv.imread(path)

            # locate the image file on the left side of the window
            canvas.create_image(width // 2, height // 2, image=photo)
    except KeyError:
        pass

def func_exit():
    window.quit()
    window.destroy()

def clickMouse(event):
    # txt shows how many times the user clicked the image on window.
    txt = ""
    global hsv, img_mask, count, img_hsv, filename, result, path

    if path != '':
        if event.num == 1:
            if count >= 3:
                txt += "Exceeded the number of allowed clicks"
            else:
                count += 1
                color = img_color[event.y, event.x]
                one_pixel = np.array([[color]])

                # convert the RGB value into HSV value
                hsv = cv.cvtColor(one_pixel, cv.COLOR_BGR2HSV)[0][0]
                hsv_.append(list(hsv))
                txt += "You have clicked "+str(count)+"time(s)"

                if len(hsv_) == 3:
                    img_hsv = cv.cvtColor(img_color, cv.COLOR_BGR2HSV)
                    img_mask = mask_bound()

                    idx = filename.rfind('/')

                    # the filename of the masked image is result_ + the name of the selected file
                    result = 'result_' + filename[idx + 1:]
                    cv.imwrite(result, img_mask)
                else:
                    pass
            label1.configure(text=txt)

def mask_bound():
    global hsv_, img_hsv
    hsv_h = []
    hsv_s = []
    hsv_v = []

    if len(hsv_) == 3:
        for h, s, v in hsv_:
            hsv_h.append(h)
            hsv_s.append(s)
            hsv_v.append(v)
        h_mean = np.mean(hsv_h)
        h_std = np.std(hsv_h)
        s_mean = np.mean(hsv_s)
        s_std = np.std(hsv_s)
        v_mean = np.mean(hsv_v)
        v_std = np.std(hsv_v)

        lower_color = np.array([h_mean - 40*h_std, s_mean - 40*s_std, v_mean - 40*v_std])
        upper_color = np.array([h_mean + 40*h_std, s_mean + 40*s_std, v_mean + 40*v_std])

        img_mask = cv.inRange(img_hsv, lower_color, upper_color)
    return img_mask

def show():
    global result
    if result != "":
        photo_2 = ImageTk.PhotoImage(file=result)
        pLabel2.configure(image=photo_2)
        pLabel2.image = photo_2
    else:
        pass

window = Tk()
window.geometry("500x400")
window.title("Color Detecting Program")
label1 = Label(window, text="Click three times.")
label1.place(x=200, y=20)

photo_2 = PhotoImage()
pLabel2 = Label(window, image=photo_2)
pLabel2.place(x=270, y=50)

canvas = tkinter.Canvas(window, width=200, height=256)
canvas.place(x=20, y=50)
canvas.bind("<Button-1>", clickMouse)

button = Button(window, text = 'SHOW', command=show)
button.place(x=225, y=350)

mainMenu = Menu(window)
window.config(menu=mainMenu)
fileMenu = Menu(mainMenu, tearoff=0)
mainMenu.add_cascade(label="FILE", menu=fileMenu)
fileMenu.add_command(label="OPEN", command=func_open)
fileMenu.add_command(label="EXIT", command=func_exit)

window.mainloop()