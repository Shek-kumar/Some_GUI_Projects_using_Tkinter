from os import listdir
from tkinter import *
from PIL import Image, ImageTk
import os

Counter = 1

def Rotate_img():
    global Counter
    img_label.config(image=img_array[Counter % len(img_array)])
    Counter+=1



# Creating a Tkinter window
root = Tk()

root.title("Wallpaper Viewer")  # Setting up the title of the GUI
root.iconbitmap('icon.ico')  # Changing the logo of the GUI

# Setting the geometry of the GUI
root.geometry('400x550')
root.configure(background='black')  # Changing the background color

# opening wallpaper folder
files = listdir('Wallpapers')

# loading images in a image array as object
img_array = []
for file in files:
    img = Image.open(os.path.join('Wallpapers',file))
    resized_img = img.resize((350,400))
    Img = ImageTk.PhotoImage(resized_img)
    img_array.append(Img)

img_label = Label(root,image = img_array[0])
img_label.pack(pady=(15,10))

next_btn = Button(text='Next',bg='white',fg='black',width=27,height=2,command= lambda:Rotate_img())
next_btn.pack(pady=(10,5))
next_btn.config(font=('verdana',15))

root.mainloop()  # Running the GUI loop
