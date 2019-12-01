import numpy as np

BLANK = "_"
WHITE = "O"
BLACK = "X"

class ConnectFour(object):
    def __init__(self, n):
        self.size = n
        self.gameMap = np.full((n,n), BLANK)
        self.hasWinner = False

    def printMap(self):
        print (self.gameMap)

    def HasWinner(self):
        for symbol in "OX":
            if(self.gameMap == symbol).all(axis=1).any():
                self.hasWinner = True
                return symbol
            if(self.gameMap == symbol).all(axis=0).any():
                self.hasWinner = True
                return symbol
            if(np.diagonal(self.gameMap) == symbol).all():
                self.hasWinner = True
                return symbol
            if(np.diagonal(np.rot90(self.gameMap)) == symbol).all():
                self.hasWinner = True
                return symbol

        return "_"

    def move(self, col_index, player):
        if self.hasWinner == False:
            if col_index < self.size:
                col_array = self.gameMap[:, col_index]
                for index in range(col_array.size):
                    if col_array[col_array.size - index - 1] == BLANK:
                        col_array[col_array.size - index - 1] = player
                        self.gameMap[:, col_index] = col_array
                        player = self.HasWinner()
                        if(self.hasWinner):
                            print(player + " wins")
                        return True
                print("this col is full. mvoe failed")
                return False
            else:
                print("col index out of bounds")
                return False
        else:
            print("game ended")
            return False
                
                        
                        

if __name__ == '__main__':
    c4 = ConnectFour(4)
    c4.move(1,BLACK)
    c4.move(1, WHITE)
    c4.move(0,BLACK)
    c4.move(1, WHITE)
    c4.move(2, BLACK)
    c4.move(1, WHITE)
    c4.move(3, BLACK)
    c4.printMap()



