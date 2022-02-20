from tkinter import *
from tkinter import filedialog
from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import YouTube

import tkinter as tk
import tkinter.font as tkFont


import shutil

def GButton_28_command():
        path = filedialog.askdirectory()
        GLabel_740["text"] = path

def GCheckBox_351_command():
        if check_1.get() :
            GCheckBox_594.configure(state=DISABLED)
        else :
            GCheckBox_594.configure(state=NORMAL)

def GCheckBox_594_command():
        if check_2.get() :
            GCheckBox_351.configure(state=DISABLED)
        else :
            GCheckBox_351.configure(state=NORMAL)

def GButton_713_command():
    get_link = GLineEdit_627.get()
    user_path = GLabel_740.cget("text")
    if check_1.get() :
        screen.title('Descargando video...')
        MP4_alta_reso = YouTube(get_link).streams.get_highest_resolution().download()
        videotemp = VideoFileClip(MP4_alta_reso)
        videotemp.close()
        shutil.move(MP4_alta_reso,user_path)
        screen.title('Descarga Completada')
    if check_2.get() :
        screen.title('Descargando video...')
        MP4_low_reso = YouTube(get_link).streams.get_lowest_resolution().download()
        videotemp2 = VideoFileClip(MP4_low_reso)
        videotemp2.close()
        shutil.move(MP4_low_reso,user_path)
        screen.title('Descarga Completada')
    

screen = Tk()
title = screen.title('Deescargador Youtube')
Canvas = Canvas(screen, width=450, height=290)
Canvas.pack()

#imagen para el logo
logotipoprin = PhotoImage(file='logo.png')
Canvas.create_image(220,50, image=logotipoprin)

#variables para revisar check
check_1 = tk.IntVar()
check_2 = tk.IntVar()

#Casilla donde poner direccion web Youtube
GLineEdit_627=Entry(screen)
GLineEdit_627["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=10)
GLineEdit_627["font"] = ft
GLineEdit_627["fg"] = "#333333"
GLineEdit_627["justify"] = "center"
GLineEdit_627["text"] = "Enlace Youtube"
GLineEdit_627.place(x=20,y=100,width=417,height=30)

#Label Directorio donde almacenar el video
GLabel_740=tk.Label(screen)
ft = tkFont.Font(family='Times',size=10)
GLabel_740["font"] = ft
GLabel_740["fg"] = "#333333"
GLabel_740["justify"] = "center"
GLabel_740["text"] = "Directorio donde descargar"
GLabel_740.place(x=20,y=140,width=273,height=30)

#Boton elegir donde almacenar el video
GButton_28=tk.Button(screen)
GButton_28["bg"] = "#efefef"
ft = tkFont.Font(family='Times',size=10)
GButton_28["font"] = ft
GButton_28["fg"] = "#000000"
GButton_28["justify"] = "center"
GButton_28["text"] = "Buscar..."
GButton_28.place(x=300,y=140,width=137,height=30)
GButton_28["command"] = GButton_28_command

#Check Video Alta Calidad
GCheckBox_351=tk.Checkbutton(screen)
ft = tkFont.Font(family='Times',size=10)
GCheckBox_351["font"] = ft
GCheckBox_351["fg"] = "#333333"
GCheckBox_351["justify"] = "center"
GCheckBox_351["text"] = "MP4 Alta Calidad"
GCheckBox_351.place(x=0,y=180,width=143,height=30)
GCheckBox_351["offvalue"] = "0"
GCheckBox_351["onvalue"] = "1"
GCheckBox_351["variable"] = check_1
GCheckBox_351["command"] = GCheckBox_351_command

#Check Video Baja Calidad
GCheckBox_594=tk.Checkbutton(screen)
ft = tkFont.Font(family='Times',size=10)
GCheckBox_594["font"] = ft
GCheckBox_594["fg"] = "#333333"
GCheckBox_594["justify"] = "center"
GCheckBox_594["text"] = "MP4 Baja Calidad"
GCheckBox_594.place(x=160,y=180,width=120,height=30)
GCheckBox_594["offvalue"] = "0"
GCheckBox_594["onvalue"] = "1"
GCheckBox_594["variable"] = check_2
GCheckBox_594["command"] = GCheckBox_594_command

#Boton Descargar Video
GButton_713=tk.Button(screen)
GButton_713["bg"] = "#efefef"
ft = tkFont.Font(family='Times',size=10)
GButton_713["font"] = ft
GButton_713["fg"] = "#000000"
GButton_713["justify"] = "center"
GButton_713["text"] = "Descargar"
GButton_713.place(x=300,y=190,width=139,height=46)
GButton_713["command"] = GButton_713_command

screen.mainloop()