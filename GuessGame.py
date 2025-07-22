i=0
print("Welcome to the Number Guessing Game.
You have 5 attempts to Guess the Number.
Hint: The number is between 1 and 50.")

while i<5:
    i=i+1
    guess=int(input('Give Your Guess:'))
    if guess==24: 
        print('You gave the right answer. You Won!')
        break
    if 14<guess<24:
        print('Low Value')
        print('try again')
    if guess<=14:
        print('Too Low Value')
        print('try again')
    if 34>guess>24:
        print('High Value')
        print('try again')
    if guess=>34:
        print('Too High Value')
        print('try again')
else:
    print('Attempts finished!')
