import random
from wordlist import wlist


def main():
    print("Instructions:\n\
        Guess a random alphabet. The length of the word will be mentioned.\n\
        You can guess only one alphabet at a time.\n\
        For every wrong alphabet a body part is added to the hangman.\n\
        You have chances till the hangman figure completes, which means you'll have 8 chances in all.\n\
        Guess the word before you run out of chances.\n")
    secret=random.choice(wlist).upper()
    word=[]
    for c in secret:
        if c.isalpha():
            word.append("_")
        else:
            word.append(c)
    print(" ".join(word))
    chances=8
    while chances>0:
        letter=guessing()
        if letter in secret:
            word=fill_blank(secret,word,letter)
            print("Incorrect guesses remaining: "+str(chances))
            print(hangman(chances))
            print(" ".join(word))
            if "".join(word)==secret:
                print("You won! The secret word was: "+secret)
                break

        else:
            chances-=1
            print("Incorrect guesses remaining: "+str(chances))
            print(hangman(chances))
            print(" ".join(word))
            if chances==0:
                print("GAME OVER :( The secret word was: "+secret)

def guessing():
    while True:
        letter=input("Please enter an alphabet: ")
        if len(letter)==1 and letter.isalpha():
            return letter.upper()
        else:
            continue

def fill_blank(secret,word,letter):
    for i in range(len(secret)):
        if secret[i]==letter:
            word[i]=letter
    return word

def hangman(chances):
    step=["_____\n|\n|\n|\n_____",
    "_____\n|\n|  O  \n|\n|\n_____",
    "_____\n|\n|  O  \n|  |  \n|\n_____",
    "_____\n|\n|  O  \n| /|  \n|\n_____",
    "_____\n|\n|  O  \n| /|\ \n|\n_____",
    "_____\n|\n|  O  \n| /|\ \n| /   \n_____",
    "_____\n|\n|  O  \n| /|\ \n| / \ \n_____",
    "____\n|  |  \n|  O  \n| /|\ \n| / \ \n_____",
    "____\n\n HANGMAN DEAD :( \n_____"]
    return step[8-chances]

'''
-_____
|  |
|  O
| /|\
| / \
'''

if __name__=="__main__":
    main()
