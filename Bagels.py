import random 

NUM_DIGITS = 3 # 答案中数字的位数
MAX_GUESS = 10 # 玩家所能够猜测的次数

def getSecretNum():
    # Returns a string of unique random digits that is NUM_DIGITS long.
    numbers = list(range(10)) # numbers 是包含0~9的一个列表 
    random.shuffle(numbers) # 随机修改列表元素的顺序
    secretNum = '' # secretNum 包含了一个字符串而不是一个整数
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i]) 
    return secretNum

def getClues(guess, secretNum):
    # Returns a string with the Pico, Fermi, & Bagels clues to the user. /计算要给的线索
    if guess == secretNum:
        return 'You got it!'

    clues = []
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Fermi')
        elif guess[i] in secretNum:
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels'

    clues.sort() # 去除线索中和顺序相关的额外信息
    return ' '.join(clues)

def isOnlyDigits(num):
    # Returns True if num is a string of only digits. Otherwise, returns False. / 判断玩家是否输入一个有效的猜测
    if num == '':
        return False

    for i in num:
        if i not in '0 1 2 3 4 5 6 7 8 9'.split():
            return False

    return True


print('I am thinking of a %s-digit number. Try to guess what it is.' % (NUM_DIGITS))
print('The clues I give are...')
print('When I say:    That means:')
print(' Bagels        None of the digits is correct.')
print(' Pico          One digit is correct but in the wrong position.')
print(' Fermi         One digit is correct and in the right position.')

while True:
    secretNum = getSecretNum()
    print('I have thought up a number. You have %s guesses to get it.' %
        (MAX_GUESS))

    guessesTaken = 1 # 记录是第几次猜测
    while guessesTaken <= MAX_GUESS:
        guess = ''
        while len(guess) != NUM_DIGITS or not isOnlyDigits(guess):
            print('Guess #%s: ' % (guessesTaken))
            guess = input()

        print(getClues(guess, secretNum))
        guessesTaken += 1

        if guess == secretNum:
            break
        if guessesTaken > MAX_GUESS:
            print('You ran out of guesses. The answer was %s.' %
                (secretNum))

    print('Do you want to play again? (yes or no)')
    if not input().lower().startswith('y'):
        break