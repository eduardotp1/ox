from tkinter import *


def main():
    global frame, input_user

    window = Tk()
    window.title = 'Receptor de texto!'

    input_user = StringVar()


    frame = Frame(window, width=300, height=300)
    frame.pack_propagate(False) # prevent frame to resize to the labels size
    frame.pack()

    #putText('oi tirta')
    window.mainloop()

def putText(texto):
    label = Label(frame, text=texto)
    input_user.set('')
    label.pack()
    return

if __name__ == "__main__":
    main()

