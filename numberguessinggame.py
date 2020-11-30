import random

running = True
while running:
    # functions
    def easy():
        easy_numbers = random.randint(0, 20)
        hint_easy_numbers_add = [2, 4, 6]
        easy_numbers_hint = easy_numbers + random.choice(hint_easy_numbers_add)
        print(f"\n\nHint: {easy_numbers_hint}")
        guess_the_number_easy = float(input("Guess the number!: "))
        if guess_the_number_easy == easy_numbers:
            print("\n\nYou won! Congratulations!")
        else:
            print("\n\nYou lost! Better luck next time!")
    
    def medium():
        medium_numbers = random.randint(0, 50)
        hint_medium_numbers = [2, 3, 5, 7, 10]
        medium_hint = [
            medium_numbers + random.choice(hint_medium_numbers),
            medium_numbers - random.choice(hint_medium_numbers)
        ]
        medium_number_hint = random.choice(medium_hint)
        print(f"\n\nHint: {medium_number_hint}")
        guess_the_number_medium = float(input("\n\nGuess the number!: "))
        if guess_the_number_medium == medium_numbers:
            print("\n\nYou won! Congratulations!")
        else:
            print("\n\nYou lost! Better luck next time!")

    def hard():
        hard_numbers = random.randint(0, 80)
        hard_hint_numbers = [4, 8, 12, 16, 20]
        hard_hint = [
            hard_numbers - random.choice(hard_hint_numbers),
            hard_numbers * random.choice(hard_hint_numbers)
        ]
        hard_number_hint = random.choice(hard_hint)
        print(f"\n\nHint: {hard_number_hint}")
        guess_the_number_hard = float(input("\n\nGuess the number!: "))
        if guess_the_number_hard == hard_numbers:
            print("\n\nYou won! Congratulations")
        else:
            print("\n\nYou lost! Better luck next time!")
    
            
    def extreme():
        extreme_numbers = random.randint(0, 100)
        extreme_hint_numbers = [6, 12, 18, 24, 30]
        extreme_hint = [
            extreme_numbers * random.choice(extreme_hint_numbers),
            extreme_numbers / random.choice(extreme_hint_numbers)
        ]
        extreme_number_hint = random.choice(extreme_hint)
        print(extreme_number_hint)
        guess_the_number_extreme = float(input("\n\nGuess the number!: "))
        if guess_the_number_extreme == extreme_numbers:
            print("\n\nYou won! Congratulations!")
        else:
            print("\n\nYou lost! Better luck next time!")
    # welcome
    print("\n\nWelcome to the guessing game")

    ready = input("\n\nReady to play?: ")
    
    if ready == "Ready":
        difficulty = input("\n\nWhat difficulty do you want? type help for a list of difficulties: ")
        if difficulty == "help":
            print("NOTE: CASE SENSITIVE:\n\nEasy\n\nMedium\n\nHard\n\nExtreme")
            difficulty_choice_after_help = input("\n\nWhat difficulty would you like? type help for explaining of difficulties: ")
            if difficulty_choice_after_help == "help":
                print("\n\nEasy: Numbers are from 0 to 20, guessing the number is easier"
                      "\n\nhint number is added to the true number only.")
                print("\n\nMedium: Numbers are from 0 to 50, guessing the number is quite harder than easy."
                      "\n\nhint number can be added or removed to the true number only")
                print("\n\nHard: Numbers are from 0 to 80, guessing the number is much harder than easy and harder than medium."
                      "\n\nhint number can be removed or multiplied to the true number only")
                print("\n\nExtreme: Numbers are from 0 to 100, guessing rhe number is the hardest in this difficulty and should only be tried if you're good at this game"
                      "\n\nhint number can be multiplied or divided to the true number only")
            elif difficulty_choice_after_help == "exit":
                running = False
            elif difficulty_choice_after_help == "Easy":
                easy()
            elif difficulty_choice_after_help == "Medium":
                medium()
            elif difficulty_choice_after_help == "Hard":
                print("\n")
                hard()
            elif difficulty_choice_after_help == "Extreme":
                extreme()
            else: 
                break 
        elif difficulty == "Extreme":
            extreme() 
        elif difficulty == "Hard":
            hard()
        elif difficulty == "Medium":
            medium()
        elif difficulty == "Easy":
            easy()
        if difficulty == "exit":
            running = False
        else: 
            break
    elif ready == "exit":
        running = False
    else: 
        break
    