questions = {
    'Earth is round?':'A',
    'We are?':'B',
    'Which of theme animal eats grass?':'C',
    'Eagle is':'D',
    'Humans have __________ bones.':'D',
    'Octopus have _______ bones':'A',
    'Snake is a':'C',
    'Sun is ':'D',
    'Bones are made up of?':'C',
    'Wheels are made of?':'B',
    "World's biggest mammal is":'A',
}

options = [
    ['A. True','B.False', "C.Don't know", 'D.Maybe'],
    ['A. Animals','B.Humans', "C.bird", 'D.DK'],
    ['A. Lion','B.Dog', "C.Cow", 'D.Cat'],
     ['A. Reptile','B.Cat', "C.Don't know", 'D.Bird'],
    ['A. 210','B.306', "C.Don't know", 'D.206'],
    ['A. No','B.300', "C.120", 'D.100'],
    ['A. Insect','B.Bird', "C.Reptile", 'D.DK'],
    ['A. Warm','B.Neutral', "C.Cold", 'D.Hot'],
    ['A. Fat','B.Protien', "C.Calcuim", 'D.Magnesium'],
    ['A. Copper','B.Rubber', "C.Steel", 'D.Iron'],
    ['A. Blue Whale','B.Mammath', "C.Shark", 'D.Giraffe'],
]


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
