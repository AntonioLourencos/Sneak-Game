class Verifier:
    def files():
        try:
            with open("./src/config/sneak.json") as f:
                file = f.read()
                if len(file) >= 3:
                    return "error"
        except:
            return "error"
