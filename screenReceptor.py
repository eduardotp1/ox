from tkinter import *


class chatRecebido:

    def __init__(self):
        self.window = Tk()
        self.window.title = 'Receptor de texto!'

        self.input_user = StringVar()


        self.frame = Frame(window, width=300, height=300)
        self.frame.pack_propagate(False) # prevent frame to resize to the labels size
        self.frame.pack()

    def comeca(self):
        self.window.mainloop()


    def putText(self, texto):
        self.label = Label(self.frame, text=texto)
        self.input_user.set('')
        self.label.pack()
        return


