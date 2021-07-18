import json
import time
import pygame as game
from modules import Inicialize
from modules.Convert import Convert
from modules.GameRules import Rules
from modules.Verifier import Verifier

with open('./src/config/sneak.json') as f:
    file = json.load(f)
    display = file["display"]
    difficulty = file["difficulty"]
    body_color = file["bodySneak"]
    fruit_color = file["fruitColor"]
    size = file["size"]
    background = file["background"]
    gameOverColor = file["gameOverColor"]


class Window:
    def Start():
        print("loading window")
        game.init()
        game.display.set_caption("Sneak - Game")
        game_window = game.display.set_mode((display[0], display[1]))
        game.display.update()
        print("Started window")
        return game_window

    def Game(game_window):
        game_over = False
        game_fruit_state = False
        sneak_body_color = Convert.hex_rgb(body_color)
        Fruit_color = Convert.hex_rgb(fruit_color)
        Background = Convert.hex_rgb(background)
        PositionPlayer = [display[0] / 2,  display[1] / 2]
        positionsChange = [0, 0]
        controller = game.time.Clock()

        snakeLen = -1

        while not game_over:
            for event in game.event.get():
                if event.type == game.QUIT:
                    game_over = True
                if event.type == game.KEYDOWN:

                    if event.key == game.K_SPACE:
                        PositionPlayer[0] = display[0]/2
                        PositionPlayer[1] = display[1]/2
                        snakeLen = -1
                        game_fruit_state = False
                    elif event.key == game.K_ESCAPE:
                        game.quit()
                        Inicialize.Sneak.close()
                    else:
                        key_name = str(game.key.name(
                            event.key)).replace(" ", "_")
                        Verifier.commands(
                            key_name, positionsChange)

            if PositionPlayer[0] < 0 or PositionPlayer[1] > display[0] or PositionPlayer[1] < 0 or PositionPlayer[1] > display[1]:
                Window.GameOver(game_window)

            if game_fruit_state == False:
                snakeLen += 1
                PositionFruit = Rules.generateFruit()
                game_fruit_state = True

            PositionPlayer[0] += positionsChange[0]
            PositionPlayer[1] += positionsChange[1]

            game_window.fill(Background)
            game.draw.rect(game_window, sneak_body_color, [
                PositionPlayer[0], PositionPlayer[1], size, size])
            game.draw.rect(game_window, Fruit_color, [
                PositionFruit[0], PositionFruit[1], size, size])
            Window.InpendendMessage(
                f"Your score is {snakeLen}", game_window, positions=[10, 10])
            game.display.update()

            game_fruit_state = Rules.checkEat(
                PositionFruit, PositionPlayer)
            controller.tick(difficulty)

        game.quit()
        Inicialize.Sneak.close()

    def GameOver(game_window):

        color = Convert.hex_rgb(gameOverColor)
        font = game.font.SysFont(None, 30)
        message_gameOver = font.render(
            "YOU'RE NOOB, GAME OVER", True, color)
        message_playAgain = font.render(
            "Play again press (SPACE)", True, color)
        message_CloseGame = font.render(
            "Close game press (ESCAPE)", True, color)

        game_window.blit(message_gameOver, [display[0]/3.5, 50])
        game_window.blit(message_playAgain, [display[0]/3.2, 150])
        game_window.blit(message_CloseGame, [display[0]/3.5, 250])

        game.display.update()
        time.sleep(1)

    def InpendendMessage(message, game_window, positions):

        color = Convert.hex_rgb(fruit_color)
        font = game.font.SysFont(None, 30)
        Message = font.render(message, True, color)
        game_window.blit(Message, [positions[0], positions[1]])
