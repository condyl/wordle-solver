# computer plays

import random
from words import get_allowed_guesses,get_answers

def run():
    allowed_guesses = get_allowed_guesses()
    possible_answers = get_answers()
    
    answer = random.choice(possible_answers)
    print(answer)

    for x in range(5):
        min_wordcount = 10000000
        guess = ""
        eval_map = {}
        
        
        if x != 0:
            possible_guesses = allowed_guesses
        else:
            possible_guesses = ["risen"]
    
        for word_to_guess in possible_guesses:
            temp_eval_map = {}
            
            for possible_answer in possible_answers:
                evaluation = get_evaluation(possible_answer, word_to_guess)
                        
                if tuple(evaluation) not in temp_eval_map:
                    temp_eval_map[tuple(evaluation)] = [possible_answer]
                else:
                    temp_eval_map[tuple(evaluation)].append(possible_answer)
    
    
            max_wordcount = max([len(val) for val in temp_eval_map.values()])
            
            if max_wordcount < min_wordcount:
                min_wordcount = max_wordcount
                guess = word_to_guess
                
                eval_map = temp_eval_map

        possible_answers = eval_map[get_evaluation(answer, guess)]
        
        word_results = []
        status = ["⬛","🟨","🟩"]
        for i in range(5):
            word_results.append(status[get_evaluation(answer, guess)[i]])
        print(''.join(word_results),guess)

        if len(possible_answers) == 1:
            print("🟩🟩🟩🟩🟩",possible_answers[0])
            return True
        
        
        
    return False
            
def get_evaluation(answer, word):
    output = [0, 0, 0, 0, 0]
    
    for i in range(5):
        if word[i] == answer[i]:
            output[i] = 2
            answer = answer[:i] + ' ' + answer[i + 1:]
           
    for i in range(5):
        char = word[i]
        if char in answer and output[i] == 0:
            output[i] = 1
            first_occurence = answer.find(char)
            answer = answer[:first_occurence] + ' ' + answer[first_occurence + 1:]
    return tuple(output)

run()