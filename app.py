import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import time

class GreetApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Greet App")
        self.root.configure(background='#2C001E')
        self.root.geometry("800x600")

        self.label_name = ttk.Label(self.root, text="Name:", font=("TkDefaultFont", 16), foreground='white', background='#2C001E')
        self.label_name.grid(row=0, column=0, padx=10, pady=10)

        self.entry_name = ttk.Entry(self.root, font=("TkDefaultFont", 16))
        self.entry_name.grid(row=0, column=1, padx=10, pady=10)
        self.entry_name.focus()

        self.label_location = ttk.Label(self.root, text="Location:", font=("TkDefaultFont", 16), foreground='white', background='#2C001E')
        self.label_location.grid(row=1, column=0, padx=10, pady=10)

        self.entry_location = ttk.Entry(self.root, font=("TkDefaultFont", 16))
        self.entry_location.grid(row=1, column=1, padx=10, pady=10)

        self.button_greet = ttk.Button(self.root, text="Greet", command=self.greet)
        self.button_greet.grid(row=2, column=1, pady=10)
        
        self.root.bind('<Return>', self.greet)

        self.var_dark_mode = tk.IntVar()
        self.checkbutton_dark_mode = ttk.Checkbutton(self.root, text="Dark Mode", variable=self.var_dark_mode, command=self.toggle_dark_mode)
        self.checkbutton_dark_mode.grid(row=3, column=0, columnspan=2, pady=10)

    def greet(self, event=None):
        name = self.entry_name.get()
        location = self.entry_location.get()
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
        message = "Hello {}, from {}. Today is {}".format(name, location, current_time)
        messagebox.showinfo("Greeting", message)
        
    def toggle_dark_mode(self):
        is_dark_mode = self.var_dark_mode.get()
        if is_dark_mode:
            self.root.configure(background='#2C001E')
            self.label_name.configure(foreground='white', background='#2C001E')
            self.label_location.configure(foreground='white', background='#2C001E')
        else:
            self.root.configure(background='white')


if __name__ == '__main__':
    root = tk.Tk()
    app = GreetApp(root)
    root.mainloop()
