from tkinter import *
import tkinter.messagebox
from PIL import ImageTk,Image
from tkinter import filedialog
from pygame import mixer
import webbrowser
#import bday_bakend
import os
import os.path as OP
#import os
import sys
import random
import pkg_resources.py2_warn
from PIL.Image import core as _imaging

window=Tk()
mixer.init()
####Create Menubar
menubar=  Menu(window)
window.config(menu=menubar)

text= Label(window, text= 'Ye wala \n Gaana tereliye \n 🖤🖤🖤 \n Click Kar:')     #####To play Songs
text.grid(row=0,column=3)

myimg1= ImageTk.PhotoImage(Image.open("Pics/hbd.jpg").resize((380, 350), Image.ANTIALIAS))   ###For the first page HBD
labelphoto= Label(image= myimg1)
labelphoto.grid(row=0,column=0,columnspan=3)

def ynme():              ####You&Me subpart

	myimg1= ImageTk.PhotoImage(Image.open("Pics/YNME/pic3.jpg").resize((350, 350), Image.ANTIALIAS).rotate(180))
	myimg2= ImageTk.PhotoImage(Image.open("Pics/YNME/pic2.jpg").resize((350, 350), Image.ANTIALIAS).rotate(180))
	myimg3= ImageTk.PhotoImage(Image.open("Pics/YNME/pic1.jpg").resize((350, 350), Image.ANTIALIAS))
	myimg4= ImageTk.PhotoImage(Image.open("Pics/YNME/pic4.jpg").resize((350, 350), Image.ANTIALIAS))
	myimg5= ImageTk.PhotoImage(Image.open("Pics/YNME/pic5.jpg").resize((350, 350), Image.ANTIALIAS))
	myimg6= ImageTk.PhotoImage(Image.open("Pics/YNME/pic6.jpg").resize((350, 350), Image.ANTIALIAS))


	global mylabel1
	mylabel1= Label(image=myimg1)
	mylabel1.grid(row=0,column=0,columnspan=3)


	global im
	im = [myimg1, myimg2, myimg3, myimg4, myimg5,myimg6]


def mtfse():              ####You&Me subpart

	myimg1= ImageTk.PhotoImage(Image.open("Pics/MTFSE/pic8.jpeg").resize((350, 350), Image.ANTIALIAS))
	#myimg2= ImageTk.PhotoImage(Image.open("Pics/MTFSE/pic2.jpg").resize((350, 350), Image.ANTIALIAS))
	myimg3= ImageTk.PhotoImage(Image.open("Pics/MTFSE/pic3.jpg").resize((350, 350), Image.ANTIALIAS))
	myimg4= ImageTk.PhotoImage(Image.open("Pics/MTFSE/pic4.png").resize((350, 350), Image.ANTIALIAS))
	myimg5= ImageTk.PhotoImage(Image.open("Pics/MTFSE/pic5.jpeg").resize((350, 350), Image.ANTIALIAS))
	myimg6= ImageTk.PhotoImage(Image.open("Pics/MTFSE/pic6.jpeg").resize((350, 350), Image.ANTIALIAS))
	myimg7= ImageTk.PhotoImage(Image.open("Pics/MTFSE/pic7.jpeg").resize((500, 350), Image.ANTIALIAS))
	myimg8= ImageTk.PhotoImage(Image.open("Pics/MTFSE/pic1.jpg").resize((350, 350), Image.ANTIALIAS))
	myimg9= ImageTk.PhotoImage(Image.open("Pics/MTFSE/pic9.png").resize((350, 350), Image.ANTIALIAS))
	#myimg10= ImageTk.PhotoImage(Image.open("Pics/MTFSE/pic10.png").resize((350, 350), Image.ANTIALIAS))
	myimg11= ImageTk.PhotoImage(Image.open("Pics/MTFSE/pic11.png").resize((500, 350), Image.ANTIALIAS))
	#myimg12= ImageTk.PhotoImage(Image.open("Pics/MTFSE/pic12.png").resize((500, 350), Image.ANTIALIAS))


	global mylabel1
	mylabel1= Label(image=myimg1)
	mylabel1.grid(row=0,column=0,columnspan=3)


	global im
	im = [myimg1, myimg3, myimg4, myimg5,myimg6,myimg7,myimg8,myimg9,myimg11]

def kvta():

	myimg1= ImageTk.PhotoImage(Image.open("Pics/kvta/pic1 (1).png").resize((350, 350), Image.ANTIALIAS))
	myimg2= ImageTk.PhotoImage(Image.open("Pics/kvta/pic1 (2).png").resize((350, 350), Image.ANTIALIAS))
	myimg3= ImageTk.PhotoImage(Image.open("Pics/kvta/pic1 (3).png").resize((350, 350), Image.ANTIALIAS))
	myimg4= ImageTk.PhotoImage(Image.open("Pics/kvta/pic1 (4).png").resize((350, 350), Image.ANTIALIAS))
	myimg5= ImageTk.PhotoImage(Image.open("Pics/kvta/pic1 (5).png").resize((350, 350), Image.ANTIALIAS))
	myimg6= ImageTk.PhotoImage(Image.open("Pics/kvta/pic1 (6).png").resize((350, 350), Image.ANTIALIAS))
	myimg7= ImageTk.PhotoImage(Image.open("Pics/kvta/pic1 (7).png").resize((350, 350), Image.ANTIALIAS))
	myimg8= ImageTk.PhotoImage(Image.open("Pics/kvta/pic1 (8).png").resize((350, 350), Image.ANTIALIAS))
	myimg9= ImageTk.PhotoImage(Image.open("Pics/kvta/pic1 (9).png").resize((350, 350), Image.ANTIALIAS))
	
	#mylabel1.grid_forget()
	global mylabel1
	mylabel1= Label(image=myimg1)
	mylabel1.grid(row=0,column=0,columnspan=3)


	global im
	im = [myimg1, myimg2, myimg3, myimg4, myimg5,myimg6,myimg7,myimg8,myimg9]

def mykvta():

	myimg1= ImageTk.PhotoImage(Image.open("Pics/kvta/mine/pic1 (1).jpg").resize((350, 350), Image.ANTIALIAS))
	myimg2= ImageTk.PhotoImage(Image.open("Pics/kvta/mine/pic1 (3).jpg").resize((350, 350), Image.ANTIALIAS))
	myimg3= ImageTk.PhotoImage(Image.open("Pics/kvta/mine/pic1 (2).jpg").resize((350, 350), Image.ANTIALIAS))
	
	
	#mylabel1.grid_forget()
	global mylabel1
	mylabel1= Label(image=myimg1)
	mylabel1.grid(row=0,column=0,columnspan=3)


	global im
	im = [myimg1, myimg2, myimg3 ]

	
def bpan_func():

	myimg1= ImageTk.PhotoImage(Image.open("Pics/Bpan/pic1 (1).png").resize((350, 350), Image.ANTIALIAS))
	myimg2= ImageTk.PhotoImage(Image.open("Pics/Bpan/pic1 (2).png").resize((350, 350), Image.ANTIALIAS))
	myimg3= ImageTk.PhotoImage(Image.open("Pics/Bpan/pic1 (3).png").resize((350, 350), Image.ANTIALIAS))
	myimg4= ImageTk.PhotoImage(Image.open("Pics/Bpan/pic1 (4).png").resize((350, 350), Image.ANTIALIAS))
	myimg5= ImageTk.PhotoImage(Image.open("Pics/Bpan/pic1 (5).png").resize((350, 350), Image.ANTIALIAS))
	myimg6= ImageTk.PhotoImage(Image.open("Pics/Bpan/pic1 (6).png").resize((350, 350), Image.ANTIALIAS))
	myimg7= ImageTk.PhotoImage(Image.open("Pics/Bpan/pic1 (7).png").resize((350, 350), Image.ANTIALIAS))
	myimg8= ImageTk.PhotoImage(Image.open("Pics/Bpan/pic1 (8).png").resize((350, 350), Image.ANTIALIAS))
	myimg9= ImageTk.PhotoImage(Image.open("Pics/Bpan/pic1 (9).png").resize((350, 350), Image.ANTIALIAS))
	
	#mylabel1.grid_forget()
	global mylabel1
	mylabel1= Label(image=myimg1)
	mylabel1.grid(row=0,column=0,columnspan=3)


	global im
	im = [myimg1, myimg2, myimg3, myimg4, myimg5,myimg6,myimg7,myimg8,myimg9]






def test_func():
	
	path = './Pics/NBpan/'

	global im
	images = []

	for dirname, dirnames, filenames in os.walk(path):
	    # print path to all subdirectories first.
	    # for subdirname in dirnames:
	        # print os.path.join(dirname, subdirname)

	    # print path to all filenames.
	    for filename in filenames:
	        file = os.path.join(dirname, filename)
	        if '.jpg' in file.lower() or '.gif' in file.lower() or '.png' in file.lower():
	            images.append(file)








	random_max = random.randrange(10, len(images))
	#print(random_max)
	#print(len(im))
	im = []
	counter = 0
	while counter < random_max:
	    index = random.randrange(0, len(images))
	    im.append(images[index])
	    #print(images[index])
	    images.pop(index)
	    counter +=1 



	#print(selection)


	## Main window
	#root = Tk()
	## Grid sizing behavior in window
	#root.grid_rowconfigure(0, weight=1)
	#root.grid_columnconfigure(0, weight=1)
	## Canvas
	#cnv = Canvas(root)
	#cnv.grid(row=0, column=0, sticky='nswe')
	## Scrollbars for canvas
	"""
	hScroll = Scrollbar(root, orient=HORIZONTAL, command=cnv.xview)
	hScroll.grid(row=1, column=0, sticky='we')
	vScroll = Scrollbar(root, orient=VERTICAL, command=cnv.yview)
	vScroll.grid(row=0, column=1, sticky='ns')
	cnv.configure(xscrollcommand=hScroll.set, yscrollcommand=vScroll.set)
	"""
	## Frame in canvas
	#frm = Frame(cnv)
	## This puts the frame in the canvas's scrollable zone
	#cnv.create_window(0, 0, window=frm, anchor='nw')
	## Frame contents
	global mylabel1
	#global im
	for s in im:
	    imgs = Image.open(s).resize((350, 350), Image.ANTIALIAS)
	    tkimage = ImageTk.PhotoImage(imgs)
	    mylabel1=Label(image = tkimage,master= window)
	    mylabel1.image = tkimage
	    mylabel1.grid(row=0,column=0,columnspan=3)

	## Update display to get correct dimensions
	#frm.update_idletasks()
	## Configure size of canvas's scrollable zone
	#cnv.configure(scrollregion=(0, 0, frm.winfo_width(), frm.winfo_height()))
	## Go!


	#root.mainloop()   




	"""
	global im
	im = []
	i=0 
	for images in os.listdir('C:/Users/LENOVO/Desktop/Python_revision/Executable-Desktop-Application/Pics/NBpan'):
		if images.endswith("png"):

			im.append(ImageTk.PhotoImage((Image.open(images).resize((380, 350), Image.ANTIALIAS))))
			i=i+1

	"""

 	####Different functions I need to define to display topic specific pics


	"""
	myimg1= ImageTk.PhotoImage(Image.open("Pics/NBpan/pic1.jpg").resize((380, 350), Image.ANTIALIAS))
	myimg2= ImageTk.PhotoImage(Image.open("Pics/NBpan/pic2.jpg").resize((350, 350), Image.ANTIALIAS))
	myimg3= ImageTk.PhotoImage(Image.open("Pics/NBpan/pic3.jpg").resize((350, 350), Image.ANTIALIAS))
	myimg4= ImageTk.PhotoImage(Image.open("Pics/NBpan/pic4.jpg").resize((350, 350), Image.ANTIALIAS))
	myimg5= ImageTk.PhotoImage(Image.open("Pics/NBpan/pic5.jpg").resize((350, 350), Image.ANTIALIAS))

	global mylabel1
	mylabel1= Label(image=myimg1)
	mylabel1.grid(row=0,column=0,columnspan=3)


	global img_list 
	img_list = [myimg1, myimg2, myimg3, myimg4, myimg5]

	"""
	
            
            
	#print(i)
	#global mylabel1
	#mylabel1= Label(image=im[0])
	#mylabel1.grid(row=0,column=0,columnspan=3)



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

	mylabel= Label(image=im[image_number-1],master = window)
	mylabel.image= im[image_number-1]
	button_for = Button(window, text= ">>",command= lambda:forward(image_number+1))
	button_back = Button(window, text= "<<",command=  lambda: back(image_number-1) )


	#if image_number==5:
	#	button_for = Button(window, text= ">>",state=DISABLED)
		
	mylabel.grid(row=0,column=0 , columnspan =3)

	button_back.grid(row=1,column=0)
	button_for.grid(row=1, column=2)


def back(image_number):
	global mylabel
	global button_back
	global button_for

	mylabel.grid_forget()

	mylabel= Label(image=im[image_number-1])
	button_for = Button(window, text= ">>",command= lambda:forward(image_number+1))
	button_back = Button(window, text= "<<",command=  lambda: back(image_number-1) )

	#if image_number==1:
	#	button_for = Button(window, text= ">>",state=DISABLED)


	mylabel.grid(row=0,column=0 , columnspan =3)

	button_back.grid(row=1,column=0)
	button_for.grid(row=1, column=2)

def play_btn():
	mixer.music.load("Pics/bdaysong.mp3")
	mixer.music.play()
	#print("Hey There")

def save():
    file_name = entry.get('1.0',END)
    with open('diary.txt', 'a') as file_object:
        file_object.write(file_name)  

def diary():
	if __name__ == '__main__':
	    top = Tk()
	    #large_font = ('Verdana',12)
	    top.title('Type krnaa start kar!!')
	    entry_field_variable = StringVar()
	    #entry = Text(top, textvariable=entry_field_variable, font= large_font ,height = 16)
	    global entry
	    entry = Text(top ,height = 10,width = 50)
	    entry.pack()
	    Button(top, text="save", command=save).pack()

	top.mainloop()

def Suchna():
	tkinter.messagebox.showinfo('Jarurii Suchnaa!!',"Tu jo bhi type krke save kregi diary mein woh diary.txt namke file mein PC mein save ho jayega! \n So agr teko pdhneka mnn kre toh 'diary.txt' file search krna!!")


photo = ImageTk.PhotoImage(Image.open('Pics/play.png').resize((40, 40), Image.ANTIALIAS))
#labelphoto= Label(image= photo)
#labelphoto.grid(row=0,column=3,sticky=S,pady=99)

ply_btn = Button(window, image= photo, command=play_btn)
ply_btn.grid(row=0,column=3,sticky=S,pady=99)


def msg():
	tkinter.messagebox.showinfo("Happy Birthday Jaan🖤🖤","Wish you a lim(n→∞)(very)^n Happiestttttt Birthdayyyyy Darloooo 🖤🖤🖤🖤!! \n Uk what you're the best person I've got in my life ! \n Can't thank God enough to bless me with you in my life!! I love youuu loadssss reeee!!🖤🖤🖤 \n Abhi toh kalka poora din bcha hai sb yahipe pdhna h kya? \n 18 more to go sweetie!!!   ")

def warn():
	tkinter.messagebox.showerror('Savdhan','Sunle betaa meko bhot pyaar ayewala terpe so na ab digest krle! I lub u !🖤🖤🖤')

def onClick():
    tkinter.messagebox.showinfo("Tusssi Ja Rahe Hoo?","Thank you for viewing!! Ab naaa ek wideeeeeee smileeee kar. Bsss Auuurr Thoddisii wideee! ThankYou, I lub u!!🖤🖤🖤")

def onClickdiary():
    tkinter.messagebox.showinfo("Kyuu?","Agr kbhi teko merpe ghussa aye ya bura lge mere kisi baat ka toh sbse phle toh beta bejhijhak boliyo meko direct! \n N nahich bolneka mann krra bhotich ghussa ayewala toh use this secret diary and vent out your feelings. \n Teresiway ise koi ni pdh sktaa. \n Achha btw pyaar aya n jataneka mann ni krra woh bhi likh sktaa tu yahape")

def linkit():
	webbrowser.open('https://khushbulalwani106.wixsite.com/khushuu',new=2)

def vlink():
	webbrowser.open('https://drive.google.com/drive/folders/1nCJMuuJztHcalRuKdI2E34Q68WRQDa0z?usp=sharing',new=2)


def play_gaana():
	webbrowser.open('https://gaana.com/',new=2)

def useithow():
	tkinter.messagebox.showinfo("Ise kaise istemal kre?",'Ab woh bhi mech batau? Explore karo! \n (Bs kbhi forward button kam ni kre toh backward button use krna)')

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
subMenu.add_command(label= 'You & Me (Itne kam yaar)',command= ynme)
subMenu.add_command(label= 'Bachpan',command=bpan_func)
subMenu.add_command(label= 'Not Bachpan',command=test_func)
subMenu.add_command(label= 'Yewale Meritarafse',command= mtfse)

subMenu= Menu(menubar,tearoff=0)
menubar.add_cascade(label='Poetry',menu=subMenu)
subMenu.add_command(label= 'Teriwali',command= kvta)
subMenu.add_command(label= 'Meriwali tereliye', command=  mykvta)

subMenu= Menu(menubar,tearoff=0)
menubar.add_cascade(label='Gaane',menu=subMenu)
subMenu.add_command(label= 'Tu Gayewale',command=vlink)
#subMenu.add_command(label= 'Jo tere gaane bche hai')
subMenu.add_command(label= 'Jo teko isi moment sunneka mann krra',command=play_gaana)

subMenu= Menu(menubar,tearoff=0)
menubar.add_cascade(label='Webpage',menu=subMenu)
subMenu.add_command(label= 'Terach hai click kar',command=linkit)
#subMenu.add_command(label= 'Jo tere gaane bche hai')

subMenu= Menu(menubar,tearoff=0)
menubar.add_cascade(label='Secret Diary',menu=subMenu)
subMenu.add_command(label= 'Click Kar',command=diary)
subMenu.add_command(label= 'kyuu?',command=onClickdiary)
subMenu.add_command(label= 'Jaruri Suchnaa',command=Suchna)



window.title('Happppyyyy Birthdayyyy Darlooo!!')
#window.iconbitmap('./index.png')   ## To create icon on window
window.geometry("480x400")


button_back = Button(window, text= "<<",command=  back ,state=DISABLED)
button_for = Button(window, text= ">>",command= lambda:forward(2))
button_exit = Button(window, text= "ISPE AAKHRI MEIN CLICK KRNEKA",command=onClick)

button_back.grid(row=1,column=0)
button_for.grid(row=1, column=2)

button_exit.grid(row=1,column=1)


window.mainloop()
