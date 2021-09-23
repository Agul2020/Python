import random
HANGMAN_PICS = ['''
+---+
|
|
|
===''', '''
+---+
O   |
|
|
===''', '''
+---+
O   |
|   |
|
===''', '''
+---+
O   |
/|   |
|
===''', '''
+---+
O   |
/|\  |
|
===''', '''
+---+
O   |
/|\  |
/    |
===''', '''
+---+
O   |
/|\  |
/ \  |
===''']
# 单词 （各种动物~~）
words = '''ant baboon badger bat bear beaver camel cat clam cobra cougar 
coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk
lion lizard llama mole monkey moose mouse mule newt otter owl panda
parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep
skunk sloth snake spider stork swan tiger toad trout turkey turtle
weasel whale wolf wombat zebra'''.split() # 将字符串分割为一个个单词得到一张列表，每个单词都是该列表中的一个元素

def getRandomWord(wordList):
# This function returns a random string from the passed list of strings.
# 这个函数将随机返回 worldList 中的一个单词
 wordIndex = random.randint(0, len(wordList) - 1)
 return wordList[wordIndex]

def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('Missed letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)): # Replace blanks with correctlyguessed letters. / 用猜出的正确字母替换空格
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks: # Show the secret word with spaces in between each letter. / 打印 blanks 中的新值，每个字母之间都有空格隔开
        print(letter, end=' ')
print()

def getGuess(alreadyGuessed):
# Returns the letter the player entered. This function makes sure the player entered a single letter and not something else.
# 返回玩家输入的字母。这个函数确保玩家输入了一个有效的字母
 while True:
    print('Guess a letter.')
    guess = input()
    guess = guess.lower()
    if len(guess) != 1:
        print('Please enter a single letter.')
    elif guess in alreadyGuessed:
        print('You have already guessed that letter. Choose again.')
    elif guess not in 'abcdefghijklmnopqrstuvwxyz':
        print('Please enter a LETTER.')
    else:
        return guess

def playAgain():
# This function returns True if the player wants to play again;otherwise, it returns False.
# 这个函数询问玩家是否继续游戏
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')


print('H A N G M A N')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
    displayBoard(missedLetters, correctLetters, secretWord)

    # Let the player enter a letter.
    # 让玩家输入一个字母
    guess = getGuess(missedLetters + correctLetters) # 将玩家猜过的字母作为 alreadyGuessed 参数传递

    if guess in secretWord:
        correctLetters = correctLetters + guess

        # Check if the player has won.
        # 判断玩家是否获胜
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Yes! The secret word is "' + secretWord +'"! You have won!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        # Check if player has guessed too many times and lost.
        # 判断玩家是否猜了过多次输了游戏
        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('You have run out of guesses!\nAfter ' +
            str(len(missedLetters)) + ' missed guesses and ' +
            str(len(correctLetters)) + ' correct guesses,the word was "' + secretWord + '"')
            gameIsDone = True

    # Ask the player if they want to play again (but only if the game isdone).
    # 询问玩家是否继续游戏
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = getRandomWord(words)
        else:
            break
        