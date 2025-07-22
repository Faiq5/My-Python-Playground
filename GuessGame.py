i=0
print("""Welcome to the Number Guessing Game.
You have 5 attempts to Guess the Number.
Hint: The number is between 1 and 50.""")
import random
answer = random.randint(1, 50)
while i<5:
    i=i+1
    guess=int(input('Give Your Guess:'))
    if guess==answer: 
        print('You Won!')
        break
    if guess<answer:
        print('Low Value')
        print('try again')
    
    if guess>answer:
        print('High Value')
        print('try again')
    
else:
    print('Attempts finished!' \
    'The number was:', answer)
    print('Better luck next time!')
print('Thanks for playing!')
