name = input("Enter a username for this game: ")
print("Welcome to Riddle Riddle, " + name + "!")


def riddle():
    print("Pick the level of difficulty you want:")
    print("1. Easy Riddles")
    print("2. Medium Riddles")
    print("3. Hard Riddles")
    try:
        choice = int(input("Enter 1, 2, or 3: "))
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 3.")
        return
    trials = 0
    trial_limit = 3

    if choice == 1:
        answer = "what"
        while trials < trial_limit:
            user_input = input("A dog has 3 puppies: Monday, Tuesday, and Wednesday. What is the mother's name? ")
            if user_input.lower() == answer:
                print("Correct! Well done!")
                break
            else:
                trials += 1
                if trials < trial_limit:
                    print(f"Wrong answer! Try again. Attempts left: {trial_limit - trials}")
                else:
                    print("You are out of trials!")
    elif choice == 2:
        answer = "7"
        user_input = input("I am an odd number. Take away a letter, and I become even. What number am I? ")
        if user_input == answer:
            print("Correct! Great job!")
        else:
            print("Wrong answer! The correct answer is 7.")
    elif choice == 3:
        answer = "what is the time"
        user_input = input(
            "Ask this question all day long, but always get completely different answers, and yet all the answers will be correct. What is the question? ")
        if user_input.lower() == answer:
            print("Correct! You're a genius!")
        else:
            print("Wrong answer! The correct answer is 'What is the time?'.")
    else:
        print("Invalid choice. Please select a number between 1 and 3.")



riddle()
