
from player import *
from ai import *

USER_ID = 0
AI_ID = 1
MODES = (
    [USER_ID, AI_ID],
    [USER_ID, USER_ID],
    [AI_ID, AI_ID]
)
MODE_NAMES = (
    "Player VS AI",
    "Player VS Player",
    "AI VS AI"
)

class Game():
    players = [None, None]

    def __init__(self, screen) -> None:
        self.screen = screen
    
    # get the game setup such as the players and the 
    def inputGameSetup(self):
        # get player types
        modeNum, inverse = self.screen.inputPlayerTypes()
        playerTypes = MODES[modeNum] if not inverse else MODES[modeNum][::-1] # invert (USER, AI) if inverse is true

        # create the new players based on the user input types
        for playerNum in range(len(playerTypes)):
            playerType = playerTypes[playerNum]
            if playerType == USER_ID: # make new user with screen + inputs from setup
                self.players[playerNum] = User(self.screen, *self.screen.inputUser(playerNum)) 
            elif playerType == AI_ID:
                self.players[playerNum] = AI(self.screen, *self.screen.inputAI(playerNum))
    
    def placeShips(self):
        players[0].placeShips()
        players[1].placeShips()

    def tick(self):
        self.screen.display(self.players, 1)