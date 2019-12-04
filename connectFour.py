import numpy as np
from skimage import measure
from itertools import groupby

BLANK = 0
WHITE = 1
BLACK = -1

def ScoreHelper(state, num):
    if (state == num).all(axis=1).any():
        if(len(state) == 4):
            return True
        else:
            return False
    if (state == num).all(axis=0).any():
        if(len(state[0]) == 4):
            return True
        else:
            return False
    if((len(state[0])==4)and(len(state)==4)):
        if (np.diagonal(state) == num).all():
            return True
        if (np.diagonal(np.rot90(state)) == num).all():
            return True 
    return False   

class ConnectFour(object):
    def __init__(self, n):
        self.size = n
        self.gameMap = np.full((n,n), BLANK)
        self.hasWinner = False

    def printMap(self):
        print (self.gameMap)

    """
    Score function to find if there is four connected on game map of any size
    Used Union finding method in skimage library
    Divide the game map into sub-image that can possibly be the winning cases
    Then pass the sub-image to the  same-value line determine algorithm
    In most of the cases the sub-image should be a 4x4 matrix
    Under the condition that sub-image is not 4x4(some bound cases that sub-image is out -of-bound),
    the diagonal winning case cannnot happen
    """
    def HasWinner(self):
        """
        Get connected groups
        """
        n = measure.label(self.gameMap, connectivity=2, background=0)
        y = np.unique(n)
        """
        Get the idnex for non background groups
        """
        idx = [np.where(n == label)
               for label in y
               if label]
        
        score = 0
        min_row = 0
        max_row = 0
        min_col = 0
        max_col = 0
        new_state = []
        s = False
        
        for i in idx:
            row_len = max(i[0])-min(i[0])
            col_len = max(i[1])-min(i[1])
    
            if(row_len==3 or col_len==3):
                ind = i
                indd = [ind[0][0], ind[1][0]]
                numb = self.gameMap[indd[0], indd[1]]
        
                max_row = max(i[0])
                min_row = min(i[0])        
                max_col = max(i[1])
                min_col = min(i[1])

                if(row_len==3):
                    if(col_len <= 3):
                        if(max_col-3>0):
                            new_state = self.gameMap[(max_row-3):(max_row+1),(max_col-3):(max_col+1)]
                        else:
                            new_state = self.gameMap[(max_row-3):(max_row+1),:(max_col+1)]
                    else:
                        for i in range(col_len-3+1):
                            new_state = self.gameMap[(max_row-3):(max_row+1),(max_col-i-3):(max_col-i+1)]
                if(col_len==3):
                    if(row_len <= 3):
                        if(max_row-3>0):
                            new_state = self.gameMap[(max_row-3):(max_row+1),(max_col-3):(max_col+1)]
                        else:
                            new_state = self.gameMap[:(max_row+1),(max_col-3):(max_col+1)]
                    else:
                        for i in range(col_len-3+1):
                            new_state = self.gameMap[(max_row-i-3):(max_row-i+1),(max_col-3):(max_col+1)]
                    
                s = ScoreHelper(new_state,numb)
                
        if(s):
            self.hasWinner= True
            if(numb==1):
                return -1
            else:
                return 1
        return 0
                    

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
                            print(str(player) + " wins")
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



