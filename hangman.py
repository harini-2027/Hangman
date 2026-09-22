import random
#different stages of the hangman 
hangman_stages = ["""
--------
 |      |
 |
 |
 |
 |
- - - - -
""",
"""
 --------
 |      |
 |      O
 |      
 |      
 |      
- - - - -
""",
"""
 --------
 |      |
 |      O
 |      |
 |      |
 |      
 |      
- - - - -
""",
"""
 --------
 |      |
 |      O
 |     /| 
 |      |
 |      
- - - - -
""",
"""
 --------
 |      |
 |      O
 |     /|\
 |      |
 |      
- - - - -
""",
"""
  --------
  |      |
  |      O
  |     /|\
  |      |
  |     / 
- - - - -
""",
"""
  --------
  |      |
  |      O
  |     /|\
  |      |
  |     / \
- - - - -
"""]
#list of possible words
#the secret word will be selected from this list
words_list = ["apple", "mango", "banana", "grapes", "strawberry", "watermelon", "pineapple", "cherry"]
#stores all the letters guessed by the player
guessed_letters = []
secret_word = random.choice(words_list)
#maximum number of attempts allowed 
max_attempts = 6
#keeps track of how many wrong guesses player has made
wrong_attempts = 0
print("welcome to hangman game!")
print("can you guess the word?")
#main loop for game
while wrong_attempts < max_attempts:
#display the appropriate hangman stages
    print(hangman_stages[wrong_attempts])
#display guessed letters and underscore unguessed letters
    word_display = ""

    for letter in secret_word:
        if letter in guessed_letters:
            word_display += letter + " "
        else:
            word_display+= "_"
    print("word to guess: " + word_display)
    print(f"attempts remaining: {max_attempts - wrong_attempts}")
#check if the player has successfully guessed the entire word
    if "_" not in word_display:
        print(f"\n congratulations! you guessed the word: '{secret_word.upper()}'!")
        break         
    guess = input("guess a letter: ").lower()
#validate the players input
    if len(guess) !=1 or not guess.isalpha():
        print("please enter a single valid letter")
    elif guess in guessed_letters:
        print("you have already guessed that letter, try again!")
#handling the correct guess
    elif guess in secret_word:
        print(f"Great!'{guess}' is in the word")
        guessed_letters.append(guess)
#handle an incorrect guess
    else:
        print(f"sorry! '{guess}' is not in the word")
        wrong_attempts += 1
#display the final stage and reveal the word if the player looses   
if wrong_attempts == max_attempts:
    print(hangman_stages[wrong_attempts])
    print(f"Game over!you ran out of lives. The word was: '{secret_word}' ")   