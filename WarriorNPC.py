import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
import random

#Establish Random Array Pools
e = ['Fire', 'Water', 'Earth', 'Wind', 'Thunder', 'Light', 'Dark']
g = ['Male', 'Female', 'Non-binary', 'Herm', 'Genderfluid']
c = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Purple', 'Colorless']
h = ['Light', 'Medium','Heavy']
f = ['Factionless', 'Calix', 'Virgula', 'Gladius', 'Nummus']

#Create an Instance
win = tk.Tk()

#Add a Title
win.title('Warrior NPC Generator')

#Create Label for Name
NameLabel = ttk.Label(win,text = 'Name:')
NameLabel.grid(column=1, row=0, pady=5, padx=15)

#Create Text box for Name
NameBox = tk.StringVar()
NameEnter = ttk.Entry(win, width=25, textvariable = NameBox)
NameEnter.grid(column=2, row=0, pady=5, padx=15, columnspan=3)

#Create Label for Element
ElemLabel = ttk.Label(win, text = 'Element:')
ElemLabel.grid(column=1, row=2, pady=5, padx=15)

#Create Text Box for Element
ElemBox = tk.StringVar()
ElemEnter = ttk.Entry(win,width=12, textvariable = ElemBox)
ElemEnter.grid(column=3, row=2, pady=5, padx=15)

#Create Label for Gender
GenLabel = ttk.Label(win, text = 'Gender:')
GenLabel.grid(column=1, row=4, pady=5, padx=15)

#Create Text Box for Gender
GenBox = tk.StringVar()
GenEnter = ttk.Entry(win,width=12, textvariable = GenBox)
GenEnter.grid(column=3, row=4, pady=5, padx=15)

#Create Label for Color
ColorLabel = ttk.Label(win, text = 'Cosmic Color:')
ColorLabel.grid(column=1, row=6, pady=5, padx=15)

#Create Text Box for Color
ColorBox = tk.StringVar()
ColorEnter = ttk.Entry(win,width=12, textvariable = ColorBox)
ColorEnter.grid(column=3, row=6, pady=5, padx=15)

#Create Label for Health Tier
HealLabel = ttk.Label(win, text = 'Energy Tier:')
HealLabel.grid(column=1, row=8, pady=5, padx=15)

#Create Text Box for Health Tier
HealBox = tk.StringVar()
HealEnter = ttk.Entry(win,width=12, textvariable = HealBox)
HealEnter.grid(column=3, row=8, pady=5, padx=15)

#Create Label for Faction
FactLabel = ttk.Label(win, text = 'Faction:')
FactLabel.grid(column=1, row=10, pady=5, padx=15)

#Create Text Box for Element
FactBox = tk.StringVar()
FactEnter = ttk.Entry(win,width=12, textvariable = FactBox)
FactEnter.grid(column=3, row=10, pady=5, padx=15)

#Create Variable for Photo
loadbutton = PhotoImage(file = r'C:\Users\Bryson Keal\Desktop\Python\pngegg.png')

def Selection():
    #Set Variables
    Element = random.choice(e)
    Gender = random.choice(g)
    Color = random.choice(c)
    Health = random.choice(h)
    Faction = random.choice(f)
    
    #Delete information to Text Boxes
    ElemEnter.delete(0,'end')
    GenEnter.delete(0,'end')
    ColorEnter.delete(0,'end')
    HealEnter.delete(0,'end')
    FactEnter.delete(0,'end')
    
    #Add Information to Boxes
    ElemEnter.insert(10, Element)
    GenEnter.insert(10, Gender)
    ColorEnter.insert(10, Color)
    HealEnter.insert(10, Health)
    FactEnter.insert(10, Faction)
    
#Create Button
CycleButton = ttk.Button(win, image=loadbutton, command=Selection)
CycleButton.grid(column=2, row=12, pady=10, padx=20)

#Start GUI----
win.mainloop()
#-------------
