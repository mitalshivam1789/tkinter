
from tkinter import *
from PIL import Image, ImageTk # it helps to use all types of image formate in tkinter
shivam_root = Tk() # Tk() a base root file which contains the basic components in it

# geometry way width x height
shivam_root.geometry("512x256")
# for minimum size
#shivam_root.minsize(200,100)
# for max size
#shivam_root.maxsize(1200,500)
# for putting label
label1 = Label(text = "this is the first label")
# to display the label it is required to pack it
label1.pack()

label2 = Label(text = "this is the second label")
label2.pack()
# to insert the image
photo = PhotoImage(file="2.png")
image1_label = Label(image=photo)
image1_label.pack()
# to open the jpg images
image = Image.open("1.jpg")
photo = ImageTk.PhotoImage(image)
image2_label = Label(image = photo)
image2_label.pack()
# gui logic here

shivam_root.mainloop() # mainloop keeps us in gui window and makes it intractive


