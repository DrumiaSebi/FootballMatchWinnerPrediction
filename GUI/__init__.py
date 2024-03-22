from .main_window import MainWindow

import customtkinter as ctk
from PIL import Image, ImageTk


ctk.set_default_color_theme("dark-blue")
font_size = 25
font = "Comic Sans MS"
menu_border_width = 5
button_iypad = 4

window = ctk.CTk()
window.title('Scorecast Wizzard')
window.geometry('600x450')
window.minsize(600,450)
window.iconbitmap("Files/Icons/soccerBall.ico")


#layouts
menu_frame = ctk.CTkFrame(window, border_width = menu_border_width, border_color= '#1F1C6D')
main_frame = ctk.CTkFrame(window, fg_color = 'blue')

#placing frames
menu_frame.place(x = 0, y = 0, relwidth = 0.3, relheight = 1)
main_frame.place(relx = 0.3, y = 0, relwidth = 0.7, relheight = 1)


#preparing images for menu buttons
random_teams_image = ctk.CTkImage(
    light_image=Image.open("Files/ButtonsIcons/randomTeams.png"),
    dark_image=Image.open("Files/ButtonsIcons/randomTeams.png"))
change_background_image = ctk.CTkImage(
    light_image=Image.open("Files/ButtonsIcons/changeBackground.png"),
    dark_image=Image.open("Files/ButtonsIcons/changeBackground.png"))
update_data_image = ctk.CTkImage(
    light_image=Image.open("Files/ButtonsIcons/updateTeams.png"),
    dark_image=Image.open("Files/ButtonsIcons/updateTeams.png"))

#menu_widgets
menu_label = ctk.CTkLabel(menu_frame, text = "Menu", font = (font, font_size))
menu_button_randomise = ctk.CTkButton(menu_frame, text = "Random teams       ", image=random_teams_image, compound='right')
menu_button_change_bg = ctk.CTkButton(menu_frame, text = "Change background  ", image=change_background_image, compound='right')
menu_button_update_data = ctk.CTkButton(menu_frame, text = "Update teams data    ", image=update_data_image, compound='right')

#menu layout
menu_frame.columnconfigure(0, weight = 1)
menu_frame.columnconfigure(1, weight = 5)
menu_frame.columnconfigure(2, weight = 1)

# menu_frame.rowconfigure((0,1,2,3,4,5), weight = 1)
menu_frame.rowconfigure(0, weight = 2)
menu_frame.rowconfigure((1,2,3,4), weight = 1)
menu_frame.rowconfigure(5, weight = 5)

#placing buttons on the menu
menu_label.grid(row = 0, column = 0, columnspan = 3, sticky ='n', pady = menu_border_width)
menu_button_randomise.grid(row = 1, column = 1, sticky = 'nwe', ipady = button_iypad)
menu_button_change_bg.grid(row = 2, column = 1, sticky = 'nwe', ipady = button_iypad)
menu_button_update_data.grid(row = 3, column = 1, sticky = 'nwe', ipady = button_iypad)



#creating canvas for main_frame

# button_image = ctk.CTkButton(main_frame, text = "Button image", image=image_tk)
# button_image.pack()


window.mainloop()

# main_window = MainWindow()
# main_window.run()