from os import system
from time import sleep
from modules.Inicialize import Sneak


def SneakSystem(count: int = 0):
    system("clear")

    try:
        if(count >= 1):
            question = str(input(
                f"There have already been {count} mistake(s), will you try again? (Y/N) "))

            question.lower()

            if(question == ""):
                count = count + 1
                print("Input is undefined")
                sleep(2)
                return SneakSystem(count)
            elif(("y" in question or "n" in question) is False):
                count = count + 1
                print("Your answer should be Y or N")
                sleep(2)
                return SneakSystem(count)
            elif(question is "n"):
                return Sneak.close()
            elif(question is "y"):
                pass
            else:
                count = count + 1
                return SneakSystem(count)

        game: function = Sneak.start()

        if(game == "error"):
            count = count + 1
            print(
                "Sorry about the incident, we will send a report to the folder ./Report, please wait 10 seconds.")
            sleep(10)
            return SneakSystem(count)

    except:
        count = count + 1
        print("Error...")
        SneakSystem(count)


SneakSystem()
