class Player:
    def __init__(self, symbol):
        self.symbol = symbol

    def get_move(self):
        move = input("Next move for player " + self.symbol + " (0-8): ")

        while not (move.isdigit() and 0 <= int(move) <= 8):
            print("Invalid move digit, try again.")
            move = input("Next move for player " + self.symbol + " (0-8): ")

        return int(move)
    def __str__(self):
        return self.symbol