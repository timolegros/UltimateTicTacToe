from UltimateMetaTTT import NumTicTacToe
from UltimateMetaTTT import ClassicTicTacToe
from UltimateMetaTTT import MetaTicTacToe


def playNum(num, player, numbersEntered, counter):
    """
        This function asks the player for the row, column and input numbers for the numbers tic tac toe game. It
        validates the chosen rows, columns, and inputs before returning them. This function differentiates between odds
        and evens for player 1 and player 2 respectively.
        Parameters: The current numbers tic tac toe board initialized earlier and the current player.
        Returns: The row, column, and the input number (odd/even).
    """
    notEmpty = True
    odds = [1, 3, 5, 7, 9]
    evens = [2, 4, 6, 8]



    ask = True
    while ask:
        if counter % 2 != 0:
            playerNumber = input('Player ' + str(player) + ', please enter an odd number (1-9): ')
        elif counter % 2 == 0:
            playerNumber = input('Player ' + str(player) + ', please enter an even number (2-8): ')
        if playerNumber.isdigit():
            playerNumber = int(playerNumber)
            if counter % 2 != 0:
                if playerNumber in odds and playerNumber not in numbersEntered:
                    numbersEntered.append(playerNumber)
                    ask = False
                elif playerNumber in numbersEntered:
                    print("Error: that number has already been entered. ", end='')
                else:
                    print("Error: entry not odd. ", end='')
            elif counter % 2 == 0:
                if playerNumber in evens and playerNumber not in numbersEntered:
                    numbersEntered.append(playerNumber)
                    ask = False
                elif playerNumber in numbersEntered:
                    print("Error: that number has already been entered. ", end='')
                else:
                    print("Error: entry not even. ", end='')
        else:
            print("Please enter a valid number!")

    while notEmpty:

        ask = True
        while ask:
            row = input('Player ' + str(player) + ', please enter a row: ')
            if row.isdigit():
                row = int(row)
                if 0 <= row <= 2:
                    ask = False
                else:
                    print("Error: column not in correct range.", end='')
            else:
                print("Error: row not in correct range.", end='')

        ask = True
        while ask:
            column = input('Player ' + str(player) + ', please enter a column: ')
            if column.isdigit():
                column = int(column)
                if 0 <= column <= 2:
                    ask = False
                else:
                    print("Error: column not in correct range.", end='')
            else:
                print("Error: row not in correct range.", end='')

        if num.squareIsEmpty(row, column):
            return row, column, playerNumber
        else:
            print("Error: could not make move! This spot is already filled!")


def playClassic(classic, player):
    """
    This function asks the player for row and column numbers for the classical tic tac toe game. It validates the chosen
    rows and columns before returning them.
    Parameters: The current classic tic tac toe board initialized earlier and the current player.
    Returns: The row, column, and the corresponding player symbol.
    """
    notEmpty = True

    while notEmpty:

        ask = True
        while ask:
            row = input('Player ' + str(player) + ', please enter a row: ')
            if row.isdigit():
                row = int(row)
                if 0 <= row <= 2:
                    ask = False
                else:
                    print("Error: row not in correct range.", end='')
            else:
                print("Error: row not in correct range.", end='')

        ask = True
        while ask:
            column = input('Player ' + str(player) + ', please enter a column: ')
            if column.isdigit():
                column = int(column)
                if 0 <= column <= 2:
                    ask = False
                else:
                    print("Error: column not in correct range.", end='')
            else:
                print("Error: column not in correct range.", end='')

        if classic.squareIsEmpty(row, column):
            return row, column
        else:
            print("Error: could not make move! This spot is already filled!")


def classicGame(classic, player):
    """
    This function initializes the classic tic tac toe game. It updates the classic tic tac toe board as the game
    progresses and checks after every player turn if a player has won or if a tie has occurred.
    Parameters: The classic game board that was initialized and the current player
    Returns: the player who won or in the case of a tie it returns "tie"
    """
    dashes = '----------------------------------'
    ask = True
    playerOne = 'X'
    playerTwo = 'O'
    counter = 1

    print(dashes)
    print('This is a Classical Tic Tac Toe.')
    classic.drawBoard()

    while ask:
        currentPlayer = playClassic(classic, player)
        currentPlayerRow = currentPlayer[0]
        currentPlayerColumn = currentPlayer[1]
        # currentPlayerNumber = currentPlayer[2]

        if counter % 2 != 0:
            classic.update(currentPlayerRow, currentPlayerColumn, playerOne)
        elif counter % 2 == 0:
            classic.update(currentPlayerRow, currentPlayerColumn, playerTwo)

        classic.drawBoard()
        if classic.isWinner():
            print("Player " + str(player) + " wins. Congrats!")
            return player
        elif classic.boardFull() and not classic.isWinner():
            print("Its a tie!")
            winner = 'Tie'
            return winner
        else:
            if player == 1:
                player += 1
            else:
                player -= 1
        counter += 1

def numGame(num, player):
    """
        This function initializes the numbers tic tac toe game. It updates the numbers tic tac toe board as the game
        progresses and checks after every player turn if a player has won or if a tie has occurred.
        Parameters: The numbers game board that was initialized and the current player
        Returns: the player who won or in the case of a tie it returns "tie"
        """
    dashes = '----------------------------------'
    ask = True
    numbersEntered = []

    counter = 1

    print(dashes)
    print('This is Numerical Tic Tac Toe.')
    num.drawBoard()

    while ask:
        currentPlayer = playNum(num, player, numbersEntered, counter)
        currentPlayerRow = currentPlayer[0]
        currentPlayerColumn = currentPlayer[1]
        currentPlayerNumber = currentPlayer[2]
        counter += 1

        num.update(currentPlayerRow, currentPlayerColumn, currentPlayerNumber)
        num.drawBoard()
        if num.isWinner():
            print("Player " + str(player) + " wins. Congrats!")
            return player
        elif num.boardFull() and not num.isWinner():
            print("Its a tie!")
            winner = 'Tie'
            return winner
        else:
            if player == 1:
                player += 1
            else:
                player -= 1


def playerDeciding(num, classic, meta, player):
    """
    This function asks the current player to choose a spot on the meta board and then runs the appropriate functions
    based on the chosen square. The function also updates and draws the meta board once a player wins or ties a
    sub-tic tac toe game.
    Parameters: num and classic are the numbers/classic tic tac toe objects initialized in the main function, meta is
                current state of the meta class object created at the very start of the game, and player is the current
                player.
    Returns: N/A
    """
    winnerNum = ''
    winnerClassic = ''
    playerOneSymbol = 'X'
    playerTwoSymbol = 'O'
    correctRow = True
    correctCol = True

    while correctRow:
        row = input('Player ' + str(player) + ', please enter a row: ')
        if row.isdigit():
            row = int(row)
            if 0 <= row <= 2:
                correctRow = False
            else:
                print("Please enter a valid row number from 0 to 2!")
        else:
            print("Please enter a valid row number from 0 to 2!")

    while correctCol:
        col = input('Player ' + str(player) + ', please enter a column: ')
        if col.isdigit():
            col = int(col)
            if 0 <= col <= 2:
                correctCol = False
            else:
                print("Please enter a valid column number from 0 to 2!")
        else:
            print("Please enter a valid column number from 0 to 2!")

    if meta.squareIsEmpty(row, col):
        if meta.getLocalBoard(row, col) == 'n':
            winnerNum = numGame(num, player)
        elif meta.getLocalBoard(row, col) == 'c':
            winnerClassic = classicGame(classic, player)
    else:
        print('This spot is already filled!')
        playerDeciding(num, classic, meta, player)

    if winnerNum == 1 or winnerClassic == 1:
        meta.update(row, col, playerOneSymbol)
        meta.drawBoard()
    elif winnerNum == 2 or winnerClassic == 2:
        meta.update(row, col, playerTwoSymbol)
        meta.drawBoard()
    elif winnerClassic == 'Tie' or winnerNum == 'Tie':
        tie = 'D'
        print('', end='\n')
        meta.update(row, col, tie)
        meta.drawBoard()


def main():
    # create a board (object) for each class
    meta = MetaTicTacToe('MetaTTTconfig.txt')
    dashes = '----------------------------------'
    player = 1

    # game setup
    print(dashes)
    print('Starting new Meta Tic Tac Toe game')
    print(dashes)
    meta.drawBoard()

    # begin the game with player 1
    ask = True
    while ask:

        if player == 1:
            num = NumTicTacToe()
            classic = ClassicTicTacToe()
            playerDeciding(num, classic, meta, player)
            player += 1
        else:
            num = NumTicTacToe()
            classic = ClassicTicTacToe()
            playerDeciding(num, classic, meta, player)
            player -= 1

        if meta.isWinner():
            if player == 1:
                print("Player " + str(player + 1) + " wins the Meta Tic Tac Toe game. GOOD GAME!")
                return
            elif player == 2:
                print("Player " + str(player - 1) + " wins this game!")
                return
        elif meta.boardFull():
            print("Its a tie!")

main()

if __name__ == "__main__":
    while True:
        playAgain = input("Do you want to player another game? (Y/N)")
        if playAgain == "Y" or "N":
            if playAgain == "Y":
                main()
            elif playAgain == "N":
                print('Thanks for playing! Goodbye.')
        else:
            print("Please enter 'Y' for yes or 'N' for no")
