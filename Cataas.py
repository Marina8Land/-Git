"""Кото фото"""

from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO

window = Tk()
window.title('Котики')
window.geometry('600x400')

lable = Label()
lable.pack()
url = 'https://cataas.com/cat'
img = load.image(url)

if img:
    lable.config(image=img)
    lable.image = img

window.mainloop()
