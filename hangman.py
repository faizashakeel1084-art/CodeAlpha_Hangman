import random

WORDS = ["python", "keyboard", "internet", "program", "variable"]
MAX_WRONG = 6


def show_progress(word, guessed):
    """Return the word with unguessed letters hidden, e.g. p _ t h _ n"""
    return " ".join(letter if letter in guessed else "_" for letter in word)


def play():
    word = random.choice(WORDS)
    guessed = []          # all letters guessed so far
    wrong = 0

    print("=== HANGMAN ===")
    print(f"Guess the word. You can make {MAX_WRONG} wrong guesses.\n")

    while wrong < MAX_WRONG:
        print("Word:", show_progress(word, guessed))
        print("Guessed:", " ".join(sorted(guessed)) if guessed else "-")
        print(f"Wrong guesses left: {MAX_WRONG - wrong}")

        guess = input("Enter a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.\n")
            continue
        if guess in guessed:
            print("You already guessed that letter.\n")
            continue

        guessed.append(guess)

        if guess in word:
            print("Correct!\n")
        else:
            wrong += 1
            print("Wrong!\n")

        if all(letter in guessed for letter in word):
            print("Word:", show_progress(word, guessed))
            print(f"You won! The word was '{word}'.")
            return

    print(f"Game over! The word was '{word}'.")


def main():
    while True:
        play()
        again = input("\nPlay again? (y/n): ").lower().strip()
        if again != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
