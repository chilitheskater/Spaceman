
import random

def load_word():
    '''
    A function that reads an array of words and randomly selects one to use as the secret word
        from the list.

    Returns: 
           string: The secret word to be used in the spaceman guessing game
    '''
    words_list = ["monkey", "autumn", "tree", "coffee", "patience", "sparrow", "homework", "computer" ]

    #words_list = words_list[0].split(' ') #comment this line out if you use a words.txt file with each word on a new line
    secret_word = random.choice(words_list)
    return secret_word

    
    secret_word = random.choice(words_list)
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.

    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.

    Returns: 
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True

def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.

    Args: 
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.

    Returns: 
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, show an _ (underscore) instead.
    '''
    guessed_word = ""
    for letter in secret_word:
        if letter in letters_guessed:
            guessed_word += letter
        else:
            guessed_word += "_"
    return guessed_word

def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word

    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word

    Returns:
        bool: True if the guess is in the secret_word, False otherwise
    '''
    return guess in secret_word

def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.

    Args:
        secret_word (string): the secret word to guess.
    '''
    word_completion = "_" * len(secret_word)
    guessed = False
    guessed_letters = []
    tries = 7  # Adjust this number as per your game rules

    print("Let's play Spaceman!")
    print(display_spaceman(tries))
    print(word_completion)
    print("\n")

    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").upper()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed that letter.")
            elif guess in secret_word:
                guessed_letters.append(guess)
                word_completion = get_guessed_word(secret_word, guessed_letters)
            else:
                tries -= 1
                print("Incorrect guess. You have {} tries left.".format(tries))
        elif len(guess) == len(secret_word) and guess.isalpha():
            if guess == secret_word:
                guessed = True
                word_completion = secret_word
            else:
                tries -= 1
                print("Incorrect word guess. You have {} tries left.".format(tries))
        else:
            print("Invalid input. Please guess a single letter or the entire word.")

        print(display_spaceman(tries))
        print(word_completion)
        print("\n")

    if guessed:
        print("Congratulations, you won! The word is:", secret_word)
    else:
        print("You ran out of attempts. The word was:", secret_word)

# Define a function to display the spaceman
def display_spaceman(tries):
    spaceman = [
        """
           +---+
               |
               |
               |
              ===""",
        """
           +---+
           |   |
               |
               |
              ===""",
        """
           +---+
           |   |
           O   |
               |
              ===""",
        """
           +---+
           |   |
           O   |
           |   |
              ===""",
        """
           +---+
           |   |
           O   |
          /|   |
              ===""",
        """
           +---+
           |   |
           O   |
          /|\\  |
              ===""",
        """
           +---+
           |   |
           O   |
          /|\\  |
          /    ===""",
        """
           +---+
           |   |
           O   |
          /|\\  |
          / \\  ==="""
    ]

    return spaceman[6 - tries]  # Display the corresponding spaceman

def new_func(load_word):
    return load_word()
if __name__ == "__main__":
    secret_word = new_func(load_word)
    spaceman(secret_word)