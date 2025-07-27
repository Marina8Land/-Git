"""Кото фото"""

from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO


def load_image():
    try:
        response = requests.get(url)
        response.raise_for_status()
        image_data = BytesIO(response.content)
        img = Image.open(image_data)
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f'произошла ошика {e}')
        return None



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
