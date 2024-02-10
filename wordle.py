# user plays

from words import get_allowed_guesses, get_answers
import random

allowed_guesses = get_allowed_guesses()
possible_answers = get_answers()

def run():
    answer = random.choice(possible_answers)
    print(answer)

    print("Guess a word:\n")

    for x in range(6):
        guess = input()

        validated = validate(answer,guess)
        if validated == "🟩🟩🟩🟩🟩":
            break
            
def validate(answer, guess):
    status = ["⬛","🟨","🟩"]
    if guess == answer:
        print(f'{status[2]}{status[2]}{status[2]}{status[2]}{status[2]} {guess}')
        return "🟩🟩🟩🟩🟩"
    else:
        word_results = []
        for char_index in range(5):
            if guess[char_index] == answer[char_index]:
                word_results.append(status[2])
            elif guess[char_index] in answer:
                word_results.append(status[1])
            else:
                word_results.append(status[0])
        
        print(''.join(word_results),guess)
    return ''.join(word_results)

run()