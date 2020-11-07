import tkinter as Tk
from cryptography import fernet
import hashlib

string=""

'''  #To load a specific key stored in a file
file = open('key.key','rb')
key = file.read()
file.close()
'''
key ='JHCvclW-kphb0-a64GNENYLFhhg97L19zRnDA7IVcwI=' #Random key
f1 = fernet.Fernet(key)

window = Tk.Tk()
window.configure(bg="black")
heading = Tk.Label(text="©Muneeb Bhalli",fg="yellow",bg="black")
heading.pack()
def printtext():
    global entry
    string = entry.get() 
    name = str(string)
    name =name.encode()
    enc_msg = f1.encrypt(name)
    lb = Tk.Label(text=enc_msg,height=5,bg="black",fg="red")
    lb.pack()
    file = open('enc.txt','a')
    file.writelines(str(enc_msg)+'\n')
    file.close()
    return string   

label = Tk.Label(text="Enter Message",width=30,height=5,bg = "black",fg="yellow")
label.config(font=("Courier",13))
label.pack()
entry = Tk.Entry(window)
entry.pack()
name = entry.get()
b = Tk.Button(window,text='okay',command=printtext)
b.pack()



window.mainloop()