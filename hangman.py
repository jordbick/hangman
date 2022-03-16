import random
from hangman_words import word_list
import hangman_art as A


# Choose word from list at random
chosen_word = random.choice(word_list)

# Create list containing _ as long as word
display = []
for letter in chosen_word:
    display.append("_")

lives = 6

# User input in lower case


# Check if letter is contained within word
# Use range function to get position of letter

end_of_game = False

print(A.logo)
while end_of_game == False:
    guess = input("Guess a letter: ").lower()
    if guess in display:
      print(f"You have already guessed the letter {guess}")
    for i in range(len(chosen_word)):
        if guess == chosen_word[i]:
          display[i] = guess
    if guess not in chosen_word:
      print(f"{guess} is not in the word")
      lives -=1
    print(f"{' '.join(display)}")
    print(A.stages[lives])
    if "_" not in display:
        end_of_game = True
        print("You won!")
    elif lives == 0:
        end_of_game = True
        print("The word was " + chosen_word)
        print("You lose!")
