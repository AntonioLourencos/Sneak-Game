from modules.verifier import Verifier


class Sneak:
    def start():
        try:
            Verifier.files()
        except:
            return "error"

    def close():
        print("Stoping process.")
        print("Closing Files.")
        print("All files was finalized.")
        return
