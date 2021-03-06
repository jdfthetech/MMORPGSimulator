#! /usr/bin/python

#MMORPG Simulator

from tkinter import Tk, Label, Button, filedialog, simpledialog, Entry
import os
from PIL import Image, ImageTk
import random
import time

# gui class

class mmorpgGUI:
    def __init__(self, master):
    
       
        self.master = master
        master.title("MMORPG Simulator")
        
        
        screenWidth = master.winfo_screenwidth()
        screenHeight = master.winfo_screenheight()
        
        # adjust dimensions to middle of screen and make room for box
        
        xLocation = screenWidth / 2 - 245
        yLocation = screenHeight / 2 - 95    
        
        # have to convert to int because geometry doesn't like floats
        
        xLocation = int(xLocation)
        yLocation = int(yLocation)
        
        # specify geometry, must make coords a string normally looks like "490x190+220+200"
        
        master.geometry("720x500+"+str(xLocation)+"+"+str(yLocation))        
		        
        # using grid rather than pack to set buttons in correct spot

        self.name = Label(master, text="Enter Character Name:  ")        
        self.name.grid(column=0,row=0)
        
        self.nameEntry = Entry(master)
        self.nameEntry.insert(0,"Fire Squirrel")
        self.nameEntry.grid(column=1,row=0)
        self.nameEntry.config(font=("Freeserif", 24))

        # base stat rolls
        strStat = random.randint(3,18)
        dexStat = random.randint(3,18)
        conStat = random.randint(3,18)
        intStat = random.randint(3,18)
        wisStat = random.randint(3,18)
        chrStat = random.randint(3,18)

        imageFile = "shockedSquirrel_firesmall.png"
        load = Image.open(imageFile)
        load = load.resize((330,220), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)

        self.imageLabel = Label(master, image=render)
        self.imageLabel.image = render
        self.imageLabel.grid(column=1,row=1, columnspan = 4, rowspan = 5)


        # stat blocks

        self.strength = Label(master, text="Strength: "+str(strStat))        
        self.strength.grid(column=0,row=1, sticky='W')
        self.strength.config(font=("Freeserif", 20))
        self.strength.after(4000, self.refresh_str)

        self.dexterity = Label(master, text="Dexterity: "+str(dexStat))        
        self.dexterity.grid(column=0,row=2, sticky='W')
        self.dexterity.config(font=("Freeserif", 20))

        self.constitution = Label(master, text="Constitution: "+str(conStat))        
        self.constitution.grid(column=0,row=3, sticky='W')
        self.constitution.config(font=("Freeserif", 20))


        self.intelligence = Label(master, text="Intelligence: "+str(intStat))        
        self.intelligence.grid(column=5,row=1, sticky='W')
        self.intelligence.config(font=("Freeserif", 20))

        self.wisdom = Label(master, text="Wisdom: "+str(wisStat))        
        self.wisdom.grid(column=5,row=2, sticky='W')
        self.wisdom.config(font=("Freeserif", 20))

        self.charisma = Label(master, text="Charisma: "+str(chrStat))        
        self.charisma.grid(column=5,row=3, sticky='W')
        self.charisma.config(font=("Freeserif", 20))

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.grid(column=1,row=9, sticky ='NESW')
        
        # the timer test
        # will use this structure to update XP and level up stats

        self.var = strStat
        self.seconds = 0

        self.battle = 3

        self.timeLabel = Label(master, text="Test Timer: 0 s")
        self.timeLabel.grid(column=1,row=10, sticky='W')
        self.timeLabel.config(font=("Freeserif", 20))
        self.timeLabel.after(1000, self.timerTest_label)


        self.battleLabel = Label(master, text="No Battles Yet This Round")
        self.battleLabel.grid(column=1,row=11, sticky='W')
        self.battleLabel.config(font=("Freeserif", 14))
        self.battleLabel.after(4000, self.timerBattleLable)        
    
    # basic timer test

    def timerTest_label(self):
        self.seconds += 1
        self.timeLabel.configure(text="Test Timer: %i s" % self.seconds)
        self.timeLabel.after(1000, self.timerTest_label)

        # array loading

        self.weaponsArray = []
        self.enemyArray = []


        # randomly generate weapons and enemies

        with open('weaponNames') as input_file:
            for i, line in enumerate(input_file):
                #remove \n char
                n = len(line) - 1
                #build array of weapons
                self.weaponsArray.append(line[:n])

        with open('enemyNames') as input_file:
            for i, line in enumerate(input_file):
                #remove \n char
                n = len(line) - 1
                #build array of weapons
                self.enemyArray.append(line[:n])

        self.x = len(self.weaponsArray)
        self.weapon = random.randint(0,self.x)

        self.z = len(self.enemyArray)
        self.enemy = random.randint(0,self.z)

        # update strength test

    def refresh_str(self):
        self.var += 1
        self.strength.configure(text="Strength: %i" % self.var)
        self.strength.after(4000, self.refresh_str)


        # battle test

    def timerBattleLable(self):
        self.battle += 1
        self.battleLabel.configure(text=self.enemyArray[self.enemy]+" attacks with it's "+self.weaponsArray[self.weapon])
        self.battleLabel.after(4000, self.timerBattleLable)


# display gui and loop it    
if __name__ == "__main__":        
    root = Tk()
    my_gui = mmorpgGUI(root)
    root.mainloop()
