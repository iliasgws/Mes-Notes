import tkinter as app
import accueil  

interface = app.Tk()
interface.title("Connection | Mes notes")
interface.geometry("700x500")
interface.config(bg="pink")

def login():
    user = username_entry.get()
    passwd = passwd_entry.get()

    if user == "admin" and passwd == "01":
        interface.destroy() 
        
        
        accueil.open_homepage()

Tf = app.Label(interface, text="Nom d'utilisateur", bg="pink")
Tf.pack()

username_entry = app.Entry(interface)
username_entry.pack()

d = app.Label(interface, text="Mot de passe", bg="pink")
d.pack()

passwd_entry = app.Entry(interface, show="*")
passwd_entry.pack()

login_btn = app.Button(interface, text="Login", command=login)
login_btn.pack()

interface.mainloop()
