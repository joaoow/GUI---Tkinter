from tkinter import *
window=Tk()
btn=Button(window, text="Código do componente botão", fg='blue')
btn.place(x=80, y=100)
lbl=Label(window, text="Código do componente texto (Rotulo)", fg='red', font=("Helvetica", 16))
lbl.place(x=60, y=50)
txtfld=Entry(window, text="Esse é um componente de entrada de texto", bd=5)
txtfld.place(x=80, y=150)
window.title("Bem-Vindo João!")
window.geometry("300x200+10+10")
window.mainloop()

