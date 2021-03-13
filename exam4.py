menu = """ This is a list of popular birds.

0: Exit
1: Display the list of birds
2: Add a bird to the list

"""

birds = []


done = False

while not done:

    print(menu)

    selection = input('Please enter your selection: ')
    print()

    if selection == '0':
        print('')
        print('Good bye!')
        done = True
        
    elif selection == '1':
        print()
        print('{}'.format(birds))
        print()

    elif selection == '2':
            addBird = (input('Please add a bird to the list: '))
            birds.append(addBird)
    else:
        print()
        print('Invalid entry. Please enter a selection between 0 and 2')

