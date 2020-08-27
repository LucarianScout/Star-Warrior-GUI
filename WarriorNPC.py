import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
import random

#Establish Random Array Pools
e = ['Fire', 'Water', 'Earth', 'Wind', 'Thunder', 'Light', 'Dark', 'No Element'] #Element
g = ['Male', 'Female', 'Non-binary', 'Herm', 'Genderfluid'] #Gender
c = ['Pink', 'Red', 'Burnt Orange', 'Orange', 'Amber', 'Yellow', 'Lime', 'Green', 'Cyan', 'Blue', 'Indigo', 'Purple', 'Colorless'] #Colors
h = ['Very Low','Low', 'Low-Medium','Medium','Medium-High','High', 'Very High'] #Energy Tier
f = ['Factionless', 'Calix', 'Virgula', 'Gladius', 'Nummus'] #Faction
i = ['Idiot', 'Uneducated', 'Below-Average', 'Average', 'Above-Average', 'Genius', 'Sage'] #Intelligence
p = ['Rugged', 'Lonely', 'Brave', 'Steadfast', 'Unruly', 'Daring', 'Obedient', 'Relaxed', 'Prankster', 'Careless', 'Timid', 'Hasty', 'Serious', 'Jolly', 'Naive', 'Humble', 'Mild', 'Quiet', 'Bashful', 'Reckless', 'Calm', 'Kind', 'Sassy', 'Carefree', 'Quirky']#Personality
d = ['Dismemberment', 'Cutting', 'Scratching', 'Bleedout', 'Hemorrhage', 'Disease', 'Poison', 'Multilation', 'Crushing', 'Burning', 'Freezing', 'Exploding', 'Age', 'Instant Death', 'Starvation', 'Dehydration', 'Trauma', 'Electrocution', 'Supernatural', 'Spiritual', 'Asphyxiation', 'Drowning', 'Suicide']#Method of Death
v = ['Chastity', 'Temperance', 'Charity', 'Diligence', 'Patience', 'Kindness', 'Humility']#Virtue
s = ['Lust', 'Gluttony', 'Greed', 'Sloth', 'Wrath', 'Envy', 'Pride']#Vice

#Create an Instance
win = tk.Tk()

#Add a Title
win.title('Warrior NPC Generator')

#Stop Window From being Resizable
win.resizable(0,0)

#Create Label for Name
NameLabel = ttk.Label(win,text = 'Name:')
NameLabel.grid(column=0, row=0, pady=5, padx=5, sticky='E')
#Create Text box for Name
NameBox = tk.StringVar()
NameEnter = ttk.Entry(win, width=49, textvariable = NameBox)
NameEnter.grid(column=1, row=0, pady=5, columnspan=6, sticky='W')

#Create Label for Element
ElemLabel = ttk.Label(win, text = 'Element:')
ElemLabel.grid(column=0, row=1, pady=5, padx=5, sticky = 'E')
#Create Text Box for Element
ElemBox = tk.StringVar()
ElemEnter = ttk.Entry(win,width=15, textvariable = ElemBox)
ElemEnter.grid(column=1, row=1, pady=5, sticky ='W')
#Create Checkbox for Element
Elock = tk.IntVar()
lockE = tk.Checkbutton(win, text="Lock", offvalue=0, onvalue=1, variable=Elock)
lockE.deselect()
lockE.grid(column=2, row=1, sticky='W')

#Create Label for Gender
GenLabel = ttk.Label(win, text = 'Gender:')
GenLabel.grid(column=4, row=1, pady=5, padx=5, sticky = 'E')
#Create Text Box for Gender
GenBox = tk.StringVar()
GenEnter = ttk.Entry(win,width=15, textvariable = GenBox)
GenEnter.grid(column=5, row=1, pady=5, padx=5, sticky='W')
#Create Checkbox for Gender
Glock = tk.IntVar()
lockG = tk.Checkbutton(win, text="Lock", offvalue=0, onvalue=1, variable=Glock)
lockG.deselect()
lockG.grid(column=6, row=1, sticky='W')

#Create Label for Color
ColorLabel = ttk.Label(win, text = 'Cosmic Color:')
ColorLabel.grid(column=0, row=2, pady=5, padx=5, sticky = 'E')
#Create Text Box for Color
ColorBox = tk.StringVar()
ColorEnter = ttk.Entry(win,width=15, textvariable = ColorBox)
ColorEnter.grid(column=1, row=2, pady=5, sticky ='W')
#Create Checkbox for Color
Clock = tk.IntVar()
lockC = tk.Checkbutton(win, text="Lock", offvalue=0, onvalue=1, variable=Clock)
lockC.deselect()
lockC.grid(column=2, row=2, sticky='W')

#Create Label for Health Tier
HealLabel = ttk.Label(win, text = 'Energy Tier:')
HealLabel.grid(column=0, row=3, pady=5, padx=5, sticky = 'E')
#Create Text Box for Health Tier
HealBox = tk.StringVar()
HealEnter = ttk.Entry(win,width=15, textvariable = HealBox)
HealEnter.grid(column=1, row=3, pady=5, sticky ='W')
#Create Checkbox for Health Tier
Hlock = tk.IntVar()
lockH = tk.Checkbutton(win, text="Lock", offvalue=0, onvalue=1, variable=Hlock)
lockH.deselect()
lockH.grid(column=2, row=3, sticky='W')

#Create Label for Faction
FactLabel = ttk.Label(win, text = 'Faction:')
FactLabel.grid(column=4, row=2, pady=5, padx=5, sticky = 'E')
#Create Text Box for Faction
FactBox = tk.StringVar()
FactEnter = ttk.Entry(win,width=15, textvariable = FactBox)
FactEnter.grid(column=5, row=2, pady=5, padx=5, sticky='W')
#Create Checkbox for Faction
Flock = tk.IntVar()
lockF = tk.Checkbutton(win, text="Lock", offvalue=0, onvalue=1, variable=Flock)
lockF.deselect()
lockF.grid(column=6, row=2, sticky='W')

#Create Label for Intelligence
IntLabel = ttk.Label(win, text = 'Intelligence:')
IntLabel.grid(column=0, row=4, pady=5, padx=5, sticky = 'E')
#Create Text Box for Intelligence
IntBox = tk.StringVar()
IntEnter = ttk.Entry(win,width=15, textvariable = IntBox)
IntEnter.grid(column=1, row=4, pady=5, sticky ='W')
#Create Checkbox for Intelligence
Ilock = tk.IntVar()
lockI = tk.Checkbutton(win, text="Lock", offvalue=0, onvalue=1, variable=Ilock)
lockI.deselect()
lockI.grid(column=2, row=4, sticky='W')

#Create Label for Method of Death
DeathLabel = ttk.Label(win, text = 'Method of Death:')
DeathLabel.grid(column=4, row=3, pady=5, padx=5, sticky = 'E')
#Create Text Box for Method of Death
DeathBox = tk.StringVar()
DeathEnter = ttk.Entry(win,width=15, textvariable = DeathBox)
DeathEnter.grid(column=5, row=3, pady=5, padx=5, sticky='W')
#Create Checkbox for Death
Dlock = tk.IntVar()
lockD = tk.Checkbutton(win, text="Lock", offvalue=0, onvalue=1, variable=Dlock)
lockD.deselect()
lockD.grid(column=6, row=3, sticky='W')

#Create Label for Method of Personality
PersLabel = ttk.Label(win, text = 'Personality:')
PersLabel.grid(column=4, row=4, pady=5, padx=5, sticky = 'E')
#Create Text Box for Personality
PersBox = tk.StringVar()
PersEnter = ttk.Entry(win,width=15, textvariable = PersBox)
PersEnter.grid(column=5, row=4, pady=5, padx=5, sticky='W')
#Create Checkbox for Personality
Plock = tk.IntVar()
lockP = tk.Checkbutton(win, text="Lock", offvalue=0, onvalue=1, variable=Plock)
lockP.deselect()
lockP.grid(column=6, row=4, sticky='W')

#Create Label for Method of Virtue
VirLabel = ttk.Label(win, text = 'Virtue:')
VirLabel.grid(column=0, row=5, pady=5, padx=5, sticky = 'E')
#Create Text Box for Virtue
VirBox = tk.StringVar()
VirEnter = ttk.Entry(win,width=15, textvariable = VirBox)
VirEnter.grid(column=1, row=5, pady=5, sticky='W')
#Create Checkbox for Virtue
Vlock = tk.IntVar()
lockV = tk.Checkbutton(win, text="Lock", offvalue=0, onvalue=1, variable=Vlock)
lockV.deselect()
lockV.grid(column=2, row=5, sticky='W')

#Create Label for Method of Sin
SinLabel = ttk.Label(win, text = 'Vice:')
SinLabel.grid(column=4, row=5, pady=5, padx=5, sticky = 'E')
#Create Text Box for Sin
SinBox = tk.StringVar()
SinEnter = ttk.Entry(win,width=15, textvariable = SinBox)
SinEnter.grid(column=5, row=5, pady=5, padx=5, sticky='W')
#Create Checkbox for Sin
Slock = tk.IntVar()
lockS = tk.Checkbutton(win, text="Lock", offvalue=0, onvalue=1, variable=Slock)
lockS.deselect()
lockS.grid(column=6, row=5, sticky='W')

#Create Variable for Photo
#loadbutton = PhotoImage(file = r'C:\Users\Bryson Keal\Desktop\Python\pngegg.png')
#xbutton=PhotoImage(file = r'C:\Users\Bryson Keal\Desktop\Python\x-icon-vector-7.png')
def Selection():
    #Set Variables
    if Elock.get() == 0:
        Element = random.choice(e)
        ElemEnter.delete(0,'end')
        ElemEnter.insert(10, Element)
        
    if Glock.get() == 0:
        Gender = random.choice(g)
        GenEnter.delete(0,'end')
        GenEnter.insert(10, Gender)
        
    if Clock.get() == 0:
        Color = random.choice(c)
        ColorEnter.delete(0,'end')
        ColorEnter.insert(10, Color)
        
    if Hlock.get() == 0:
        Health = random.choice(h)
        HealEnter.delete(0,'end')
        HealEnter.insert(10, Health)
        
    if Flock.get() == 0:
        Faction = random.choice(f)
        FactEnter.delete(0,'end')
        FactEnter.insert(10, Faction)
        
    if Ilock.get() == 0:
        Intelligence = random.choice(i)
        IntEnter.delete(0,'end')
        IntEnter.insert(10, Intelligence)
        
    if Dlock.get() == 0:
        Death = random.choice(d)
        DeathEnter.delete(0,'end')
        DeathEnter.insert(10,Death)
        
    if Plock.get() == 0:
        Personality = random.choice(p)
        PersEnter.delete(0,'end')
        PersEnter.insert(10, Personality)
        
    if Vlock.get() == 0:
        Virtue = random.choice(v)
        VirEnter.delete(0,'end')
        VirEnter.insert(10, Virtue)
        
    if Slock.get() == 0:
        Sin = random.choice(s)
        SinEnter.delete(0,'end')
        SinEnter.insert(10, Sin)
    

def Clear():
    #Delete information to Text Boxes
    ElemEnter.delete(0,'end')
    lockE.deselect()
    GenEnter.delete(0,'end')
    lockG.deselect()
    ColorEnter.delete(0,'end')
    lockC.deselect()
    HealEnter.delete(0,'end')
    lockH.deselect()
    FactEnter.delete(0,'end')
    lockF.deselect()
    IntEnter.delete(0,'end')
    lockI.deselect()
    DeathEnter.delete(0,'end')
    lockD.deselect()
    PersEnter.delete(0,'end')
    lockP.deselect()
    VirEnter.delete(0,'end')
    lockV.deselect()
    SinEnter.delete(0,'end')
    lockS.deselect()
    
#Create Cycle Button
CycleButton = ttk.Button(win, text = 'Refresh', command=Selection)
CycleButton.grid(column=0, row=6, pady=10)

#Create Clear Button
ClearButton = ttk.Button(win,text = 'Reset', command=Clear)
ClearButton.grid(column = 6, row=6, pady=10, padx=3)

#Start GUI----
win.mainloop()
#-------------
