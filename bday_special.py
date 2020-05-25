from tkinter import *
import tkinter.messagebox
from PIL import ImageTk,Image
from tkinter import filedialog
from pygame import mixer
import webbrowser
#import bday_bakend

window=Tk()
mixer.init()
####Create Menubar
menubar=  Menu(window)
window.config(menu=menubar)

text= Label(window, text= 'Ye wala \n Gaana tereliye \n Click Kar:')     #####To play Songs
text.grid(row=0,column=3)

myimg1= ImageTk.PhotoImage(Image.open("Pics/hbd.jpg").resize((380, 350), Image.ANTIALIAS))   ###For the first page HBD
labelphoto= Label(image= myimg1)
labelphoto.grid(row=0,column=0,columnspan=3)


def test_func():                                                                ####Different functions I need to define to display topic specific pics



	myimg1= ImageTk.PhotoImage(Image.open("Pics/pic1.jpg").resize((380, 350), Image.ANTIALIAS))
	myimg2= ImageTk.PhotoImage(Image.open("Pics/pic2.jpg").resize((350, 350), Image.ANTIALIAS))
	myimg3= ImageTk.PhotoImage(Image.open("Pics/pic3.jpg").resize((350, 350), Image.ANTIALIAS))
	myimg4= ImageTk.PhotoImage(Image.open("Pics/pic4.jpg").resize((350, 350), Image.ANTIALIAS))
	myimg5= ImageTk.PhotoImage(Image.open("Pics/pic5.jpg").resize((350, 350), Image.ANTIALIAS))

	global mylabel1
	mylabel1= Label(image=myimg1)
	mylabel1.grid(row=0,column=0,columnspan=3)


	global img_list 
	img_list = [myimg1, myimg2, myimg3, myimg4, myimg5]


def forward(image_number):
	#myimg1= ImageTk.PhotoImage(Image.open("Pics/pic1.jpg").resize((380, 350), Image.ANTIALIAS))
	#myimg2= ImageTk.PhotoImage(Image.open("Pics/pic2.jpg").resize((350, 350), Image.ANTIALIAS))
	#myimg3= ImageTk.PhotoImage(Image.open("Pics/pic3.jpg").resize((350, 350), Image.ANTIALIAS))
	#myimg4= ImageTk.PhotoImage(Image.open("Pics/pic4.jpg").resize((350, 350), Image.ANTIALIAS))
	#myimg5= ImageTk.PhotoImage(Image.open("Pics/pic5.jpg").resize((350, 350), Image.ANTIALIAS))

	mylabel1.grid_forget()

	global mylabel
	#mylabel= Label(image=myimg2)
	global button_back
	global button_for
	#mylabel.grid_forget()

	mylabel= Label(image=img_list[image_number-1])
	button_for = Button(window, text= ">>",command= lambda:forward(image_number+1))
	button_back = Button(window, text= "<<",command=  lambda: back(image_number-1) )

	if image_number==5:
		button_for = Button(window, text= ">>",state=DISABLED)
		
	mylabel.grid(row=0,column=0 , columnspan =3)

	button_back.grid(row=1,column=0)
	button_for.grid(row=1, column=2)


def back(image_number):
	global mylabel
	global button_back
	global button_for

	mylabel.grid_forget()

	mylabel= Label(image=img_list[image_number-1])
	button_for = Button(window, text= ">>",command= lambda:forward(image_number+1))
	button_back = Button(window, text= "<<",command=  lambda: back(image_number-1) )

	if image_number==1:
		button_for = Button(window, text= ">>",state=DISABLED)


	mylabel.grid(row=0,column=0 , columnspan =3)

	button_back.grid(row=1,column=0)
	button_for.grid(row=1, column=2)

def play_btn():
	mixer.music.load("Pics/bdaysong.mp3")
	mixer.music.play()
	#print("Hey There")

photo = ImageTk.PhotoImage(Image.open('Pics/play.png').resize((40, 40), Image.ANTIALIAS))
#labelphoto= Label(image= photo)
#labelphoto.grid(row=0,column=3,sticky=S,pady=99)

ply_btn = Button(window, image= photo, command=play_btn)
ply_btn.grid(row=0,column=3,sticky=S,pady=99)


def msg():
	tkinter.messagebox.showinfo('Happy Birthday Jaan','Trial msg hai ye aaa bbbb ccc')

def warn():
	tkinter.messagebox.showerror('Savdhan','Sunle betaa meko bhot pyaar ayewala terpe so na ab digest krle! I lub u !')

def onClick():
    tkinter.messagebox.showinfo("Tusssi Ja Rahe Hoo?","Thank you for viewing!! Ab naaa ek wideeeeeee smileeee kar. Bsss Auuurr Thoddisii wideee! ThankYou, I lub u!!")

def onClickdiary():
    tkinter.messagebox.showinfo("Kyuu?","Agr kbhi teko merpe ghussa aye ya bura lge mere kisi baat ka toh sbse phle toh beta bejhijhak boliyo meko direct! N nahich bolneka mann krra bhotich ghussa ayewala toh use this secret diary and vent out your feelings.Teresiway ise koi ni pdh sktaa.Achha btw pyaar aya n jataneka mann ni krra woh bhi likh sktaa tu yahape")

def linkit():
	webbrowser.open('https://khushbulalwani106.wixsite.com/khushuu',new=2)

def play_gaana():
	webbrowser.open('https://gaana.com/',new=2)

def useithow():
	tkinter.messagebox.showinfo("Ise kaise istemal kre?",'Ab woh bhi mech batau? Explore karo!')

##Create submenus

subMenu= Menu(menubar,tearoff=0)

def browse_file():
	global filename
	filename = filedialog.askopenfilename()
	#print(filename)

menubar.add_cascade(label='Message for You',menu=subMenu)
subMenu.add_command(label= 'Click Kar',command=msg)
subMenu.add_command(label= 'Savdhaan',command=warn)
subMenu.add_command(label= 'Ise kaise istemaal kre?',command=useithow)
#subMenu.add_command(label= 'Not Bachpan')

subMenu= Menu(menubar,tearoff=0)
menubar.add_cascade(label='Pics',menu=subMenu)
subMenu.add_command(label= 'You & Me')
subMenu.add_command(label= 'Bachpan')
subMenu.add_command(label= 'Not Bachpan',command=test_func)
subMenu.add_command(label= 'Yewale Meritarafse')

subMenu= Menu(menubar,tearoff=0)
menubar.add_cascade(label='Poetry',menu=subMenu)
subMenu.add_command(label= 'Teriwali')
subMenu.add_command(label= 'Meriwali tereliye')

subMenu= Menu(menubar,tearoff=0)
menubar.add_cascade(label='Gaane',menu=subMenu)
subMenu.add_command(label= 'Tu Gayewale')
subMenu.add_command(label= 'Jo tere gaane bche hai')
subMenu.add_command(label= 'Jo teko isi moment sunneka mann krra',command=play_gaana)

subMenu= Menu(menubar,tearoff=0)
menubar.add_cascade(label='Webpage',menu=subMenu)
subMenu.add_command(label= 'Terach hai click kar',command=linkit)
#subMenu.add_command(label= 'Jo tere gaane bche hai')

subMenu= Menu(menubar,tearoff=0)
menubar.add_cascade(label='Secret Diary',menu=subMenu)
subMenu.add_command(label= 'kyuu?',command=onClickdiary)



window.title('Happppyyyy Birthdayyyy Darlooo!!')
#window.iconbitmap('./index.png')   ## To create icon on window
window.geometry("480x380")


button_back = Button(window, text= "<<",command=  back ,state=DISABLED)
button_for = Button(window, text= ">>",command= lambda:forward(2))
button_exit = Button(window, text= "ISPE AAKHRI MEIN CLICK KRNEKA",command=onClick)

button_back.grid(row=1,column=0)
button_for.grid(row=1, column=2)

button_exit.grid(row=1,column=1)














window.mainloop()
