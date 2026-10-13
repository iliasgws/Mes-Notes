import tkinter as app
interface=app.Tk()
interface.title("aaaaa")
interface.geometry("700x500")
interface.config(bg="pink")

def login():
    user = username.entry.get()
    passwd =  passwd_entry.get()

    if  user = "admin" and passwd = "01":
        fenetre.destroy()

        homepage =app.TK

Tf=app.Label(interface,text="Nom d'utilisateur",bg="pink")
Tf.pack()
X=app.Entry(interface,)
X.pack()
d=app.Label(interface,text="Mot de passe",bg="pink")
d.pack()
X=app.Entry(interface,)
X.pack()
X=app.Button(interface,text="Login")
X.pack()
