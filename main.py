import sys, random

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"

quit = False
range = 100
while not quit:
    random_number = random.randint(1,range)
    count = 1
    number = -1
    while number != random_number:
        number  = input("Please Guess a Number between 1 and {}: ".format (range))
        if not number.isdigit():
            print('please guess a number')
        else:
            number = int(number)
            print('no, why did you think that?')
            if number > random_number:
                print('Too high dumbass')
            if number < random_number:
                print('Too low dipshit')
            count = count + 1

    print('woah, you actually got it')
    print('It only took you {} tries!'.format (count))
    play_again = input('\nWana try again? (yes or no)')
    play_again = play_again.lower()
    if play_again == 'yee' or play_again == 'yes':
        quit = False
    else:
        quit = True

print('\n\nThanks for playing')
