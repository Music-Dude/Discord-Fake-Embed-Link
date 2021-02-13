import PIL, urllib, tkinter, clipboard
from tkinter import *
from PIL import ImageTk
from urllib import *
root = Tk()
root.geometry('600x400')
root.resizable(False, False)
root.configure(bg='#7289da')
root.title('Discord Fake Embed Generator')
root.iconbitmap('icon.ico')
l = Label(root, text='Fake Link')
l.place(x=75, y=50)
e = Label(root, text='Embed')
e.place(x=75, y=150)
url = Entry(root, width=75)
url.place(x=75, y=75)
embedLink = Entry(root, width=75)
embedLink.place(x=75, y=175)
def click():
    output = '<' + url.get() + '>' + ' ||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​|| ' + embedLink.get()
    generate = Label(root, text=clipboard.copy(output))
    busted_display = Label(root, text="Successfully copied to clipboard")
    busted_display.place(x=0, y=0)
    root.after(2000, busted_display.destroy)
button = Button(root, text='Generate!', command=click)
button.place(x=200, y=250, height=100, width=200)

root.mainloop()