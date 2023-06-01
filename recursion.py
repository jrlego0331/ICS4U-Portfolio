def factorial(n):
    if n != 0: return n * factorial(n-1)
    return 1

userInput = input('put in your permutation or combination, nPr or nCr')
for letter in userInput:
    if letter == 'P':
        operation = 'permutation'
        n, r = int(userInput[:userInput.index('P')]), int(userInput[userInput.index('P')+1:])
        break
    if letter == 'C':
        operation = 'combination'
        n, r = int(userInput[:userInput.index('C')]), int(userInput[userInput.index('C')+1:])
        break

if n < r: print('n has to be larger than r')
print(n, operation, r, 'is')
if operation == 'permutation': print(factorial(n)/factorial(n-r))
if operation == 'combination': print(factorial(n)/(factorial(n-r)*factorial(r)))
