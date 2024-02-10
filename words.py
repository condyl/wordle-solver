def get_allowed_guesses():
    words = []
    with open("wordle-allowed-guesses.txt", "r") as f:
        for line in f:
            words.append(line.strip())
    return words

def get_answers():
    words = []
    with open("wordle-answers-alphabetical.txt", "r") as f:
        for line in f:
            words.append(line.strip())
    return words