from tkinter import *
import random
import os
from random import shuffle

master = Tk()
master.title('League of Legends Role Chooser')
master.configure(bg='beige')
master.geometry('350x150')
Label(master, bg='beige', text='Player 1').grid(row=0)
Label(master, bg='beige', text='Player 2').grid(row=1)
Label(master, bg='beige', text='Player 3').grid(row=2)
Label(master, bg='beige', text='Player 4').grid(row=3)
Label(master, bg='beige', text='Player 5').grid(row=4)
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

def roll():
    shuffle(lolroles)
    os.system('cls')
    Label(master, bg='beige', text=e1.get() + ' --- ' + rand_lane1).grid(row=0, column=5)
    Label(master, bg='beige', text=e2.get() + ' --- ' + rand_lane2).grid(row=1, column=5)
    Label(master, bg='beige', text=e3.get() + ' --- ' + rand_lane3).grid(row=2, column=5)
    Label(master, bg='beige',text=e4.get() + ' --- ' + rand_lane4).grid(row=3, column=5)
    Label(master, bg='beige', text=e5.get() + ' --- ' + rand_lane5).grid(row=4, column=5)


btn = Button(master, text = 'Reroll', bg='aqua', command = roll)
btn.grid(row=5, column=1)


master.bind('<Return>', lambda event:prin())

mainloop()
