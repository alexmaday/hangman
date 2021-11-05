print("HANGMAN")
print("-------")

secret_word = "rubiks"
guess_count = 0
letters_solved = 0

# variable to hold the solution as the game progresses
the_solve = list('_' * len(secret_word))

while (guess_count < len(secret_word) and letters_solved != len(secret_word)):
    guess = input("What is your guess? ")
    correct_guesses = 0     # correctly guessed letters this iteration
    if (guess in secret_word):
        # where in the word is it? It could be multiple places
        index = 0
        while index < len(secret_word):

            if guess == secret_word[index]:
                letters_solved += 1
                correct_guesses += 1
                the_solve[index] = guess
            index += 1
    else:
        print(f"Sorry, there are no {guess}'s")

    guess_count += 1
    # display the current state of the solve
    print(f"There are {correct_guesses} {guess}'s")
    for letter in the_solve:
        print(letter, end='')
    print('\n')

if letters_solved == len(secret_word):
    print("You correctly solved the puzzle!")
else:
    print(
        f"Sorry, you did not solve the puzzle, the secret word was {secret_word}")
