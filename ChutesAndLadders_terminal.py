import random


def roll_dice():
    # simulates the rolling of a six-sided die
    return random.randint(1, 6)


def starting_player(player_count):
    # determines which player gets the first turn
    return random.randint(0, player_count - 1)


class ChutesAndLadders:
    def __init__(self, player_count):
        self.turns_committed = 0
        self.player_count = player_count
        self.players = list()
        self.player_spaces = dict()
        self.chutes = {34: 2, 38: 3, 46: 33, 56: 39, 57: 44, 59: 45}
        self.ladders = {4: 20, 5: 10, 7: 23, 14: 30, 18: 35, 22: 39, 27: 37, 41: 58, 42: 53, 49: 62}

    def player_creation(self):
        # makes the list of players that are in the game
        current_iteration = 1
        while current_iteration <= self.player_count:
            self.players.append('Player ' + str(current_iteration))
            current_iteration += 1

    def ladder_chute_movement(self, current_player):
        # options for if the players fall on a ladder or chute space
        if self.player_spaces.get(current_player) in self.ladders.keys():
            print('{} landed on a ladder! Move up to space {}.'.format(current_player, self.ladders.get(
                self.player_spaces[current_player])))
            self.player_spaces[current_player] = self.ladders.get(self.player_spaces[current_player])

        elif self.player_spaces.get(current_player) in self.chutes.keys():
            print('{}} landed on a chute, move down to space {}.'.format(current_player, self.chutes.get(
                self.player_spaces[current_player])))
            self.player_spaces[current_player] = self.chutes.get(self.player_spaces[current_player])


class StartGame:
    def __init__(self):

        # creates the game, sets up the variables and modules
        player_count = int(input('Players: '))
        cal = ChutesAndLadders(player_count)
        cal.player_creation()

        # names all the players
        for player in cal.players:
            cal.players[cal.players.index(player)] = input('{} name: '.format(player))

        # determines the first player using the starting player function
        first_player = cal.players[starting_player(player_count)]
        current_player = first_player

        for player in cal.players:
            cal.player_spaces[player] = 0

        while True:
            # keep playing as long as no one has reached the finish line
            win = None
            winning_player = None
            winning_space = list()

            for player_space in cal.player_spaces.values():
                if player_space < 63:
                    winning_space.append(False)
                else:
                    # indexes the winning player's space and return's the player's name to the winning_player variable
                    winning_player = \
                        list(cal.player_spaces.keys())[list(cal.player_spaces.values()).index(player_space)]

            if winning_space.count(False) == cal.player_count:
                win = False
            else:
                win = True

            if win is False:
                current_player_move = str(input(current_player + "'s move (forwards or backwards): "))
                print(current_player_move)

                # gives the option of moving forwards or backwards in an attempt to get the ladders
                if current_player_move == 'forwards':
                    cal.player_spaces[current_player] += roll_dice()
                    cal.ladder_chute_movement(current_player)

                elif current_player_move == 'backwards':
                    cal.player_spaces[current_player] -= roll_dice()
                    cal.ladder_chute_movement(current_player)

                print(cal.player_spaces)

                if cal.players.index(current_player) < len(cal.players) - 1:
                    current_player = cal.players[cal.players.index(current_player) + 1]
                    cal.turns_committed += 1
                    continue
                else:
                    current_player = cal.players[0]
                    cal.turns_committed += 1
                    continue

            print('{} won!'.format(winning_player))
            break


StartGame()
