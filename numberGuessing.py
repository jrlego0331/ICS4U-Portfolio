from random import randint
levels = [(1,10),  (1,50), (1,100)]
print('Guess the Number! \n 1. Easy', levels[0], ' 2. Experienced', levels[1], ' 3. Hard', levels[2])
guessCount = 0

while True:    
    try: 
        difficulty = int(input('Your Difficulty: '))
        answer = randint(levels[difficulty-1][0], levels[difficulty-1][1])
        print('You have chosen: ', difficulty)
        break
    except: print('error: choose an integer between 1~3')


while True:
    try:
        guessCount+=1
        guess = int(input('Your Guess: '))
        if answer == guess: break
        if answer > guess: print('Too Small')
        if answer < guess: print('Too Big')  
    except: print('Input must be between an integer!')

print('You got it in', guessCount, 'tries')