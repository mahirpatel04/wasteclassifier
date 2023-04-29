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

#Creates the introFrame
introFrame = customtkinter.CTkFrame(root)

# Adds a label to the frame
label = tk.Label(introFrame, text="Hello, World!")
label.pack()

userWaste = ""



# BUTTON/ENTER EVENT
def button_event():
    global entry
    userWaste = entry.get()
    print(userWaste)
    
    # if statements to check for types of trash
    if "battery" in userWaste:
        battery()
            
    
# ENTRY
entry = customtkinter.CTkEntry(master=introFrame, width=200, height=50, corner_radius=10)
entry.place(relx=0.5, rely=0.4, anchor=customtkinter.CENTER)


# BUTTON
button = customtkinter.CTkButton(master=introFrame, text="Classify My Waste", command=button_event, width=120, 
                                 height=32, border_width=0, corner_radius=8)
button.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)
entry.bind('<Return>', lambda event: button_event())

#different frames depending on the type of waste
batteryFrame = customtkinter.CTkFrame(root)
battery_label = tk.Label(batteryFrame, text="Battery Info Goes Here")

glassFrame = customtkinter.CTkFrame(root)

#different types of wastes and their pages

def battery():
    introFrame.pack_forget()
    batteryFrame.pack()
    





introFrame.pack()


# Run the main loop to start the app
root.mainloop()

