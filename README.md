# __Hangman__
#### Video Demo: https://www.youtube.com/watch?v=pq1OG_LmVEg&t=4s

## __Definition__
 This project is an interactive hangman game in which the user has to guess words within a limited number of chances.

 Project structure :
 - project.py
 - test_project.py
 - README.md

## __Libraries__

__random__: Python Random module is an in-built module of Python which is used to generate random numbers. [(Readmore)](https://docs.python.org/3/library/random.html)

__pytest__: It will automate the tests as long as you write the bsic test cases. [(Readmore)](https://docs.pytest.org/en/7.2.x/)

## **Installing Libraries**
Libraries can simply be installed by this pip command:

```pip install -r requirements.txt```

## _Usage__

```python project.py```
```
$ cd project
project/ $ python project.py
Instructions:
        Guess a random alphabet. The length of the word will be mentioned.
        You can guess only one alphabet at a time.
        For every wrong alphabet a body part is added to the hangman.
        You have chances till the hangman figure completes, which means you'll have 8 chances in all.
        Guess the word before you run out of chances.

_ _ _ _ _ _ _
Please enter an alphabet: a
Incorrect guesses remaining: 7
_____
|
|  O
|
|
_____
_ _ _ _ _ _ _
Please enter an alphabet: s
Incorrect guesses remaining: 7
_____
|
|  O
|
|
_____
_ _ S _ _ _ _
Please enter an alphabet: t
Incorrect guesses remaining: 7
_____
|
|  O
|
|
_____
_ _ S _ _ _ T
Please enter an alphabet: b
Incorrect guesses remaining: 6
_____
|
|  O
|  |
|
_____
_ _ S _ _ _ T
Please enter an alphabet: e
Incorrect guesses remaining: 6
_____
|
|  O
|  |
|
_____
_ E S _ E _ T
Please enter an alphabet: v
Incorrect guesses remaining: 5
_____
|
|  O
| /|
|
_____
_ E S _ E _ T
Please enter an alphabet: p
Incorrect guesses remaining: 5
_____
|
|  O
| /|
|
_____
_ E S P E _ T
Please enter an alphabet: r
Incorrect guesses remaining: 5
_____
|
|  O
| /|
|
_____
R E S P E _ T
Please enter an alphabet: c
Incorrect guesses remaining: 5
_____
|
|  O
| /|
|
_____
R E S P E C T
You won! The secret word was: RESPECT
```

## __Functioning__

The project.py contains 4 functions including the main function. These functions are as follows:

### _guessing()_:
This function checks that the character enetred by user is valid or not.

### _fill_blank()_:
This function inputs the alphabet in the given balnks if it exists in the word and also displays the complete word at the end.

### _hangman()_:
This function is used to display the different figures of hangman according to the number of chances left.

### Author : Jasleen Kaur
