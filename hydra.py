import tkinter as tk
import threading

def new_window():
    root = tk.Tk()
    root.protocol("WM_DELETE_WINDOW", lambda: new_threads(root))
    root.geometry("300x300")
    title = tk.Label(root, text="HAIL HYDRA!", font="Arial 36 bold").pack()
    description = tk.Label(root, text="Kill 1, 2 more appear.", font="Arial 18").pack()
    root.mainloop()

def new_threads(root: tk.Tk):
    root.destroy()
    threading.Thread(target=new_window).start()
    threading.Thread(target=new_window).start()

threading.Thread(target=new_window).start()