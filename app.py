import tkinter as tk
import time
import platform

def greet_user():
    name = entry.get()
    current_time = time.strftime("%H:%M:%S")
    greet = "Hello " + name + ", it's " + current_time + " here."
    label.config(text=greet)

app = tk.Tk()
app.geometry("300x100")
app.configure(bg=app.cget("bg"))
app.title("Greeting App")

label = tk.Label(text="", font=("Arial", 14), bg=app.cget("bg"), fg="black")
label.pack()

entry = tk.Entry(font=("Arial", 14), bg="white")
entry.pack(pady=10)

greet_button = tk.Button(text="Greet", font=("Arial", 14), command=greet_user)
greet_button.pack()

app.mainloop()
