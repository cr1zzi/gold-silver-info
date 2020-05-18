from tkinter import *

from PIL import Image , ImageTk

Photo = 'gold.jpg'

def page1():
    page2.pack_forget()
    page1.pack()


def page2():
    page1.pack_forget()
    page2.pack()

window = Tk()



canvas = Canvas(window, width=250, height=250)
canvas.pack()

tk_img = ImageTk.PhotoImage(file = Photo)
canvas.create_image(125, 125, image=tk_img)

quitbut = Button(window , text = "Exit",command = quit)
quitbut_window = canvas.create_window(130,20 , window = quitbut)

aur = Button(window, text = "Aur",  anchor = 's',
                    width = 10, activebackground = "#ffff66" , command = page1)
aur_window = canvas.create_window(15, 50, anchor='nw', window=aur)

argint = Button(window, text = "Argint",  anchor = 's',
                    width = 10, activebackground = "#b3b3b3" , command =page2)
argint_window = canvas.create_window(160, 50, anchor='nw', window=argint)


page1 = Label(window , text="999 / 995 / 986 \t\t\t 24k\n"
                            "953 \t\t\t\t 23k\n"
                            "916 \t\t\t\t 22k\n"
                            "833 \t\t\t\t 20k\n"
                            "750 \t\t\t\t 18k\n"
                            "625 \t\t\t\t 15k\n"
                            "585 \t\t\t\t 14k\n"
                            "417 \t\t\t\t 10k\n"
                            "375 \t\t\t\t  9k\n"
                            "333 \t standard minim \t\t  8k")

page2 = Label(window,
text="999                           Argint fin utilizat in lingouri\n\
980                  Standard comun folosit in Mexic\n\
958                   Echivalent cu Britannia de argint\n\
925                      Echivalent cu Sterling de argint\n\
835                         Standard utilizat in Germania\n\
833           Utilizat in Olanda , Suedia , Germania\n\
830   Standard folosit in argint scandinav vechi\n\
800                               Standard minim de argint")


window.mainloop()


