i=0
while i<3:
    i=i+1
    guess=int(input('Give Your Guess:'))
    if guess==24: 
        print('You Won!')
        break
    if guess<24:
        print('Low Value')
        print('try again')
    if guess>24:
        print('High Value')
        print('try again')
else:
    print('Attempts finished!')