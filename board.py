from tkinter import *

class Board(Frame):
    '''creates a Chutes and Ladders window'''

    def __init__(self,master):
        '''Board()
        creates a new board for Chutes and Ladders'''
        Frame.__init__(self,master)  # set up as a Tk frame
        self.grid()  # place the frame in the root window

        # variables
        self.numPlayers = 0
        
        # create labels
        self.welcomeLabel = Label(self,text = 'CHUTES AND LADDERS')
        self.welcomeLabel.grid(row=0,columnspan=4)
        self.playerLabel = Label(self,text='How many players?')
        self.playerLabel.grid(row=1,columnspan=4)

        # create options for numPlayers (1-4 players)
        self.player1 = Button(self,text='1',command=lambda:self.set_num_players(1))
        self.player1.grid(row=2,column = 0)
        self.player2 = Button(self,text='2',command=lambda:self.set_num_players(2))
        self.player2.grid(row=2,column = 1)
        self.player3 = Button(self,text='3',command=lambda:self.set_num_players(3))
        self.player3.grid(row=2,column = 2)
        self.player4 = Button(self,text='4',command=lambda:self.set_num_players(4))
        self.player4.grid(row=2,column = 3)

        self.next = Button(self,text='Play!',command=lambda:self.create_board(),state=DISABLED)
        self.next.grid(row=3,columnspan = 4)


    def set_num_players(self, x):
        '''set_num_players(self,x) -> takes in an integer (1,2,3,4)
            and stores it into numPlayers'''
        self.numPlayers = x
        self.playerLabel['text'] ='How many players?: '+str(x)
        self.next['state']=NORMAL
        

    def get_num_players(self):
        '''get_num_players(self) -> accessor method'''
        return self.numPlayers

    def create_board(self):
        '''create_board(self)->creates the "playing field"'''
        list = root.grid_slaves()
        for l in list:
            l.destroy()

        

root = Tk()
root.title('Chutes and Ladders')
bd = Board(root)
bd.mainloop()
