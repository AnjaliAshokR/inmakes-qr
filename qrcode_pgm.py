from tkinter import *
import pyqrcode
from PIL import ImageTk,Image
import png
root=Tk()
canvas=Canvas(root, width=400, height=700)
canvas.pack()
def qr_generate():
    name=name_input.get()
    link=link_input.get()
    file_name=name + ".png"
    qr_url= pyqrcode.create(link)
    qr_url.png(file_name,scale=7)
    img=ImageTk.PhotoImage(Image.open(file_name))
    img_label=Label(image=img)
    img_label.img=img
    canvas.create_window(200,450,window=img_label)
app_label=Label(root,text="QR Code Generator", font=("Arial",30),bd=3)
canvas.create_window(200,100,window=app_label)
label_name=Label(root,text="Link Name")
label_link=Label(root, text="Link")
canvas.create_window(200,150, window=label_name)
canvas.create_window(200,200,window=label_link)
name_input=Entry(root)
link_input=Entry(root)
button=Button(text="Generate",command=qr_generate)
canvas.create_window(200,170, window=name_input)
canvas.create_window(200,220,window=link_input)
canvas.create_window(200,260,window=button)
root.mainloop()