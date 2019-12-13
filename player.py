import board


class Player:

    def __init__(self, player_number, current_space, is_turn):
        self.start_space = 0
        self.current_space = current_space
        self.player_number = player_number
        self.is_turn = is_turn

        # a list of all the ladders with the key being the ladder start and the value being the ladder end
        self.ladders_start_end = {4: 20, 5: 10, 7: 23, 14: 30, 18: 35, 22: 39, 27: 37, 41: 58, 42: 53, 49: 62}

        # a list of all the chutes with the key being the chute start and the value being the chute end
        self.chutes_start_end = {34: 2, 38: 3, 46: 33, 56: 39, 57: 44, 59: 45}

    # checks whether the current space the player is on is a chute or a ladder, moves them to the corresponding space
    def space_check(self):
        if self.current_space in self.ladders_start_end.keys():
            self.current_space = self.ladders_start_end.get(self.current_space)
            return self.ladders_start_end.get(self.current_space)

        elif self.current_space in self.chutes_start_end.keys():
            self.current_space = self.chutes_start_end.get(self.current_space)
            return self.chutes_start_end.get(self.current_space)


board.ChutesAndLadders()
