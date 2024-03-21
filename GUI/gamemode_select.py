import customtkinter as ctk

class GamemodeSelect():
    def __init__(self, root):
        optionmenu_var = ctk.StringVar(value="National Teams")
        self.optionmenu = ctk.CTkOptionMenu(root, values=["National Teams", "Euro 2024"],
                                       command=self.optionmenu_callback,
                                       variable=optionmenu_var)
        self.root = root

    def optionmenu_callback(self, choice):
        print("optionmenu dropdown clicked:", choice)
        if choice == "National Teams":
            self.root.configure(fg_color='red')
        elif choice == "Euro 2024":
            self.root.configure(fg_color='blue')



    def pack_select(self):
        self.optionmenu.pack()