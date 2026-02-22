import tkinter as tk

# ---------- COLORS ----------
BG_COLOR = "#1e1e1e"
DISPLAY_BG = "#2b2b2b"
BTN_BG = "#f2c94c"        # matte yellow
BTN_TEXT = "#000000"
DISPLAY_TEXT = "#ffffff"

# ---------- WINDOW ----------
window = tk.Tk()
window.title("Calculator")
window.geometry("320x450")
window.configure(bg=BG_COLOR)
window.resizable(True, True)

# Grid expand
for i in range(6):
    window.rowconfigure(i, weight=1)
for j in range(4):
    window.columnconfigure(j, weight=1)

# ---------- DISPLAY ----------
display = tk.Entry(
    window,
    font=("Segoe UI", 22),
    bg=DISPLAY_BG,
    fg=DISPLAY_TEXT,
    insertbackground=DISPLAY_TEXT,
    borderwidth=0,
    justify="right"
)
display.grid(row=0, column=0, columnspan=4,
             padx=12, pady=12, sticky="nsew")

# ---------- FUNCTIONS ----------
def button_click(value):
    display.insert(tk.END, value)

def clear():
    display.delete(0, tk.END)

def backspace():
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current[:-1])

def calculate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, result)
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")

# ---------- KEYBOARD SUPPORT ----------
def key_input(event):
    if event.char in "0123456789+-*/.":
        button_click(event.char)
    elif event.keysym == "Return":
        calculate()
    elif event.keysym == "BackSpace":
        backspace()
    elif event.keysym == "Escape":
        clear()

window.bind("<Key>", key_input)

# ---------- BUTTON FONT ----------
btn_font = ("Segoe UI Semibold", 16)

# ---------- BUTTON LAYOUT ----------
buttons = [
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3),
    ('0', 5, 0), ('.', 5, 1), ('=', 5, 2), ('+', 5, 3)
]

# ---------- TOP BUTTONS ----------
tk.Button(
    window, text="C", font=btn_font,
    bg="#ff6b6b", fg="white", borderwidth=0,
    command=clear
).grid(row=1, column=0, padx=6, pady=6, sticky="nsew")

tk.Button(
    window, text="⌫", font=btn_font,
    bg="#6c757d", fg="white", borderwidth=0,
    command=backspace
).grid(row=1, column=1, columnspan=3,
       padx=6, pady=6, sticky="nsew")

# ---------- CREATE BUTTONS ----------
for (text, row, col) in buttons:
    if text == '=':
        btn = tk.Button(
            window, text=text, font=btn_font,
            bg="#27ae60", fg="white", borderwidth=0,
            command=calculate
        )
    else:
        btn = tk.Button(
            window, text=text, font=btn_font,
            bg=BTN_BG, fg=BTN_TEXT, borderwidth=0,
            activebackground="#e0b84a",
            command=lambda t=text: button_click(t)
        )

    btn.grid(row=row, column=col,
             padx=6, pady=6, sticky="nsew")

window.mainloop()
