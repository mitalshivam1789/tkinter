from tkinter import *
root = Tk()
root.geometry("512x256")
root.title("shivam")# to change the title of the gui
# Import Label Options
'''
text - adda the text
bg - background
fg - foreground
font - sets the font
1. font =("comicsansms",19,"bold") # one way to use tuples
2. font="comicsansms 19 bold"
padx - x padding
pady - y padding
relief - border styling -SUNKEN, RAISED, GROOVE, RIDGE
'''
title_label =Label(text = '''Abdul Rashid Salim Salman Khan ; born 27 December 1965)[4] is an Indian film actor, producer,
 \n occasional singer and television personality. In a film career spanning over thirty years, Khan has received numerous awards, 
  \nincluding two National Film Awards as a film producer, and two Filmfare Awards for acting.[5] He has a significant following in 
   \nAsia and the Indian diaspora worldwide,[6][better source needed] and is cited in the media as one of the most commercially successful 
   \nactors of both world and Indian cinema.[7][8] According to the Forbes 2018 list of Top-Paid 100 Celebrity Entertainers in world, Khan was the highest
   \n ranked Indian with 82nd rank with earnings of $37.7 million.[9][10] He is also known as the host of the reality show, Bigg Boss since 2010.''',
                   bg="red",
                   fg="white",
                   padx = 100,
                   pady = 50,
                   font=("comicsansms",10,"bold"),
                   borderwidth=3,relief = RAISED)
# important pack options
"""
anchor = nw/ne # nw moves content north west and ne north east
side = top,bottom,left,right
fill = 
padx = 
pady = 
"""
title_label.pack(side=LEFT,fill=Y)
root.mainloop()
