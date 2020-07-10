from tkinter import *
import tkinter.messagebox
from PIL import ImageTk,Image
from tkinter import filedialog
from pygame import mixer
import webbrowser
import os

gtk = Tk()

def getFileName(image):
    print(str(image))

for images in os.listdir(os.getcwd()):
        if images.endswith("png"):
            im = Image.open(images)
            tkimage = ImageTk.PhotoImage(im)
            handler = lambda img = images: getFileName(img)  #here modify
            imageButton = Button(gtk, image=tkimage, command=handler)#here
            imageButton.image=tkimage
            imageButton.pack()


gtk.mainloop()