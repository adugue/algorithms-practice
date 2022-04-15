voted = {"tom": True}

def check_voter(name):
    value = voted.get(name)
    if value:
        print("This person has already voted. Kick them out!")
    else:
        voted[name] = True
        print("Let them vote.")
