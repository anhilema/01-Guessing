import sys, random

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"
cheese = False
quit = False
range = 100
while not quit:
    while cheese == False:
        potato = input('Please choose a difficulty (E) (M) (H) (I) ')
        if potato == 'e' or potato == 'E':
            range = 100
            cheese = True
        elif potato == 'm' or potato == 'M':
            range = 500
            cheese = True
        elif potato == 'h' or potato == 'H':
            range = 1000
            cheese = True
        elif potato == 'i' or potato == 'I':
            range = 1000000
            cheese = True
        else:
            cheese = False
            print ('Choose an option from the list')
    random_number = random.randint(1,range)
    count = 1
    number = -1
    while number != random_number:
        number  = input("\nPlease Guess a Number between 1 and {}: ".format (range))
        if not number.isdigit():
            print ("Guess a number please")
        else:
            number = int(number)
            print('No, why did you think that?')
            if number > random_number:
                print('Too high fool')
            if number < random_number:
                print('Too low fool')
            count = count + 1
    print('Woah, you actually got it')
    print('It only took you {} tries!'.format (count))
    play_again = input('\nWanna try again? (Y or N)')
    play_again = play_again.lower()
    if play_again == 'y':
        quit = False
    else:
        quit = True

print('\n\nThanks for playing')
