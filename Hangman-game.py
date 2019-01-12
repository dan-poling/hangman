
def hangman():

    import random
    wordlist = ['aligator','train','gumbo', 'dinosaur']
    word = random.choice(wordlist)

    print("Welcome to Hangman, where a man's life hangs in the balance.")
    print('The word is this many letters: {}'.format(len(word)))
    
    wrong = 0
    stages = ['_____   ',
              '|   |   ',
              '|   o   ',
              '|  /|\  ',
              '|  / \  ',
              '|       '
             ]

    rletters = list(word)
    board = [' __ '] * len(word)
    win = False

    while wrong < len(stages) - 1:
        print('\n')
        x = input('Guess a letter: ')
        
        # if guess is in the word
        if x in rletters:
            cind = rletters.index(x)
            board[cind] = x
            rletters[cind] = '$'

        # if guess is not in the word
        else:
            wrong += 1
            print('Wrong!')

        # we need to see the board
        print('\n')
        print(''.join(board))

        # we need to see the man get hanged as guesses are wrong
        e = wrong
        print('\n'.join(stages[0:e]))

        # once all the open spaces are replaced with correct guesses:
        if ' __ ' not in board:
            print("A criminal went free b guessing letters. How's it feel to subvert justice?")
            print(' '.join(board))
            win = True
            break

    #some unnecessary comment to test change commits
    if not win:
        print('\n'.join(stages[0:wrong]))
        print("An innocent man died today all because you couldn't guess {}.".format(word))

hangman()
