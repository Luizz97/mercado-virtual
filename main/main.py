import tkinter as tk
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from projeto_livre.app import App

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x500")
    app = App(root)
    root.mainloop()
