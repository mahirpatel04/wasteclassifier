import customtkinter
import tkinter as tk
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

# Creates a new window
root = customtkinter.CTk()

# Sets the window title
root.title("Where should I throw away my trash?")

# Sets the window size
width = "500"
height = "570"
root.geometry(width + "x" + height)

# Adds a label to the window
label = tk.Label(root, text="Hello, World!")
label.pack()

userWaste = ""

# BUTTON/ENTER EVENT
def button_event():
    global entry
    userWaste = entry.get()
    print(userWaste)
    
    # if statements to check for types of trash
    if "battery" in userWaste:
        print("you likely have battery in ur waste")
    
# ENTRY
entry = customtkinter.CTkEntry(master=root, width=200, height=50, corner_radius=10)
entry.place(relx=0.5, rely=0.4, anchor=customtkinter.CENTER)


# BUTTON
button = customtkinter.CTkButton(master=root, text="Classify My Waste", command=button_event, width=120, 
                                 height=32, border_width=0, corner_radius=8)
button.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)
entry.bind('<Return>', lambda event: button_event())










# Run the main loop to start the app
root.mainloop()

