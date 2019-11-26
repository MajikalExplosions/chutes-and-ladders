from tkinter import *

class Board(Frame):
    '''creates a new Chutes and Ladders game'''

    def __init__(self,master):
        '''Board()
        creates a new board for Chutes and Ladders'''
        Frame.__init__(self,master,width=800,height=800,bg="white")  # set up as a Tk frame
        self.pack_propagate(0)
        self.grid()  # place the frame in the root window

        # variables
        self.numPlayers = 0

        # First, the welcome screen:
        # create labels
        self.welcomeLabel = Label(self,text = 'CHUTES AND LADDERS',font = "Verdana 30 bold", fg = "Cadet Blue")
        self.welcomeLabel.grid(row=0,columnspan=4)
        self.playerLabel = Label(self,text='How many players?',font=("Calibri"))
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

        # Second: the actual game screen. Nothing is gridded yet (will be gridded in create_board)
        # title
        self.title = Label(self,text = 'CHUTES AND LADDERS',font = "Verdana 30 bold", fg = "Cadet Blue")

        #game announcer/commentator
        self.text = StringVar()
        self.comments = Label(self,height=37, width = 30,textvariable = self.text, font=("Calibri"), fg="White", bg = "Dark Grey")
        self.text.set("Welcome to Chutes and Ladders!\nThere are " + str(self.numPlayers) +" players playing in this game.\n")
        
        #game board
        self.boardGIF = PhotoImage(file="gameBoard.gif")
        self.board = Label(self,image=self.boardGIF)

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
        '''create_board(self)->destroys the current welcome screen,
            creates the actual playing board'''
        # destroy the current screen
        list = self.grid_slaves()
        for l in list:
            l.destroy()
        self.board.grid(row=1,column=0)
        self.title.grid(row=0,columnspan=3)
        self.comments.grid(row = 1,column=3)
        self.update_comments("hi")
        self.update_comments("hi")
        self.update_comments("hi")
        self.update_comments("hi")
        self.update_comments("hi")
        self.update_comments("hi")
        self.update_comments("hi")
        self.update_comments("hi")
        self.update_comments("hi")
        self.update_comments("hi")
        self.update_comments("hi")
        self.update_comments("hi")
        self.update_comments("hi")
        self.update_comments("hi")
        self.update_comments("hi")
        self.update_comments("hi")
        self.update_comments("hi")
        self.update_comments("hi")          #don't mind this haha. just trying to debug the comments :)
        self.update_comments("hi")
        self.update_comments("hi")
        self.update_comments("hi")
        self.update_comments("hi")
        self.update_comments("hi")
        self.update_comments("hi")
        self.update_comments("hi")
        self.update_comments("hi")
        self.update_comments("hi")
        self.update_comments("hi")
        self.update_comments("hi")
        self.update_comments("hi")
        self.update_comments("hi")
        self.update_comments("hi")
        self.update_comments("hi")
        self.update_comments("hi")
        self.update_comments("hi")
        self.update_comments("hi")
        self.update_comments("hi")
        self.update_comments("hi")
        self.update_comments("hi")
        self.update_comments("woah")
        
        
        
        
    def update_comments(self, x):
        '''updates commentary text box'''
        self.text.set(str(self.text.get()) + "\n" + str(x))




class ChutesAndLadders:
    '''represents a game of Chutes and ladders'''

    def __init__(self):
        #set up welcome screen
        root = Tk()
        root.title('Chutes and Ladders')
        bd = Board(root)
        bd.mainloop()
        

        

ChutesAndLadders()
