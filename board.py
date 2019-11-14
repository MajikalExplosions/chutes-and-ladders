from tkinter import *

class Board(Frame):
    '''creates a Chutes and Ladders window'''

    def __init__(self,master):
        '''Board()
        creates a new board for Chutes and Ladders'''
        Frame.__init__(self,master)  # set up as a Tk frame
        self.grid()  # place the frame in the root window
        # create a label
        self.welcomeLabel = Label(self,text='How many players?')
        self.welcomeLabel.grid(row=0,column=0)
        # create a text display
        self.responseLabel = Label(self,text="")
        self.responseLabel.grid(row=2,column=0)

    def get_num_players(self):
        return 
        

root = Tk()
bd = Board(root)
bd.mainloop()
