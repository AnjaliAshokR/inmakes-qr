import os
from gtts import gTTS
from tkinter import *
root=Tk()
def txt_to_speech():
    input_txt=inp.get()
    out_text = gTTS(text=input_txt, lang='en', slow=False)
    out_text.save('file_out.mp3')
    os.system("start file_out.mp3")
canvas=Canvas(root, width=400, height=400)
canvas.pack()
inp=Entry(root)
canvas.create_window(200,200, window=inp)
button=Button(text="start", command=txt_to_speech)
canvas.create_window(200, 300,window=button)
root.mainloop()