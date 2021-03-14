mode = input("Mode? ")
rounds = ""

while rounds == "" or rounds > 0:

    if rounds == "":
        heading = "Continuous"

    else:
        heading = "Something else"
        rounds = "0"
        rounds -= 1

    choice = input("Choose: ")