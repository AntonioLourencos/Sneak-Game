from os import error, walk
from datetime import date


class Verifier:
    def files():

        listJson = ["fruitColor", "bodySneak", "velocity", "display"]

        print("Starting files verifier.")

        try:
            with open("./src/config/sneak.json") as f:
                file = f.read()

                for item in listJson:
                    if(item in file) == False:
                        count = 0
                        day = date.today()

                        for files in walk("./report"):
                            files = files[2]
                            for item in files:
                                if "Log_Error" in item:
                                    count = count + 1

                        model = open(
                            "./src/utils/views/errors/loadingFile.model.txt")
                        model_Read = model.read()
                        model_Read = model_Read.replace("date", str(day))
                        model.close()

                        new_File = open(
                            f"./report/Log_Error_{day}({count}).txt", "a+")
                        new_File.write(model_Read)
                        new_File.close()

                        raise Exception("Missing arguments!")

                print("The files was verifier.")

        except(error):
            return error
