from game import Game
from interface import Screen


"""
KEY
0: unoccupied
1: missed space
2: vertical ship
3: horizontal ship
4: hit vertical ship
5: hit horizontal ship
6: sunk vertical ship
7: sunk horizontal ship
8: implied unoccupied
"""

exampleBoard = [
    [0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
    [0, 3, 3, 3, 3, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 2, 0, 0],
    [0, 2, 0, 0, 0, 1, 0, 2, 0, 0],
    [0, 2, 0, 0, 0, 0, 0, 2, 0, 0],
    [0, 4, 0, 1, 0, 0, 0, 2, 0, 0],
    [0, 0, 3, 3, 5, 0, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 7, 7, 0, 0, 0, 0, 0, 0]
]
exampleBoard2 = [
    [0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
    [0, 3, 4, 3, 0, 0, 1, 0, 0, 0],
    [6, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [6, 0, 0, 0, 1, 0, 0, 1, 0, 0],
    [6, 0, 1, 2, 0, 1, 0, 0, 2, 0],
    [6, 0, 0, 2, 0, 0, 1, 0, 2, 0],
    [0, 0, 0, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [1, 7, 7, 7, 7, 7, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

game = Game(Screen())

game.inputGameSetup()
game.placeShips()

game.tick()