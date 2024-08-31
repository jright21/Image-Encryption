# importing tkinter for GUI
from tkinter import *
from tkinter import filedialog

# create window
root = Tk()
root.title('IMG Encrypt')
root.geometry("500x500")

#Encryption function
def encrypt_image():
    file1 = filedialog.askopenfile(mode='r', filetypes=[('jpg file','*.jpg'),('png file','*.png'),('jpeg file','*.jpeg')])
    #check if file is empty or not
    if file1 is not None:
        file_name = file1.name
        print(file_name)
        key=entry1.get(1.0,END)
        print(key)
        fi=open(file_name,'rb')
        image=fi.read()
        fi.close

        #Converting image data into bytearray

        image = bytearray(image)
        for index,values in enumerate(image):
            image[index]=values^int(key)
        fi1=open(file_name,'wb')
        fi1.write(image)
        fi1.close()

#creating button
b1=Button(root, text="Encrypt", command=encrypt_image)
b1.place(x=240,y=100)

entry1 = Text(root, height=2, width=30)
entry1.place(x=130,y=30)
label_widget = Label(root, text="Hello, Enter the key and choose the image here")
label_widget.pack()

# Insert some text into the Text widget
root.mainloop()



