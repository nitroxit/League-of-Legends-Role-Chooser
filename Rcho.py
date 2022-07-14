from tkinter import *
import random
import os
from random import shuffle

master = Tk()
master.geometry('350x175')
master.resizable(False, False)
master.title('League of Legends Role Chooser')
master.configure(bg='#add123')
master.wm_attributes('-transparentcolor','#add123')
bg = PhotoImage(file = "stars.gif")
label1 = Label(master, image = bg)
label1.place(x = 0, y = 0)
global l1
global l2
global l3
global l4
global l5
l1 = Label(master, bg='white', text='Player 1')
l1.grid(row=0)
l2 = Label(master, bg='white', text='Player 2')
l2.grid(row=1)
l3 = Label(master, bg='white', text='Player 3')
l3.grid(row=2)
l4 = Label(master, bg='white', text='Player 4')
l4.grid(row=3)
l5 = Label(master, bg='white', text='Player 5')
l5.grid(row=4)
e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)
e4 = Entry(master)
e5 = Entry(master)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)
e5.grid(row=4, column=1)


lolroles = ['Top', 'Jungle', 'Mid', 'Bot/ADC', 'Support']

rand_lane1 = random.choice(lolroles)
lolroles.remove(rand_lane1)
rand_lane2 = random.choice(lolroles)
lolroles.remove(rand_lane2)
rand_lane3 = random.choice(lolroles)
lolroles.remove(rand_lane3)
rand_lane4 = random.choice(lolroles)
lolroles.remove(rand_lane4)
rand_lane5 = random.choice(lolroles)
lolroles.remove(rand_lane5)

aproles = ['Recon', 'Movement', 'Heals', 'Defense', 'Attack']

rand_role1 = random.choice(aproles)
aproles.remove(rand_role1)
rand_role2 = random.choice(aproles)
aproles.remove(rand_role2)
rand_role3 = random.choice(aproles)
aproles.remove(rand_role3)


def apex():
    l4.grid_remove()
    l5.grid_remove()
    e4.grid_remove()
    e5.grid_remove()
    apexbtn.grid_remove()
    aprrbtn.grid()
    lolbtn.grid()
    lolrrbtn.grid_remove()
    apdelbtn.grid()
    loldelbtn.grid_remove()
    
def lol():
    l4.grid()
    l5.grid()
    e4.grid()
    e5.grid()
    lolbtn.grid_remove()
    apexbtn.grid()
    aprrbtn.grid_remove()
    lolrrbtn.grid()
    apdelbtn.grid_remove()
    loldelbtn.grid()

    
def roll():
    shuffle(lolroles)
    os.system('cls')
    global lea1
    global lea2
    global lea3
    global lea4
    global lea5
    lea1 = Label(master, bg='white', text=e1.get() + ' --- ' + rand_lane1)
    lea1.grid(row=0, column=5)
    lea2 = Label(master, bg='white', text=e2.get() + ' --- ' + rand_lane2)
    lea2.grid(row=1, column=5)
    lea3 = Label(master, bg='white', text=e3.get() + ' --- ' + rand_lane3)
    lea3.grid(row=2, column=5)
    lea4 = Label(master, bg='white',text=e4.get() + ' --- ' + rand_lane4)
    lea4.grid(row=3, column=5)
    lea5 = Label(master, bg='white', text=e5.get() + ' --- ' + rand_lane5)
    lea5.grid(row=4, column=5)
    lolrrbtn["state"] = DISABLED

def aproll():
    shuffle(aproles)
    os.system('cls')
    global aplab1
    global aplab2
    global aplab3
    aplab1 = Label(master, bg='white', text=e1.get() + ' --- ' + rand_role1)
    aplab1.grid(row=0, column=5)
    aplab2 = Label(master, bg='white', text=e2.get() + ' --- ' + rand_role2)
    aplab2.grid(row=1, column=5)
    aplab3 = Label(master, bg='white', text=e3.get() + ' --- ' + rand_role3)
    aplab3.grid(row=2, column=5)
    aprrbtn["state"] = DISABLED

def lolclear():
    lea1.destroy()
    lea2.destroy()
    lea3.destroy()
    lea4.destroy()
    lea5.destroy()
    lolrrbtn["state"] = NORMAL

def apclear():
    aplab1.destroy()
    aplab2.destroy()
    aplab3.destroy()
    aprrbtn["state"] = NORMAL
    

aprrbtn = Button(master, text = 'Reroll', bg='aqua', command = aproll)
aprrbtn.grid(row=5, column=0)


lolrrbtn = Button(master, text = 'Reroll', bg='aqua', command = roll)
lolrrbtn.grid(row=5, column=0)


apexbtn = Button(master, text = 'Apex Mode', bg='aqua', command = apex)
apexbtn.grid(row=5, column=1)


lolbtn = Button(master, text='LoL Mode', bg='aqua', command = lol)
lolbtn.grid(row=5, column=1)
lolbtn.grid_remove()

loldelbtn = Button(master, text='Clear', bg='aqua', command = lolclear)
loldelbtn.grid(row=5, column=2)

apdelbtn = Button(master, text='Clear', bg='aqua', command = apclear)
apdelbtn.grid(row=5, column=2)
apdelbtn.grid_remove()



master.bind('<Return>', lambda event:roll())

mainloop()
