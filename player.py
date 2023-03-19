
# player
# ======
# both humans and bots are Players, Users are humans, and AI is bots
class Player:
    visibleBoard = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    
    difficulty = 0

    def __init__(self, screen, name, playerType) -> None:
        self.screen = screen
        self.name = name
        self.type = playerType

    def placeShips(self, ships):
        pass

# user
# ====
class User(Player):
    def __init__(self, screen, name) -> None:
        super().__init__(screen, name, "User")

    def placeShips():
        pass