print("""Welcome to "The Car Game
Lets Begin!
Give Command "Start" to start the Car
Give command "Stop" to stop the Car
Give Command "End" to Exit the game""")
command=''
started=False
while True:
    command=input('What is your order Commander:')
    command=command.lower()
    if command == 'start':
        if started:
            print('Car is already started')
        else:
            started=True
            print('Engine Started!')
    elif command == 'stop':
        if not started:
            print('Car is already Stopped')
        else:
            started=False
            print('Car Stopped(Engine Off)')
    elif command=='end':
        print('Thanks for Playing')
        break
    else:
        print('Give a suitable Command')