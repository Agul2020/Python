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
===,
+---+
[O   |
/|\  |
/ \  |
===,
+---+
[O]   |
/|\  |
/ \  |
==='''
]
# 单词 （颜色 形状 水果 动物）
words = {'Colors':'red orange yellow green blue indigo violet white black brown'.split(),
 'Shapes':'square triangle rectangle circle ellipse rhombus trapezoid chevron pentagon hexagon septagon octagon'.split(),
'Fruits':'apple orange lemon lime pear watermelon grape grapefruit cherry banana cantaloupe mango strawberry tomato'.split(), 
'Animals':'bat bear beaver cat cougar crab deer dog donkey duck eagle fish frog goat leech lion lizard monkey moose mouse otter owl panda python rabbit rat shark sheep skunk squid tiger turkey turtle weasel whale wolf wombat zebra'.split()}

def getRandomWord(wordDict):
    # This function returns a random string from the passed from the passed dictionary of lists of lists of strings and its key. //此函数从传递的字符串列表列表及其 key 的传递字典中返回一个随机字符串。
    # First, randomly select a key from the dictionary: //首先，从字典中随机选择一个 key： 
    wordKey = random.choice(list(wordDict.keys()))

    # Second,randomly select a word from the key's list in the dictionary:其次，从字典的 key 列表中随机选择一个单词：
    wordIndex = random.randint(0, len(wordDict[wordKey]) - 1)
    
    return [wordDict[wordKey][wordIndex], wordKey]

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
difficulty = 'X'
while difficulty not in 'EMH':
     print('Enter difficulty: E - Easy, M - Medium, H - Hard')
     difficulty = input().upper()
if difficulty == 'M':
     del HANGMAN_PICS[8]
     del HANGMAN_PICS[7]
if difficulty == 'H':
     del HANGMAN_PICS[8]
     del HANGMAN_PICS[7]
     del HANGMAN_PICS[5]
     del HANGMAN_PICS[3]

missedLetters = ''
correctLetters = ''
secretWord,secretSet= getRandomWord(words)
gameIsDone = False

while True:
    print('The secret word is in the set:'+ secretSet)
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
            secretWord,secretSet = getRandomWord(words)
        else:
            break
        