import random

# Predefined word list
word_list = ["apple", "grape", "mango", "lemon", "peach"]
word_to_guess = random.choice(word_list)

# Game setup
guessed_letters = []
tries = 6
display_word = ["_" for _ in word_to_guess]
a
print("🎮 Welcome to Hangman!")
print("Guess the word by typing one letter at a time.")
print("You have 6 chances to guess incorrectly.\n")

# Game loop
while tries > 0 and "_" in display_word:
    print("Word: ", " ".join(display_word))
    print("Guessed letters: ", " ".join(guessed_letters))
    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("❗ Please enter a single alphabet letter.\n")
        continue

    if guess in guessed_letters:
        print("⚠️ You've already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    if guess in word_to_guess:
        print("✅ Correct guess!\n")
        for i, letter in enumerate(word_to_guess):
            if letter == guess:
                display_word[i] = guess
    else:
        tries -= 1
        print(f"❌ Wrong guess! Tries left: {tries}\n")

# Final result
if "_" not in display_word:
    print("🎉 Congratulations! You guessed the word:", word_to_guess)
else:
    print("💀 Game Over! The word was:", word_to_guess)
