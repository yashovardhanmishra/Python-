from questions import*
def game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("-----------------")
        print(key)

        for i in options[question_num-1]:
            print(i)

        guess = input("Choose the correct ansewr: ")
        guess = guess.upper()
        guesses.append(guess)
          

        correct_guesses+=check_answer(questions.get(key), guess)
        question_num+=1
        
    display_score(correct_guesses, guesses)
        
    score = int(correct_guesses/len(questions)*100)
    print(f"YOUR SCORE IS {score}%")
    

def check_answer(answer, guess):
    if answer == guess:
        print("CORRECT")
        return 1
    else:
        print("WRONG")
        return 0
    

def display_score(correct_guesses, guesses):
    print("-----------")
    print("Result")
    print("-----------")
    
    print("ANSWERS: ")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("GUESSES: ")
    for i in  guesses:
        print(i, end=" ")
    print()

def play_again():
    ask = input("WANNA PLA AGAIN? (yes/no):")
    ask = ask.upper()

    if ask == "YES":
        return True

    else:
        return False

game()

while play_again():
    game()
