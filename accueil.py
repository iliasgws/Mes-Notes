import tkinter as app

def open_homepage():
    
    homepage = app.Tk()
    homepage.title("Accueil | Mes notes")
    homepage.geometry("700x500")
    homepage.config(bg="green")

    welcome_label = app.Label(homepage, text="Une nouvelle experience pour vos notes !", bg="blue", font=("Arial", 24))
    welcome_label.pack(pady=50)

    homepage.mainloop()
