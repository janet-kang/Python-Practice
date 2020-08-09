# Created August 8, 2020
# Play tic tac toe through the console. Two-player or against computer.

# checklist
# checkGameWon
# gamePlay (prints board, asks for input, check is won, check if over, next player)

# Classes
class gameStatus:
    def __init__(self):
        self.board = [[' ',' ',' '],
                    [' ',' ',' '],
                    [' ',' ',' ']]
        self.player = 1 #or 2
        self.winner = 0 #or 1 or 2

        self.gamePlay()

    def printBoard(self):
        print(f"  1 2 3",
            f"a {self.board[0][0]}|{self.board[0][1]}|{self.board[0][2]}",
            f"-------",
            f"b {self.board[1][0]}|{self.board[1][1]}|{self.board[1][2]}",
            f"-------",
            f"c {self.board[2][0]}|{self.board[2][1]}|{self.board[2][2]}",
            sep="\n")
    
    def askPlacement(self):
        coord = input("(ex: 1a, 3b, 2c): ")
        coord = list(coord)
        if coord[0] not in ['1','2','3']:
            print("Invalid input. Try again.")
            return self.askPlacement()
        elif coord[1] not in ['a','b','c']:
            print("Inavlid input. Try again.")
            return self.askPlacement()
        col = int(coord[0]) - 1
        row = ord(coord[1]) - ord('a')
        if self.board[row][col] != ' ':
            print("This space is occupied. Try again.")
            return self.askPlacement()
        else:
            coord = [row, col]
            return coord

    def placePiece(self):
        print(f"Player {self.player}, where would you like to place your piece?")
        coord = self.askPlacement()
        row = coord[0]
        col = coord[1]
        if self.player == 1:
            piece = 'x'
        else:
            piece = 'o'
        self.board[row][col] = piece

    def checkGameOver(self):
        i = 0
        for i in range(3):
            if ' ' in self.board[i]:
                print("continue playing!!")
                return 0
        print("we all done.")
        return 1

    def checkGameWon(self):
        if self.player == 1:
            piece = 'x'
        else:
            piece = 'o'
        i = 0
        for i in range(3):
            col_check = self.colSame(piece,i)
            if(col_check):
                return True
            row_check = self.rowSame(piece,i)
            if(row_check):
                return True
        diag_check = self.diagSame(piece)
        if(diag_check):
            return True
        return False

    def colSame(self, piece, col):
        i = 0
        for i in range(3):
            if(self.board[i][col] != piece):
                return False
        return True
    
    def rowSame(self, piece, row):
        i = 0
        for i in range(3):
            if(self.board[row][i] != piece):
                return False
        return True

    def diagSame(self, piece):
        i = 0
        for i in range(3):
            if(self.board[i][i] != piece):
                return False
        for i in range(3):
            if(self.board[i][2-i] != piece):
                return False
        return True

    def gamePlay(self):
        self.printBoard()
        self.placePiece()
        won = self.checkGameWon()
        if(won):
            print(f"Congrats! Player {self.player} won!")
            self.printBoard()
            return 0
        over = self.checkGameOver()
        if(over):
            print(f"GAME OVER. Neither player won.")
            self.printBoard()
            return 0
        if(self.player == 1):
            self.player = 2
        else:
            self.player = 1
        return self.gamePlay()



# Functions
def askType():
    """Ask for input and return type of play."""
    type_play = input("Type \"twoplayer\" or \"computer\": ")
    if((type_play == 'twoplayer') or (type_play == 'computer')):
        return type_play
    else:
        print("Invalid input!!")
        return askType()

def welcome():
    """Welcome and return type of play."""
    print("Welcome to the game of Tic Tac Toe! \n",
            "Would you like to play \"twoplayer\" or against \"computer\"?")
    type_play = askType()
    if(type_play == 'twoplayer'):
        print("You entered a two player game.")
        game = twoPlayerGame()
        return 0
    elif(type_play == 'computer'):
        print("You will play against the computer.")
        game = computerGame()
        return 0
    else:
        print("Error. Restart.")
        return 1



def twoPlayerGame():
    """Execute two player game."""
    #Ask for player names

    #Create board and display
    game = gameStatus()
    #game.checkGameOver()
    #Ask for input

    #Check if won

    return 0

def computerGame():
    """Execute computer game play."""
    return 0

if __name__ == '__main__':
    game = welcome()