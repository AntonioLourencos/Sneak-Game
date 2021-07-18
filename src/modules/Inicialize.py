from modules.Window import Window


class Sneak:
    def start():
        print("Starting process.")
        print("Starting Window...")
        game_window = Window.Start()
        Window.Game(game_window)

    def close():
        print("Stoping process.")
        print("Closing Files.")
        print("All files was finalized.")
        exit()
