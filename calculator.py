def calculator(user_intent,num1,num2):
    if user_intent.lower() == 'sum':
        solution = num1 + num2
        return solution
    elif user_intent.lower() == 'substract':
        solution = num1 - num2
        return solution
    elif user_intent.lower() == 'multiply':
        solution = num1 * num2
        return solution
    elif user_intent.lower() == 'division':
        if num2 == 0:
            print("Error: no number can be divided by zero")
        solution = num1/num2
        return solution
    else:
        print('Please write a suitable operation')
        exit()
solution=""
print('Hi! I am your calculator today...:)')
user_intent = input('What do you want me to do?' \
'Write either sum, substract, multiply or division')
num1 = float(input('Write your first number'))
num2 = float(input('Write your second Number'))
solution = calculator(user_intent,num1,num2)
print (num1,user_intent,num2)
print('Your Answer is', solution)
