import math
from termcolor import colored
import os
import random

from ai import *

def clearScr():
    os.system("cls" if os.name == "nt" else "clear")

ROW_LETTERS = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'G')

"""
                        BATTLESHIP
            A I          \ ==== /            YOU
    1 2 3 4 5 6 7 8 9 0   | -- |     1 2 3 4 5 6 7 8 9 0
  A - - - o - o - - - -   | -- |   A - - - o - o - - - - 
  B - > > > > - o - - -   | -- |   B - - o - - - o - - - 
  C - - - - - - - - - -   | -- |   C v - - - - - - - - - 
  D - - - - o - - v - -   | -- |   D v - - - o - - o - - 
  E - v - - - o - v - -   | -- |   E v - o - - o - - - - 
  F - v - - - - - v - -   | -- |   F v - - - - - o - - - 
  G - v - o - - - v - -   | -- |   G - - - o - - - - - - 
  H - - > > > - - v - -   | -- |   H - - - o - - - - - - 
  I - - - - - - o - - -   | -- |   I o > > > > > o - - - 
  G - - > > - - - - - -   | -- |   G - - - - - - - - - - 
         ANONYMOUS       / ==== \         ANONYMOUS     
  
  YOUR MOVE: 
"""


ALL_FONT_KEY = (
    colored("-", "white", "on_blue"),
    colored("o", "white", "on_blue"),
    colored("v", "white", "on_blue", attrs=["dark"]), 
    colored(">", "white", "on_blue", attrs=["dark"]), 
    colored("v", "red", "on_blue"), 
    colored(">", "red", "on_blue"), 
    colored("v", "red", "on_blue", attrs=["dark"]), 
    colored(">", "red", "on_blue", attrs=["dark"]), 
    colored("#", "white", "on_blue"),
)
CONCEALED_FONT_KEY = (
    colored("-", "white", "on_blue"),
    colored("o", "white", "on_blue"),
    colored("-", "white", "on_blue", attrs=["dark"]), 
    colored("-", "white", "on_blue", attrs=["dark"]), 
    colored("o", "red", "on_blue"), 
    colored("o", "red", "on_blue"), 
    colored("v", "red", "on_blue", attrs=["dark"]), 
    colored(">", "red", "on_blue", attrs=["dark"]), 
    colored("#", "white", "on_blue"),
)



# format = (color, attrs)
AI_DIFFICULTY_COLORS = (
    ("white", ["dark"]), # none
    ("green", []), # super easy
    ("green", ["dark"]), # easy
    ("yellow", []), # medium
    ("red", []), # hard
    ("red", ["dark"]), # super hard
    ("magenta", ["dark"]), # impossible
)
# get the dif
def getDifficultyColor(player, isAttribute):
    return AI_DIFFICULTY_COLORS[player.difficulty][isAttribute]




class Screen():
    def __init__(self) -> None:
        pass

    # starting inputs
    # ===============


    # player types----------------------
    def inputPlayerTypes(self):
        from game import MODE_NAMES

        clearScr()
        print("BATTLESHIP\n")

        print("Select game mode:")
        for i in range(len(MODE_NAMES)):
            print("  {0}: {1}".format(i, MODE_NAMES[i]))
        modeStr = input(">> ")
        mode = int(modeStr) if modeStr != "" else 0
        
        if mode == 0:
            print("\nPlayer goes first? (y/n)")
            inverse = input(">> ").lower() == "n"
        else:
            inverse = 0

        return (mode, inverse)
    


    # user -------------------------------------------
    def inputUser(self, playerNum):
        print("\nInput PLAYER{0} name:".format(str(playerNum+1)))
        name = input(">> ")
        if playerNum == 0:
            self.user1Name = name
        else:
            self.user2Name = name
        return (name,)



    # ai ----------------------------------------------
    def inputAI(self, playerNum):
        # creates a colored wrap around any mode (preset, placement...) like "**MODE**"
        # entrys look like (name, difficulty) and can be found in ai.ai
        def difficultyWrap(entry):
            col = AI_DIFFICULTY_COLORS[entry[1]]
            return colored("**", col[0], attrs=col[1]) + entry[0] + colored("**", col[0], attrs=col[1])
        def printEntries(entries):
            for i in range(len(entries)):
                print("  {0}: {1}".format(i, difficultyWrap(entries[i])))

        def handleInput(randFinish, randStart=0):
            inp = input(">> ")
            return int(inp) if inp != "" else random.randint(randStart, randFinish)

        clearScr()
        print("Select AI(PLAYER{0}) preset: (leave blank for random preset)".format(str(playerNum+1)))
        printEntries(AI_PRESET_NAMES)
        
        preset = handleInput(len(AI_PRESETS)-1, 1)
        
        if preset != 0: # not custom
            return (AI_PRESETS[preset],)
        else: #if custom ai
            print(colored("\nCUSTOM AI", "white", attrs=["underline"]))

            print("\nSelect placement method:")
            printEntries(AI_PLACEMENT_MODE_NAMES)
            placementMode = handleInput(len(AI_PLACEMENT_MODE_NAMES)-1)
            
            print("\nSelect method for finding enemy ships:")
            printEntries(AI_LOCATION_MODE_NAMES)
            locationMode = handleInput(len(AI_LOCATION_MODE_NAMES)-1)

            print("\nSelect method for destroying found ships:")
            printEntries(AI_DESTROYING_MODE_NAMES)
            destroyMode = handleInput(len(AI_DESTROYING_MODE_NAMES)-1)

            methodTuple = (placementMode, locationMode, destroyMode)
            return (methodTuple,)

            


    
    """
        IN: 
            - players - [player1, player2]
                returns two player classes 
            - turn - the index of the player whose turn it is
    """
    def display(self, players, turn):
        # format the name into a string that can be printed without breaking the screen
        def formatName (string):
            if len(string) >= 19:
                string = string[:19]
            else:
                spacesNeeded = math.floor((19 - len(string)) / 2)
                for i in range(spacesNeeded):
                    string = " " + string + " "
                if len(string) < 19:
                    string = string + " "
            return string.upper()

        # get the title of a player
        def getTitle(playerNum):
            myTurn = playerNum == turn
            attributes = ["bold", "blink"] if myTurn else ["bold"]
            if players[playerNum].type == "User":
                color = "yellow" if myTurn else "blue"
                text = "PLAYER{0}".format(playerNum+1)
                return colored(formatName(text), color, attrs=attributes)
            else:
                color = "yellow" if myTurn else "red"
                return colored(formatName("A I"), color, attrs=attributes)

        clearScr()

        # define variables
        # ======================
        leftTitle = getTitle(0)
        rightTitle = getTitle(1)
        boardSeparator = colored(" | -- | ", "cyan")
        # format names to fill space and color them to match difficulty
        leftName = colored(formatName(players[0].name), getDifficultyColor(players[0], 0), attrs=getDifficultyColor(players[0], 1))
        rightName = colored(formatName(players[1].name), getDifficultyColor(players[1], 0), attrs=getDifficultyColor(players[1], 1))

        # print header
        # ======================
        #     #                        BATTLESHIP
        print("                        {00000000}".format(colored("BATTLESHIP", "blue", attrs=["underline", "bold"])))
        #     #            A I          \ ==== /            YOU
        print("    {00000000000000000}  {000002}    {00000000000000001}".format(leftTitle, rightTitle, colored("\ ==== /", "cyan")))
        #     #    1 2 3 4 5 6 7 8 9 0   | -- |     1 2 3 4 5 6 7 8 9 0
        print("    1 2 3 4 5 6 7 8 9 0  {000000}    1 2 3 4 5 6 7 8 9 0".format(boardSeparator))


        # display the two boards
        # ========================
        for row in range(10):
            board1Line = ""
            board2Line = ""
            for col in range (10):
                # add characters to the row using the all font key (all revealing since visi board is concealed already)
                board1Line = board1Line + ALL_FONT_KEY[players[0].visibleBoard[row][col]] + (colored(" ", "white", "on_blue") if col != 9 else " ")
                board2Line = board2Line + ALL_FONT_KEY[players[1].visibleBoard[row][col]] + (colored(" ", "white", "on_blue") if col != 9 else " ")
            
            #Boardline:- - - o - o - - - - 
            #Separator: | -- | 
            #     #  A - - - o - o - - - -   | -- |   A - - - o - o - - - -
            print("  "+ROW_LETTERS[row]+" "+board1Line+" "+boardSeparator+"  "+ROW_LETTERS[row]+" "+board2Line)
        
        #     #  G - - > > - - - - - -   | -- |   G - - - - - - - - - -
        #     #         ANONYMOUS       / ==== \         ANONYMOUS
        print("    {00000000000000000}  {000002}    {00000000000000001}".format(leftName, rightName, colored("/ ==== \\", "cyan")))

