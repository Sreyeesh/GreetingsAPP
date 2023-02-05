import tkinter as tk
from tkinter import messagebox
import time
import geocoder

class GreetingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Greeting App")

        self.entry_frame = tk.Frame(self.root)
        self.entry_frame.grid(row=0, column=0, padx=10, pady=10)

        self.entry_label = tk.Label(self.entry_frame, text="Insert name:", font=("Arial", 14))
        self.entry_label.grid(row=0, column=0)

        self.name_entry = tk.Entry(self.entry_frame, font=("Arial", 14), width=20)
        self.name_entry.grid(row=0, column=1)
        self.name_entry.focus()
        self.name_entry.bind("<Return>", self.greet_user)

        self.button_frame = tk.Frame(self.root)
        self.button_frame.grid(row=1, column=0, padx=10, pady=10)

        self.greet_button = tk.Button(self.button_frame, text="Greet", font=("Arial", 14), command=self.greet_user)
        self.greet_button.grid(row=0, column=0, padx=10, pady=10)

        self.quit_button = tk.Button(self.button_frame, text="Quit", font=("Arial", 14), command=self.root.quit)
        self.quit_button.grid(row=0, column=1, padx=10, pady=10)

    def greet_user(self, event=None):
        name = self.name_entry.get().strip()
        try:
            if not name:
                raise ValueError("Please enter your name to continue")
            g = geocoder.ip('me')
            location = g.city + ", " + g.state
            current_time = time.strftime("%I:%M %p")
            greet = f"Hello {name}, it is currently {current_time} in {location}"
            messagebox.showinfo("Greeting", greet)
        except Exception as error:
            messagebox.showerror("Error", str(error))

if __name__ == "__main__":
    root = tk.Tk()
    app = GreetingApp(root)
    root.mainloop()
