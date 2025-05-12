import random

def read_words_from_file(filename):
    with open(filename, 'r') as file:
        words = [line.strip().lower() for line in file if line.strip()]
    return words

def get_category(word):
    # Simple categorization based on word length (customize as needed)
    if len(word) <= 5:
        return "Short Fruit"
    elif len(word) <= 7:
        return "Medium Fruit"
    else:
        return "Long Fruit"

def play_game():
    words = read_words_from_file('words.txt')
    selected_word = random.choice(words)
    category = get_category(selected_word)
    guessed_letters = set()
    attempts = 6
    print("\nWelcome to the Interactive Word Guessing Game!")
    print(f"Hint: The word is a {category} with {len(selected_word)} letters.")

    while attempts > 0:
        display_word = ' '.join([letter if letter in guessed_letters else '_' for letter in selected_word])
        print(f"\nWord: {display_word}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
        print(f"Attempts left: {attempts}")
        guess = input("Guess a letter: ").lower().strip()

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single alphabetic character.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in selected_word:
            print("Good guess!")
            if all(letter in guessed_letters for letter in selected_word):
                print(f"\nCongratulations! You guessed the word: {selected_word}")
                break
        else:
            print("Wrong guess.")
            attempts -= 1

    else:
        print(f"\nGame Over! The word was: {selected_word}")

if __name__ == "__main__":
    while True:
        play_game()
        again = input("\nPlay again? (Y/N): ").strip().lower()
        if again != 'y':
            print("Thank you for playing!")
            break
