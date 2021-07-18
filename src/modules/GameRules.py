import json
import random
import pygame as game
from modules import Inicialize

with open('./src/config/sneak.json') as f:
    file = json.load(f)
    move = file["move"]
    size = file["size"]
    display = file["display"]


class Rules:
    def up(position: list):
        position[1] -= move
        position[0] = 0
        return position

    def down(position: list):
        position[1] += move
        position[0] = 0
        return position

    def right(position: list):

        position[0] += move
        position[1] = 0
        return position

    def left(position: list):
        position[0] -= move
        position[1] = 0
        return position

    def generateFruit():
        x = round(random.randrange(0, display[1] - size) / 10.0) * 10.0
        y = round(random.randrange(0, display[1] - size) / 10.0) * 10.0
        return [x, y]

    def checkEat(PositionFruit, PositionPlayer):
        if PositionFruit == PositionPlayer:
            return False
