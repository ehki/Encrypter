from tkinter import (
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
  
    def start_loop(self) -> None:
        self.window.protocol('WM_DELETE_WINDOW', self.root.destroy)
        self.root.mainloop()
