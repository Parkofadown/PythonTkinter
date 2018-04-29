from tkinter import *
from tkinter import ttk

class Richard:
    def __init__(self, master):
        self.label = ttk.Label(master, text = 'Hello, Richie!')
        self.label.pack()
        
        ttk.Button(master, text = 'Click Here!',
                   command = self.Click_here).pack()
        
        ttk.Button(master, text = 'Press me!',
                   command = self.Press_me).pack()
       

    def Click_here(self):
        self.label.config(text = 'Richie! Daddy Loves you!', foreground = 'blue', background = 'red')
    
    def Press_me(self):
        self.label.config(text = 'Richard stop bumping your head!', foreground = 'blue', background = 'red')
    
def main():
        root = Tk()
        app = Richard(root)
        root.mainloop()

if __name__ == '__main__': main()
