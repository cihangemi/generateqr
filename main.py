import os
import time
from tkinter import *
from PIL import ImageTk,Image

import qr
from qr import makeQR

imas="/Users/PC/PycharmProjects/qrgenerate/{}.png"











app =Tk()
def main():

    a=linkEntry.get()
    b=qrEntry.get()
    qrcomp=makeQR(a,b)
    d=imas.format(b)
    icon=ImageTk.PhotoImage(Image.open(d))
    qrhereLabel.configure(image=icon)
    qrhereLabel.image=icon

def changelocation():
    b=qrEntry.get()
    d=imas.format(b)
    icon=Image.open(d)
    icon.save("C:/Users/PC/Desktop/"+str(b)+".png")
    time.sleep(2)
    os.remove("/Users/PC/PycharmProjects/qrgenerate/"+str(b)+".png")






app.title("QR Generator")
app.geometry("420x680+100+200")
app.resizable(False,False)
app.configure(bg="#17161b" )

cerceve1 = Frame(app)
cerceve1.pack(side = "top", fill="both", expand=True)
cerceve2 = Frame(app,bg="white")
cerceve2.pack(side = "bottom")

linkLabel=Label(cerceve1,width=7,height=1,text="Link:",font=("Arial",15)).place(height=27,x=20 ,y=1)

linkEntry=Entry(cerceve1,justify="left",font=("Arial",15),background="#f8f8ff")
linkEntry.place(x=110,y=1)
linkEntry.focus()

qrLabel=Label(cerceve1,width=7,height=3,text="Qr-Adı:",font=("Arial",15)).place(height=27,x=20, y=60)

qrEntry=Entry(cerceve1,justify="left",font=("Arial",15),background="#f8f8ff")
qrEntry.place(x=110,y=60)
qrEntry.focus()

searchButton=Button(cerceve1,text="Oluştur",width=30,height=1,command=main).place(x=110,y=120,)

showqrLabel=Label(cerceve1,width=35,height=1,text="QR KODUNUZ",font=("Arial",15),justify="center").place(height=27,x=20 ,y=200)

qrhereLabel=Label(cerceve1,width=440,height=270)
qrhereLabel.place(y=260)

saveButton=Button(cerceve1,text="Kaydet",width=30,height=1,command=changelocation).place(x=110,y=550)




app.mainloop()


