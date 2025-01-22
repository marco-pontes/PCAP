class BoardGameClass:
    counter = 0
    __counter = 0

    def __init__(self, name, max_players):
        self.name = name
        self.max_players = max_players
        BoardGameClass.__counter += 1