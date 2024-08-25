from tkinter import *
from tkinter import messagebox

from PIL import Image, ImageTk

def handle_login():
    email = email_input.get()
    password = password_input.get()

    if email =='shek@123' and password == '1412' :
        messagebox.showinfo('Yayy','Login Succesful'
                                   ' Welcome Shekhar')

    elif email =='shek@1412' and password == '1234':
        messagebox.showinfo('Yayy','Login Succesful'
                                   ' Welcome Kumar')

    else:
        messagebox.showerror('Error','Login Failed')




# Creating a Tkinter window
root = Tk()

root.title("Login Page")  # Setting up the title of the GUI
root.iconbitmap('icon.ico')  # Changing the logo of the GUI

# Setting the geometry of the GUI
root.geometry('400x550')
root.configure(background='#0096DC')  # Changing the background color

# Opening and resizing the image using PIL
img = Image.open('flipkart_logo.png')
resized_img = img.resize((70, 70), Image.LANCZOS)

# Converting the resized image to PhotoImage
photo_img = ImageTk.PhotoImage(resized_img)

# Adding the image to the GUI using Label
img_label = Label(root, image=photo_img)
img_label.pack(pady=(10,10))  # Packing the label


# Adding text in our gui using Label class
text_label = Label(root,text = "Flipkart", fg='white',bg="#0096DC")
text_label.pack()
text_label.configure(font = ('verdana',30))


# Adding text to enter your mail id in our gui using Label class
email_label = Label(root,text = "Enter your mail id", fg='white',bg="#0096DC")
email_label.pack(pady=(20,5))
email_label.configure(font = ('verdana',15))


# using Entry class to take input for email id in our gui
email_input = Entry(root,width = 60)
email_input.pack(ipady = 6,pady=(1,15))


# Adding text to enter your password  in our gui using Label class

password_label = Label(root,text = "Enter your Password", fg='white',bg="#0096DC")
password_label.pack(pady=(20,5))
password_label.configure(font = ('verdana',15))


# using Entry class to take input for password in our gui
password_input = Entry(root,width = 60)
password_input.pack(ipady = 6,pady=(1,15))

# creating a login button using the Button class
login_btn = Button(root,text ='Press to Login',fg='white',bg='green',width=20,height=2 , command = lambda:handle_login())
login_btn.pack(pady=(10,20))
login_btn.config(font = ('verdana',13))

root.mainloop()  # Running the GUI loop
