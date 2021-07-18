from modules.GameRules import Rules


class Verifier:
    def commands(key_name: str, position: list):
        command = getattr(Rules, key_name, False)
        if command is not False:
            return command(position)

        return False
