from tkinter import (
    Button,
    Entry,
    Frame,
    LEFT,
    RIGHT,
    scrolledtext,
    Tk,
    Toplevel,
)

class Window():
    def __init__(self) -> None:

        # no content in root
        self.root = Tk()
        self.root.withdraw()

        # contents are placed in window
        self.window = Toplevel(self.root)
        self.window.title("Encrypter")
        self.textframe = Frame(self.window)
        self.textframe.pack()
        self.passframe = Frame(self.window)
        self.passframe.pack()
        self.text = scrolledtext.ScrolledText(self.textframe)
        self.text.pack(side=LEFT)
        self.text2 = scrolledtext.ScrolledText(self.textframe)
        self.text2.pack(side=RIGHT)
        self.butframe = Frame(self.textframe)
        self.encrypt_button = Button(
            self.butframe, text="->")
        self.decrypt_button = Button(
            self.butframe, text="<-")
        self.exit_button = Button(
            self.butframe, text="x")
        self.butframe.pack()
        self.encrypt_button.pack()
        self.decrypt_button.pack()
        self.exit_button.pack()
        self.pswdbox = Entry(self.passframe, show='*')
        self.pswdbox.pack()
  
    def start_loop(self) -> None:
        self.window.protocol('WM_DELETE_WINDOW', self.root.destroy)
        self.root.mainloop()
