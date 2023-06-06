from tkinter import *
from PIL import ImageTk,Image
root=Tk()
root.title("Welcome to the modern ERA")
# images
my_image1=ImageTk.PhotoImage(Image.open("Photo profile.jpeg"))
my_image2=ImageTk.PhotoImage(Image.open("phot_1.jpeg"))
my_image3=ImageTk.PhotoImage(Image.open("photo_2.jpeg"))
my_image4=ImageTk.PhotoImage(Image.open("photo_3.jpeg"))
my_image5=ImageTk.PhotoImage(Image.open("photo_6.jpeg"))
my_image6=ImageTk.PhotoImage(Image.open("photo_5.jpeg"))

my_images=[my_image1,my_image2,my_image3,my_image4,my_image5,my_image6]
status=Label(root,text="Image 1 of "+ str(len(my_images)),bd=1,relief=SUNKEN,anchor=E)

my_Label=Label(image=my_image1)
my_Label.grid(row=0,column=0,columnspan=3)

def forward(img_number):
    global my_Label
    global button_forward
    global button_back

    my_Label.grid_forget()
    my_Label=Label(image=my_images[img_number-1])

    button_forward=Button(root,text=">>",command=lambda : forward(img_number+1))
    button_back=Button(root,text="<<",command=lambda : backward(img_number-1))

    status = Label(root, text="Image "+str(img_number)+" of " + str(len(my_images)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)

    if img_number==5:
        button_forward=Button(root,text=">>",state=DISABLED )

    my_Label.grid(row=0,column=0,columnspan=3)
    button_forward.grid(row=1,column=2)
    button_back.grid(row=1,column=0)

def backward(img_number):
    global my_Label
    global button_forward
    global button_back

    if img_number==0:
        button_back=Button(root,text="<<",state=DISABLED)

    my_Label.grid_forget()
    my_Label = Label(image=my_images[img_number - 1])

    button_forward = Button(root, text=">>", command=lambda: forward(img_number + 1))
    button_back = Button(root, text="<<", command=lambda: backward(img_number - 1))

    status = Label(root, text="Image " + str(img_number) + " of " + str(len(my_images)), bd=1, relief=SUNKEN, anchor=E)
    '''NEWS-North East West South'''
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)

    my_Label.grid(row=0, column=0, columnspan=3)
    button_forward.grid(row=1, column=2)
    button_back.grid(row=1, column=0)

button_back=Button(root,text="<<",command=lambda : backward()).grid(row=1,column=0)
button_forward=Button(root,text=">>",command=lambda :forward(2)).grid(row=1,column=2)
buuton_exit=Button(root,text="Exit",command=root.quit).grid(row=1,column=1,pady=10)


root.mainloop()