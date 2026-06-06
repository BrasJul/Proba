from customtkinter import *
from PIL import Image


window = CTk()
window.geometry('200x200')
window.title('Губка Боб')


img = Image.open('img.jpg')
img_ctk = CTkImage(light_image=img, size=(200, 200))


label = CTkLabel(window, text='Привіт Боб', image=img_ctk)
label.pack(pady=10)


window.mainloop()
