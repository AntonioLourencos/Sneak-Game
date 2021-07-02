from modules.Verifier import Verifier
from modules.Window import Window


class Sneak:
    def start():
        print("Starting process.")
        Verifier.files()
        print("Starting Window...")
        game = Window.Start()
        Window.Game(game)

    def close():
        print("Stoping process.")
        print("Closing Files.")
        print("All files was finalized.")
        return
