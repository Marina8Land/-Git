"""Кото фото"""

from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO


def load_image(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        image_data = BytesIO(response.content)
        img = Image.open(image_data)
        img.thumbnail((600,480),Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f'произошла ошибка {e}')
        return None


def set_image():
    img = load_image(url)

    if img:
        lable.config(image=img)
        lable.image = img

def exit():
    window.destroy()

window = Tk()
window.title('Котики')
window.geometry('600x520')

lable = Label()
lable.pack()

# update_button = Button(text='Обновить', command=set_image)
# update_button.pack()

menu_bar = Menu(window)
window.config(menu=menu_bar)
file_menu =Menu()
menu_bar.add_cascade(label='Файл')
menu_bar.add_command(label='Загрузить фото', command=set_image)
menu_bar.add_command(label='Загрузить фото', command=set_image)
menu_bar.add_command(label='Загрузить фото', command=set_image)

url = 'https://cataas.com/cat'

set_image()

window.mainloop()
