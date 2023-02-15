from tkinter import *

def seleccionar():
    ventana.config(text="{}".format(opcion.get()))
def reset():
    opcion.set(None)
    ventana.config(text="")

root = Tk()
opcion = StringVar()
opcion.set(None)
Radiobutton(root, text="Argentina", variable=opcion, 
            value='Arentina', command=seleccionar).pack(anchor=W)

Radiobutton(root, text="Brasil", variable=opcion, 
            value='Brasil', command=seleccionar).pack(anchor=W)
Radiobutton(root, text="Chile", variable=opcion,   
            value='Chile', command=seleccionar).pack(anchor=W)
Radiobutton(root, text="Venezuela", variable=opcion,   
            value='Venezuela', command=seleccionar).pack(anchor=W)

ventana = Label(root)
ventana.pack()
Button(root, text="Reiniciar", command=reset).pack()

root.mainloop()