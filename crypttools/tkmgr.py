from tkinter import (
    Button,
    END,
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


class EntryWithPlaceholder(Entry):
    def __init__(
            self,
            master=None,
            placeholder="PLACEHOLDER",
            color='grey',
            **options):
        super().__init__(master, **options)

        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self['fg']

        self.bind("<FocusIn>", self.foc_in)
        self.bind("<FocusOut>", self.foc_out)

        self.put_placeholder()

    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self['fg'] = self.placeholder_color

    def foc_in(self, *args):
        if self['fg'] == self.placeholder_color:
            self.delete('0', 'end')
            self['fg'] = self.default_fg_color
            self.config(show='*')

    def foc_out(self, *args):
        if not self.get():
            self.put_placeholder()


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
            self.butframe, text="->",
            command=lambda: self.encrypt(
                self.text.get('1.0', END),
                self.pswdbox.get()))
        self.decrypt_button = Button(
            self.butframe, text="<-",
            command=lambda: self.decrypt(
                self.text2.get('1.0', END),
                self.pswdbox.get()))
        self.exit_button = Button(
            self.butframe, text="x",
            command=self.root.destroy)
        self.butframe.pack()
        self.encrypt_button.pack()
        self.decrypt_button.pack()
        self.exit_button.pack()
        self.pswdbox = EntryWithPlaceholder(self.passframe, 'password')
        self.pswdbox.pack()
  
    def encrypt(self, text, pswd) -> None:
        text = text.rstrip('\n')
        encrypted = encrypt(
            pswd.encode('utf-8'),
            text.encode('utf-8'),
            encode=True)
        self.text2.delete('1.0', END)
        self.text2.insert('1.0', encrypted)

    def decrypt(self, text, pswd) -> None:
        encrypted = decrypt(
            pswd.encode('utf-8'),
            text,
            decode=True)
        self.text.delete('1.0', END)
        self.text.insert('1.0', encrypted.decode('utf-8'))

    def start_loop(self) -> None:
        self.window.protocol('WM_DELETE_WINDOW', self.root.destroy)
        self.root.mainloop()
