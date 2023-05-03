class hangman:

    def __init__(self):
        self.MAX_TRIES = 6
        self.__HANGMAN_PHOTOS = {1: """ x-------x""", 2: """    x-------x
    |
    |
    |
    |
    |
 """, 3: """    x-------x
    |       |
    |       0
    |
    |
    |""", 4: """    x-------x
    |       |
    |       0
    |       |
    |
    |
""", 5: """    x-------x
    |       |
    |       0
    |      /|\\
    |
    |
""", 6: """    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |
""", 7: """    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |"""}

    def get_hangman_photos(self):
        return self.__HANGMAN_PHOTOS

    def openScreen(self):
        HANGMAN_ASCII_ART = """ 
            Welcome to the game Hangman
                _    _
               | |  | |
               | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
               |  __  |/ _' | '_ \ / _' | '_ ' _ \ / _' | '_ \\
               | |  | | (_| | | | | (_| | | | | | | (_| | | | |
               |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                                    __/ |
                                   |___/
            """

        print(HANGMAN_ASCII_ART + f"You have {self.MAX_TRIES} attempts to guess the word.")

    def is_valid_input(self, get_letter):

        if len(get_letter) > 1:
            return False

        if get_letter < 'a' and get_letter > 'Z' or get_letter > 'z' or get_letter < 'A':
            return False
        if ((get_letter >= 'a' and get_letter <= 'z') or (get_letter <= 'Z' and get_letter >= 'A')):

            return True
        else:

            return False

    def try_update_letter_guessed(self, letter_guessed, old_letters_guessed):
        flag = True
        try:
            index = old_letters_guessed.index(letter_guessed)
        except ValueError:

            index = -1
        if (self.is_valid_input(letter_guessed) == True and index == -1):
            old_letters_guessed.append(letter_guessed)

        else:
            print("X\n" + "->".join(sorted(old_letters_guessed)))
            flag = False
        return old_letters_guessed, flag

    def show_hidden_word(self, secret_word, old_letters_guessed):

        hidden_word = ""
        for letter in secret_word:
            if letter in old_letters_guessed:
                hidden_word += letter
            else:
                hidden_word += " _ "
        return hidden_word

    def check_in_word(self, letterguesses, secret_word):
        return letterguesses in secret_word

    def check_win(self, secret_word, old_letters_guessed):
        count = 0
        for letter in secret_word:
            if letter in old_letters_guessed:
                count += 1
        if count == len(secret_word):
            return True
        return False

    def print_hangman(self, num_of_tries):
        print(self.__HANGMAN_PHOTOS[num_of_tries])

    def choose_word(self, file_path, index):
        # read file and split into words
        f = open(file_path, "r")
        words = f.read().split()
        num_words = len(words)
        index = (index - 1) % num_words
        secret_word = words[index]
        unique_words = set(words)
        unique = len(unique_words)

        return (unique, secret_word)


def main():
    game = hangman()
    game.openScreen()
    file_path = input("Enter file path:")
    index = int(input("Enter index"))
    photos = game.get_hangman_photos()
    secret_word = game.choose_word(file_path, index)[1]
    old_letters_guessed = []
    game.print_hangman(1)
    print(game.show_hidden_word(secret_word, old_letters_guessed))
    numguesses = 2
    while (numguesses <= game.MAX_TRIES + 1):
        letterguess = input("enter letter: ")
        flag = game.is_valid_input(letterguess.lower())
        if (flag == False):
            print("X\n")
        if(flag==True):

            result = game.try_update_letter_guessed(letterguess.lower(), old_letters_guessed)
            old_letters_guessed = result[0]
            flag = result[1]

        if (flag == True):
            if game.check_in_word(letterguess.lower(), secret_word) == False:
                game.print_hangman(numguesses)
                numguesses += 1
            print(game.show_hidden_word(secret_word, old_letters_guessed))

        if (game.check_win(secret_word, old_letters_guessed) == True):
            print("WIN")
            break

    if (game.check_win(secret_word, old_letters_guessed) == False):
        print("LOST")

    # print(game.check_win(secret_word, old_letters_guessed))

    # get_letter = input("enter letter")
    # old_letters_guessed=['a','m','y']
    # game.try_update_letter_guessed(get_letter, old_letters_guessed)
    # print(game.show_hidden_word("may",old_letters_guessed))


# print(game.check_win("may",old_letters_guessed))
# game.print_hangman(6)
# print(game.choose_word('C:\\Users\\claude\\PycharmProjects\\pythonProject\\forhangman.txt',3))

if __name__ == '__main__':
    main()