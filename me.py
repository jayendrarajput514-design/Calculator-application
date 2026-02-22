import tkinter as tk

window = tk.Tk()
window.title("Test Window")
window.geometry("300x200")

label = tk.Label(window, text="Tkinter is working!")
label.pack(pady=20)

window.mainloop()

