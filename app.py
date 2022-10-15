car_input = input(">")
car_started = False
while car_input != 'quit':
    if car_input == 'start':
        print("Car started")
        car_started = True
    elif car_input == 'stop':
        if car_started:
            print("Car stopped")
        else:
            print("Car has not started yet")
    else:
        print("Please enter valid input")
    car_input = input(">")








