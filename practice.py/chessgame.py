class board:
    def __init__(self):
        self.grid = [[" " for _ in range(8)] for _ in range(8)]
    def display(self):
        print("\n  a b c d e f g h")
        for i, row in enumerate(self.grid):
            print(f"{8-i} { ' '.join(row)} {8-i}")
        print("  a b c d e f g h\n")
board = board()
board.display()
class pieces:
    def __init__(self):
        self.pieces = {"rook","knight","bishop","pawn","queen","king"}
        self.places ={"a1":"rook",