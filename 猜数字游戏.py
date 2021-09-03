# This is a Guess the Number game.

import random # 导入 andom 模块，以便程序可以调用 random.randint() 函数
guessesTaken = 0 # 玩家猜过的次数
print('Hello! What is your name?')
myName = input() # 要求用户输入姓名

number = random.randint(1,20) # 产生一个随机数，保存到变量 number 中。这就是玩家试图猜测的神秘数字
print('Well, ' + myName + ' , I am thinking of a number between 1 and 20.')

for i in range(6): # 循环6次      i的范围为0~5
    print('Take a guess.')
    guess = input() # 要求用户输入猜的数  
    guess = int(guess) # 将用户输入的数转换为整数值

    if guess < number:
        print('Your guess is too low.')

    if guess > number:
        print('your guess is too high.')

    if guess == number:
        break

if guess == number:
    guessesTaken = str(i+1) #将用户猜过的次数转化为字符串型 
    print('Good job, ' +myName + '! you guessed my number in ' + guessesTaken + ' guesses!')

if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number + '.')
        
    
    
    


