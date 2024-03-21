import customtkinter as ctk

from GUI.gamemode_select import GamemodeSelect

ctk.set_default_color_theme("dark-blue")

import tkinter as tk
from tkinter import ttk

class MainWindow():
    def __init__(self):
        self.window = ctk.CTk()
        self.window.title('Scorecast Wizzard')
        self.window.geometry('900x600')
        self.window.iconbitmap("Files/Icons/soccerBall.ico")
        self.gamemode_select = GamemodeSelect(self.window)
        self.gamemode_select.pack_select()

    def run(self):
        self.window.mainloop()




