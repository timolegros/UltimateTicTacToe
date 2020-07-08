# ----------------------------------------------------
# Assignment 2: Tic Tac Toe classes
# 
# Author: 
# Collaborators:
# References:
# ----------------------------------------------------


class NumTicTacToe:
    def __init__(self):
        """
        Initializes an empty Numerical Tic Tac Toe board.
        Inputs: none
        Returns: None
        """
        self.board = []
        self.size = 3

        for i in range(self.size):
            row = []
            for j in range(self.size):
                row.append(0)
            self.board.append(row)

    def drawBoard(self):
        """
        Displays the current state of the board, formatted with column and row
        indices shown.
        Inputs: none
        Returns: None
        """
        space = " "
        print()
        print('   0   1   2')
        for i in range(self.size):
            if i != 0:
                print('  -----------')
            print(str(i) + space, end='')
            for j in range(self.size):
                if self.board[i][j] == 0:
                    print(space * 3, end='')
                else:
                    print(space + str(self.board[i][j]) + space, end='')

                if not j == 2:
                    print('|', end='')
                else:
                    print()

    def squareIsEmpty(self, row, col):
        """
        Checks if a given square is "empty", or if it already contains a number
        greater than 0.
        Inputs:
           row (int) - row index of square to check
           col (int) - column index of square to check
        Returns: True if square is "empty"; False otherwise
        """
        if self.board[row][col] == 0:
            return True
        elif self.board[row][col] != 0:
            return False

    def update(self, row, col, mark):
        """
        Assigns the integer, mark, to the board at the provided row and column,
        but only if that square is empty.
        Inputs:
           row (int) - row index of square to update
           col (int) - column index of square to update
           mark (int) - entry to place in square
        Returns: True if attempted update was successful; False otherwise
        """
        if self.squareIsEmpty(row, col):
            if 1 <= mark <= 9:
                self.board[row][col] = mark
                return True
            else:
                return False
        else:
            return False

    def boardFull(self):
        """
        Checks if the board has any remaining "empty" squares.
        Inputs: none
        Returns: True if the board has no "empty" squares (full); False otherwise
        """
        counter = 0
        for row in self.board:
            for col in row:
                if col == 0:
                    counter += 1
                    return False
        if counter == 0:
            return True

    def isWinner(self):
        """
        Checks whether the current player has just made a winning move.  In order
        to win, the player must have just completed a line (of 3 squares) that
        adds up to 15. That line can be horizontal, vertical, or diagonal.
        Inputs: none
        Returns: True if current player has won with their most recent move;
                 False otherwise
        """
        counter = 0
        inRow = []

        # checks rows
        for row in self.board:
            for i in row:
                counter += i
                inRow.append(i)
            if counter == 15 and 0 not in inRow:
                return True
            else:
                counter = 0
                inRow = []

        # checks columns
        for i in range(self.size):
            for row in self.board:
                counter += row[i]
                inRow.append(row[i])
            if counter == 15 and 0 not in inRow:
                return True
            else:
                counter = 0
                inRow = []

        # checks diagonals
        i = 0
        for row in self.board:
            counter += row[i]
            inRow.append(row[i])
            i += 1
        if counter == 15 and 0 not in inRow:
            return True
        else:
            counter = 0
            inRow = []

        i = 2
        for row in self.board:
            counter += row[i]
            inRow.append(row[i])
            i -= 1
        if counter == 15 and 0 not in inRow:
            return True

        return False

    def isNum(self):
        """
        Checks whether this is a Numerical Tic Tac Toe board or not
        Inputs: none
        Returns: True
        """
        # ???????????????


class ClassicTicTacToe:
    def __init__(self):
        """
        Initializes an empty Classic Tic Tac Toe board.
        Inputs: none
        Returns: None
        """
        self.board = []
        self.size = 3

        for i in range(self.size):
            row = []
            for j in range(self.size):
                row.append(0)
            self.board.append(row)

    def drawBoard(self):
        """
        Displays the current state of the board, formatted with column and row
        indices shown.
        Inputs: none
        Returns: None
        """
        space = " "
        print()
        print('   0   1   2')
        for i in range(self.size):
            if i != 0:
                print('  -----------')
            print(str(i) + space, end='')
            for j in range(self.size):
                if self.board[i][j] == 0:
                    print(space * 3, end='')
                else:
                    print(space + str(self.board[i][j]) + space, end='')

                if not j == 2:
                    print('|', end='')
                else:
                    print()

    def squareIsEmpty(self, row, col):
        """
        Checks if a given square is "empty", or if it already contains an X or O.
        Inputs:
           row (int) - row index of square to check
           col (int) - column index of square to check
        Returns: True if square is "empty"; False otherwise
        """
        if self.board[row][col] == 0:
            return True
        else:
            return False

    def update(self, row, col, mark):
        """
        Assigns the string, mark, to the board at the provided row and column,
        but only if that square is "empty".
        Inputs:
           row (int) - row index of square to update
           col (int) - column index of square to update
           mark (str) - entry to place in square
        Returns: True if attempted update was successful; False otherwise
        """
        if self.squareIsEmpty(row, col):
            if str(mark) == 'X' or str(mark) == 'O':
                self.board[row][col] = str(mark)
                return True
            else:
                return False
        else:
            return False

    def boardFull(self):
        """
        Checks if the board has any remaining "empty" squares.
        Inputs: none
        Returns: True if the board has no "empty" squares (full); False otherwise
        """
        counter = 0
        for row in self.board:
            for col in row:
                if col == 0:
                    counter += 1
                    return False
        if counter == 0:
            return True

    def isWinner(self):
        """
        Checks whether the current player has just made a winning move.  In order
        to win, the player must have just completed a line (of 3 squares) with
        matching marks (i.e. 3 Xs  or 3 Os). That line can be horizontal, vertical,
        or diagonal.
        Inputs: none
        Returns: True if current player has won with their most recent move;
                 False otherwise
        """
        firstPlayer = 0
        secondPlayer = 0

        # checks rows
        for row in self.board:
            for i in row:
                if i == 'X':
                    firstPlayer += 1
                elif i == 'O':
                    secondPlayer += 1
            if firstPlayer == 3 or secondPlayer == 3:
                return True
            else:
                firstPlayer = 0
                secondPlayer = 0

        # checks columns
        for i in range(self.size):
            for row in self.board:
                if row[i] == 'X':
                    firstPlayer += 1
                elif row[i] == 'O':
                    secondPlayer += 1
            if firstPlayer == 3 or secondPlayer == 3:
                return True
            else:
                firstPlayer = 0
                secondPlayer = 0

        # checks diagonals
        i = 0
        for row in self.board:
            if row[i] == 'X':
                firstPlayer += 1
            elif row[i] == 'O':
                secondPlayer += 1
            i += 1
        if firstPlayer == 3 or secondPlayer == 3:
            return True
        else:
            firstPlayer = 0
            secondPlayer = 0

        i = 2
        for row in self.board:
            if row[i] == 'X':
                firstPlayer += 1
            elif row[i] == 'O':
                secondPlayer += 1
            i -= 1
        if firstPlayer == 3 or secondPlayer == 3:
            return True

        return False

    def isNum(self):
        """
        Checks whether this is a Numerical Tic Tac Toe board or not
        Inputs: none
        Returns: False
        """
        # TO DO: delete pass (and this comment) and complete method
        pass


class MetaTicTacToe:
    def __init__(self, configFile):
        """
        Initializes an empty Meta Tic Tac Toe board, based on the contents of a
        configuration file.
        Inputs:
           configFile (str) - name of a text file containing configuration information
        Returns: None
        """
        self.size = 3
        self.board = []
        file = open(configFile, 'r')
        for lines in file.readlines():
            line = lines.strip()
            self.board.append(line.split(' '))

    def drawBoard(self):
        """
        Displays the current state of the board, formatted with column and row
        indices shown.
        Inputs: none
        Returns: None
        """
        space = " "
        print('   0   1   2')
        for i in range(self.size):
            if i != 0:
                print('  -----------')
            print(str(i) + space, end='')
            for j in range(self.size):
                if self.board[i][j] == 'n' or self.board[i][j] == 'c':
                    print(space + str(self.board[i][j]) + space , end='')
                else:
                    print(space + str(self.board[i][j]) + space, end='')

                if not j == 2:
                    print('|', end='')
                else:
                    print()

    def squareIsEmpty(self, row, col):
        """
        Checks if a given square contains a non-played local game board ("empty"),
        or the result of a played local game board (not "empty").
        Inputs:
           row (int) - row index of square to check
           col (int) - column index of square to check
        Returns: True if square is "empty"; False otherwise
        """
        if self.board[row][col] == 'n' or self.board[row][col] == 'c':
            return True
        else:
            return False

    def update(self, row, col, result):
        """
        Assigns the string, result, to the board at the provided row and column,
        but only if that square is "empty".
        Inputs:
           row (int) - row index of square to update
           col (int) - column index of square to update
           result (str) - entry to place in square
        Returns: True if attempted update was successful; False otherwise
        """
        if self.squareIsEmpty(row, col):
            if result == 'X' or result == 'O' or result == 'D':
                self.board[row][col] = result
                return True
        return False

    def boardFull(self):
        """
        Checks if the board has any remaining "empty" squares (i.e. any un-played
        local boards).
        Inputs: none
        Returns: True if the board has no "empty" squares (full); False otherwise
        """
        counter = 0
        for row in self.board:
            for col in row:
                if col == 'c' or col == 'n':
                    counter += 1
                    return False
        if counter == 0:
            return True

    def isWinner(self):
        """
        Checks whether the current player has just made a winning move.  In order
        to win, the player must have just completed a line (of 3 squares) of their
        mark (three Xs for Player 1, three Os for Player 2), or 3 draws. That line
        can be horizontal, vertical, or diagonal.
        Inputs: none
        Returns: True if current player has won with their most recent move;
                 False otherwise
        """
        firstPlayer = 0
        secondPlayer = 0

        # checks rows
        for row in self.board:
            for i in row:
                if i == 'X':
                    firstPlayer += 1
                elif i == 'O':
                    secondPlayer += 1
            if firstPlayer == 3 or secondPlayer == 3:
                return True
            else:
                firstPlayer = 0
                secondPlayer = 0

        # checks columns
        for i in range(self.size):
            for row in self.board:
                if row[i] == 'X':
                    firstPlayer += 1
                elif row[i] == 'O':
                    secondPlayer += 1
            if firstPlayer == 3 or secondPlayer == 3:
                return True
            else:
                firstPlayer = 0
                secondPlayer = 0

        # checks diagonals
        i = 0
        for row in self.board:
            if row[i] == 'X':
                firstPlayer += 1
            elif row[i] == 'O':
                secondPlayer += 1
            i += 1
        if firstPlayer == 3 or secondPlayer == 3:
            return True
        else:
            firstPlayer = 0
            secondPlayer = 0

        i = 2
        for row in self.board:
            if row[i] == 'X':
                firstPlayer += 1
            elif row[i] == 'O':
                secondPlayer += 1
            i -= 1
        if firstPlayer == 3 or secondPlayer == 3:
            return True

        return False

    def getLocalBoard(self, row, col):
        """
        Returns the instance of the empty local board at the specified row, col
        location (i.e. either ClassicTicTacToe or NumTicTacToe).
        Inputs:
           row (int) - row index of square
           col (int) - column index of square
        Returns: instance of appropriate empty local board if un-played;
                 None if local board has already been played
        """
        if self.board[row][col] == 'n' or self.board[row][col] == 'c':
            return self.board[row][col]
        else:
            return None


if __name__ == "__main__":
    # game = NumTicTacToe()
    # game2 = ClassicTicTacToe()
    # game3 = MetaTicTacToe('MetaTTTconfig.txt')

    # testing all functions in NumTicTacToe class - all working
    # drawBoard() testing - works
    # game.drawBoard()
    # squareIsEmpty() testing - works
    # print(game.squareIsEmpty(0, 0))
    # update() testing - works
    # game.update(0, 0, 3)
    # game.update(1, 1, 7)
    # game.update(2, 2, 5)
    # game.drawBoard()
    # boardFull() testing - works
    # print(game.boardFull())
    # isWinner() testing
    # print(game.isWinner())

    # testing all functions in ClassicTicTacToe class - all working
    # drawBoard() testing - works
    # game2.drawBoard()
    # squareIsEmpty() testing - works
    # print(game2.squareIsEmpty(0, 0))
    # update() testing - works
    # game2.update(0, 0 , 'X')
    # game2.update(1, 1, 'X')
    # game2.update(2, 2, 'X')
    # game2.drawBoard()
    # boardFull() testing - works
    # print(game2.boardFull())
    # isWinner() testing - working
    # print(game2.isWinner())

    # testing the updating, drawing, and indicators for winning/continuing in MetaTicTacToe class - all working
    # game3.drawBoard()
    # print(game3.squareIsEmpty(0, 0))
    # game3.update(0, 0, 'X')
    # game3.drawBoard()
    # print(game3.squareIsEmpty(0, 0))
    # game3.update(0, 0, 'X')
    # game3.update(1, 1, 'X')
    # game3.update(2, 2, 'X')
    # game3.drawBoard()
    # print(game3.isWinner())
    # print(game3.getLocalBoard(1, 0))
