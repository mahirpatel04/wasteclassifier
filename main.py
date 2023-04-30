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
introFrame = customtkinter.CTkFrame(root, width = 10000, height = 10000)

# Adds a label to the frame
label = customtkinter.CTkLabel(master=introFrame, text="WASTE MANAGEMENT APP", fg_color=('white' ,"green"), corner_radius=8, height=30, width=400, font=("Helvetica", 24) )
label.place(relx=0.5, rely=0.05, anchor=customtkinter.CENTER)

# Text box for intro
textbox = customtkinter.CTkTextbox(master=introFrame, height=6, width=100, corner_radius=8)
textbox.place(relx=0.5, rely=0.42, anchor=customtkinter.CENTER, relwidth=0.9, relheight=0.62)
# Insert text into the text box
textbox.insert(tk.END,"Why this app?", )
textbox.insert(tk.END,"\n Throwing away garbage in the United States is broken. This has become a problem for us, as Americans produces 3 times as much garbage as the global average. One misplaced item can contaminate a full truckload of wastes, which is exteremly harmful to our environment. But why are people still at risk on misplacing their wastes? From our personal experience we realized that many people don't exactly know which bin they should throw their wastes. So hence this app was created. We created this app to educate and direct unsure users where to throw their wastes. All they need to do is type in the item they want to dispose and our databases will direct the user which bin to dispose it in. We hope this app becomes an effiencient tool substain our environment. ", )
textbox.tag_config("center", justify='center')
textbox.tag_add("center", "1.0", "end")
textbox.configure(state="disabled", height= 12, width=50)

userWaste = ""
currentFrame = introFrame


# BUTTON/ENTER EVENT
def originalButton():
    global entry
    userWaste = entry.get()
   
    trashables = []
    compostables = []
    hazardouses = []
    recyclables = []
   

    with open('WasteClassificationApp/recyclable.txt', 'r') as file1:
        recyclables = file1.read().split('\n')
    with open('WasteClassificationApp/trashable.txt', 'r') as file2:
        trashables = file2.read().split('\n')
    with open('WasteClassificationApp/compostable.txt', 'r') as file3:
        compostables = file3.read().split('\n')
    with open('WasteClassificationApp/hazardous.txt', 'r') as file4:
        hazardouses = file4.read().split('\n')

    for recyclable in recyclables:
        if recyclable == userWaste.lower():
            recycle()
            currentFrame = recycleFrame
            return
    for trashable in trashables:
        if trashable == userWaste.lower():
            trash()
            currentFrame = trashFrame
            return
    for compostable in compostables:
        if compostable == userWaste.lower():
            compost()
            currentFrame = compostFrame
            return
    for hazardous in hazardouses:
        if hazardous == userWaste.lower():
            hazard()
            currentFrame = hazardFrame
            return
    else:
        notAvailable()
        currentFrame = notAvailableFrame
        return
    
    currentFrame = introFrame



# ENTRY
entry = customtkinter.CTkEntry(master=introFrame, width=200, height=50, corner_radius=10)
entry.place(relx=0.5, rely=0.8, anchor=customtkinter.CENTER)



# BUTTON
button = customtkinter.CTkButton(master=introFrame, text="Classify My Waste", command=originalButton, width=120, 
                                 height=32, border_width=0, corner_radius=8)
button.place(relx=0.5, rely=0.93, anchor=customtkinter.CENTER)
entry.bind('<Return>', lambda event: originalButton())

def returnButton(currentFrame):
    returnButton = customtkinter.CTkButton(master=currentFrame, text="Return to home", command=lambda: leaveButton(currentFrame), width=120,
                                           height=32, border_width=0, corner_radius=8)
    returnButton.place(relx=0.5, rely=0.8, anchor=customtkinter.CENTER)


#different frames depending on the type of waste

recycleFrame = customtkinter.CTkFrame(root, width = 10000, height = 10000)
label = customtkinter.CTkLabel(master=recycleFrame, text="RECYCLING", fg_color=('white', "#3276ed"), corner_radius=8, height=60, width=180, font=("Helvetica", 24))
label.place(relx=0.28, rely=0.1, anchor=customtkinter.CENTER)
# Text box
textbox = customtkinter.CTkTextbox(master=recycleFrame, height=40, width=120, corner_radius=8)
textbox.place(relx=0.5, rely=0.65, anchor=customtkinter.CENTER, relwidth=0.8, relheight=0.6)
# Insert text into the text box
textbox.insert(tk.END,"This item will be recyled due to it being one of these options:\n 1. Plastic Bottles & Containers\n 2. Food & Beverage Cans \n 3. Paper \n 4. Flattened Cardboard & Paperboard\n 5. Food & Beverage Containers\n 6.Glass Bottles & Containers")
textbox.insert(tk.END, "\n\n More information will be found here:\n https://www.wm.com/us/en/recycle-right/recycling-101")
textbox.configure(state="disabled", height= 120, width=500)
returnButton(recycleFrame)

trashFrame = customtkinter.CTkFrame(root, width = 10000, height = 1000)
label = customtkinter.CTkLabel(master=trashFrame, text="TRASH", fg_color=('white', "#121111"), corner_radius=8, height=60, width=180, font=("Helvetica", 24))
label.place(relx=0.28, rely=0.1, anchor=customtkinter.CENTER)
# Text box
textbox = customtkinter.CTkTextbox(master=trashFrame, height=40, width=120, corner_radius=8)
textbox.place(relx=0.5, rely=0.65, anchor=customtkinter.CENTER, relwidth=0.8, relheight=0.6)
# Insert text into the text box
textbox.insert(tk.END,"This item will be composted due to it being one of these options:\n 1. Liner bags (cereal, cookies, crackers)\n 2. Plastic bubble wrap  \n 3. Popsicle sticks, toothpicks, wood chips, and pencil shaving \n 4. Light bulbs (not CFLs), dishes and drinking glasses\n 5. Plastic or foil wrappers and aluminum foil\n 6. Laminated plastic film(stand-up pouches, snack food bags)\n 7. Hot drink cups")
textbox.insert(tk.END, "\n\n More information will be found here:\n https://www.garbageday.com/gd/garbage-tips/blue-green-or-black-bin-heres-the-full-meaning/")
textbox.configure(state="disabled", height= 120, width=500)
returnButton(trashFrame)

compostFrame = customtkinter.CTkFrame(root, width = 10000, height = 10000)
label = customtkinter.CTkLabel(master=compostFrame, text="COMPOST", fg_color=('white', "#099c2b"), corner_radius=8, height=60, width=180, font=("Helvetica", 24))
label.place(relx=0.28, rely=0.1, anchor=customtkinter.CENTER)
# Text box
textbox = customtkinter.CTkTextbox(master=compostFrame, height=40, width=120, corner_radius=8)
textbox.place(relx=0.5, rely=0.65, anchor=customtkinter.CENTER, relwidth=0.8, relheight=0.6)
# Insert text into the text box
textbox.insert(tk.END,"This item will be composted due to it being one of these options:\n 1. NewsPapers\n 2. Leaves/yard waste  \n 3. Veggie and fruit scraps \n 4. Egg shells (crushed)\n 5. Coffee grounds\n 6. Tissues, paper towels, napkins\n 7. Herbivore manure")
textbox.insert(tk.END, "\n\n More information will be found here:\n https://www.azdeq.gov/what-can-and-cant-i-compost-compost-guide")
textbox.configure(state="disabled", height= 120, width=500)
returnButton(compostFrame)

hazardFrame = customtkinter.CTkFrame(root, width=10000, height=10000 )
label = customtkinter.CTkLabel(master=hazardFrame, text="HAZARDOUS WASTE", fg_color=('white', "#d10404"), corner_radius=8, height=60, width=180, font=("Helvetica", 24))
label.place(relx=0.28, rely=0.1, anchor=customtkinter.CENTER)
# Text box
textbox = customtkinter.CTkTextbox(master=hazardFrame, height=40, width=120, corner_radius=8)
textbox.place(relx=0.5, rely=0.65, anchor=customtkinter.CENTER, relwidth=0.8, relheight=0.6)
# Insert text into the text box
textbox.insert(tk.END,"This item will be recyled due to it being one of these options:\n 1. Fluorescent lamps\n 2. Cathode ray tubes \n 3. Instruments that contain mercury, batteries, and others. \n 4. Paint\n 5. Motor Oil\n 6. Electronics")
textbox.insert(tk.END, "\n\n More information will be found here:\n https://calrecycle.ca.gov/homehazwaste/")
textbox.configure(state="disabled", height= 120, width=500)
returnButton(hazardFrame)

notAvailableFrame = customtkinter.CTkFrame(root, width = 10000, height = 10000)
notAvailableLabel = customtkinter.CTkLabel(notAvailableFrame, text="Your waste cannot be classified at this moment, please try again")
notAvailableLabel.place(relx=0.5, rely=0.1, anchor=customtkinter.CENTER)
returnButton(notAvailableFrame)


#different types of wastes and their pages

def recycle():
    introFrame.pack_forget()
    currentFrame = recycleFrame
    currentFrame.pack()
    
    
def trash():
    introFrame.pack_forget()
    currentFrame = trashFrame
    currentFrame.pack()

def compost():
    introFrame.pack_forget()
    currentFrame = compostFrame
    compostFrame.pack()

def hazard():
    introFrame.pack_forget()
    currentFrame = hazardFrame
    currentFrame.pack()

def notAvailable():
    introFrame.pack_forget()
    currentFrame = notAvailableFrame
    currentFrame.pack()
    
def leaveButton(currentFrame):
    currentFrame.pack_forget()
    introFrame.pack()


introFrame.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER, relwidth = 0.8 , relheight = 0.8)


# Run the main loop to start the app
root.mainloop()

