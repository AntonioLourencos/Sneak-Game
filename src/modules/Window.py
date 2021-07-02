import json
import pygame as game


with open('./src/config/sneak.json') as f:
    file = json.load(f)
    display = file["display"]


class Window:
    def Start():
        print("loading window")
        game.init()
        game.display.set_caption("Sneak - Game")
        game.display.set_mode((display))
        print("Started window")
        return game

    def Game(game):
        gameOver = False

        while not gameOver:
            for event in game.event.get():
                if event.type == game.QUIT:
                    gameOver = True
