import tkinter as tk
import random

def phrase_generator():
    phrase = ["Hello", "Greetings", "Whats up"]
    name = str(entry1.get())
    random_phrase = phrase[random.randint(0, len(phrase)-1)]
    return f'{random_phrase} {name}'


def phrase_display():
    greeting = phrase_generator()

    # TEXTFIELD
    greeting_display = tk.Text(master=window, height=10, width=30)
    greeting_display.grid(column=0, row=3)

    greeting_display.insert(tk.END, greeting)





# --- TKINTER STUFF -----
window = tk.Tk()
window.title("Hello!")
window.geometry("400x400")


# LABELS
label1 = tk.Label(text="Welcome to my app")
label1.grid(column=0,row=0)

label2 = tk.Label(text="What is your name?")
label2.grid(column=0,row=1)


# ENTRIES
entry1 = tk.Entry()
entry1.grid(column=1, row=1)


# BUTTONS
button1 = tk.Button(text="Click Me!", command=phrase_display)
button1.grid(column=0, row=2)


window.mainloop()
