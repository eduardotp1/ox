import tkinter as tk
from recepcao import Receptor
from transmissao import Transmissor
import threading as trd
import time

class Interface:

    def __init__(self):
        self.receptor = Receptor()
        self.janela = tk.Tk()
        self.janela.geometry("600x500+100+100")
        self.janela.title("enviador_de_mensagens_do_hackerman.png")
        self.janela.configure(background = 'black')
        self.janela.resizable(True, True)

       

        trd.Thread(target=self.recebe).start()
        self.transmissor = Transmissor()

        self.janela.rowconfigure(0, minsize = 120)
        self.janela.rowconfigure(1, minsize = 10)
        self.janela.rowconfigure(2, minsize = 60)
        self.janela.rowconfigure(3, minsize = 10)
        self.janela.columnconfigure(0, minsize = 40)
        self.janela.columnconfigure(1, minsize = 20)


        self.textView = tk.Text(self.janela, height=15, width=85, bg='black', fg='green')
        self.textView.grid(row=1 ,column = 0, sticky = "nsew")

        self.textField = tk.Text(self.janela, height=1, width = 1, bg='black', fg='green')
        self.textField.grid(row = 2 ,column = 0,sticky = "nsew")
        quoteq = ">_"
        self.textField.insert(tk.END, quoteq)


        self.button_treinar = tk.Button(self.janela, text = "MANDAR", height = 3, width = 10)
        self.button_treinar.grid(row = 3, column = 0,sticky = "nsew")
        self.button_treinar.configure(command = self.mandar)



    def iniciar(self):
        self.janela.mainloop()

    def mandar(self):
        input_text = self.textField.get("1.0",tk.END)
        self.textView.insert(tk.END, 'Mandado: '+input_text)
        self.transmissor.msg = "   " + input_text + "}}}}}}}"
        trd.Thread(target=self.transmissor.envia).start()

    def recebe(self):
        
        trd.Thread(target=self.receptor.serverSocket).start()

        while True:
            if len(self.receptor.recebido) > 0:
                self.textView.insert(tk.END,'Recebido:' + self.receptor.recebido + '\n')
                self.receptor.recebido = ""

            time.sleep(0.5)


app = Interface()
app.iniciar()