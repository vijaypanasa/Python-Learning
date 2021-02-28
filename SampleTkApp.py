#!python3
import os
import tkinter as tk
import sys


class SampleTkApp(tk.Frame):
    """Simple TK GUI application coded to practive GUI-development

    Practise well :) ...
    """

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master
        self.pack()
        self.master.title("hello World... from TK")

        dialog_frm = tk.Frame(self)
        dialog_frm.pack(padx=20, pady=15)
        tk.Label(dialog_frm, text="This is label-frame Tk App..").pack()

        button_frm = tk.Frame(self)
        button_frm.pack(padx=15, pady=(0, 15))

        tk.Button(
            button_frm, text="Ok", default='active',
            command=lambda: self.click_command('Ok')
        ).pack(side='right')

        tk.Button(
            button_frm, text="Cancel", default='active',
            command=lambda: self.click_command('Cancel')
        ).pack(side='right')

        self.entry = tk.StringVar()
        tk.Entry(self, text="Hello All...", textvariable=self.entry).pack()

    def click_command(self, name):
        """Command to run when Buttons are pressed in a frame
        """
        print(f'{self.entry.get()} clicked {name}')
        if(name.lower() == 'cancel'):
            self.master.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = SampleTkApp(root)
    print(f'starting the app... please close it once done with working...')
    app.mainloop()
