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
import base64
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random


def encrypt(key, source, encode=True):
    key = SHA256.new(key).digest()
    IV = Random.new().read(AES.block_size)
    encryptor = AES.new(key, AES.MODE_CBC, IV)
    padding = AES.block_size - len(source) % AES.block_size
    source += bytes([padding]) * padding
    data = IV + encryptor.encrypt(source)
    return base64.b64encode(data).decode("latin-1") if encode else data


def decrypt(key, source, decode=True):
    if decode:
        source = base64.b64decode(source.encode("latin-1"))
    key = SHA256.new(key).digest()
    IV = source[:AES.block_size]
    decryptor = AES.new(key, AES.MODE_CBC, IV)
    data = decryptor.decrypt(source[AES.block_size:])
    padding = data[-1]
    if data[-padding:] != bytes([padding]) * padding:
        raise ValueError("Invalid padding...")
    return data[:-padding]


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
