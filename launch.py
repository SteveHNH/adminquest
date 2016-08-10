'''
Adminquest
==========
This is a basic framework for how adminquest is going to work. I have mostly no
idea what I'm doing yet, but I'm kind of excited about the possibilities.
'''

from __future__ import print_function
from questBoard import availableQuests
from characterFunctions import inventory, character, availableRaces, availableClasses
from functions import printQuests, pressEnter, speech, modGold, displaySheet, clearScreen, mainTitle

mainTitle()

print('1. Begin Quest')
print('')
print('Choice: ', end='')
choice = raw_input()

print('What is your name, Adventurer? ')
character['NAME'] = raw_input()

speech('''
It is so good to see you, ''' + character['NAME'] + '!' + '''
My vision is poor, my friend. It has been a long time since an adventurer
such as yourself has made their way to this place.''')

pressEnter()
clearScreen()
speech('''
Tell me, ''' + character['NAME'] + ', of what race are you?')
while character['RACE'] == '':
    print
    print('Choose a Race:')
    for race in availableRaces:
        print(race.title())
    print('')
    print('Race Choice: ', end='')
    character['RACE'] = raw_input().lower()
    if character['RACE'] not in availableRaces:
        print('')
        print('Please choose a valid race')
        character['RACE'] = ''
    else:
        continue

print('')
if character['RACE'] == 'Elf':
    print('Oh, so you\'re an ' + str.lower(character['RACE']) +
          ', eh? Excellent')
else:
    print('Oh, so you\'re a ' + str.lower(character['RACE']) +
          ', eh? Excellent')
print('')

pressEnter()
clearScreen()
speech('''You clearly have seen a bit of the world. What would you say you specialize
in, friend? What is your profession?''')

while character['CLASS'] == '':
    print('Choose a Class')
    for classes in availableClasses:
        print(classes.title())
    print('')
    print('Class Choice: ')
    character['CLASS'] = raw_input().lower()
    if character['CLASS'] not in availableClasses:
        print('')
        print('Please choose a valid class')
        character['CLASS'] = ''
    else:
        continue

speech('Fantastic! We need more ' + str.lower(character['CLASS']) +
      's in the world')

pressEnter()
clearScreen()

speech('Well, ' + character['NAME'] + ', we have a lot of work to do.')
speech('''
The system is broken, friend. We need a system administrator to help bring
it back. But first, you'll need some training. Here I have a list of "quests"
that you can undertake to hone your skills. Choose them wisely, and good
luck!''')

modGold(50)
speech('Oh! By the way, here\'s ' + str(inventory['Gold']) +
      ' gold to get you started')

pressEnter()
clearScreen()
speech('Makes sure I got all your details correct')
displaySheet()

# Changing stuff is currently broken. Something up with the while loop
speech('Would you like to change anything? (y/n)')
sheetChange = raw_input().lower()
if sheetChange == 'y':
    while sheetChange == 'y':
        speech('What would you like to change?')
        print('Name, Class, or Race: ', end='')
        choice = raw_input().lower
        if choice == 'name':
            speech('What would you like to change your name to?')
            character['NAME'] = ''
            while character['NAME'] == '':
                newName = raw_input().lower
                character['NAME'] = newName
            speech('Name changed to ' + character['Name'])
            print('Would you like to change anything else? (y/n)', end='')
            answer = raw_input().lower()
            if answer == 'n':
                sheetChange = 'n'
        elif choice == 'class':
            speech('What would you like to change your class to?')
            character['CLASS'] = ''
            while character['CLASS'] == '':
                newClass = raw_input().lower
                character['CLASS'] = newClass
                if character['CLASS'] not in availableClasses:
                    print('Not a valid class')
                    print('Choose one of the following')
                    for classes in availableClasses:
                        print(classes.title())
                    character['CLASS'] = ''
            print('Would you like to change anything else? (y/n)', end='')
            answer = raw_input().lower()
            if answer == 'n':
                sheetChange = 'n'
        elif choice == 'race':
            speech('What would you like to change your class to?')
            character['RACE'] = ''
            while character['RACE'] == '':
                newRace = raw_input().lower
                character['RACE'] = newRace
                if character['RACE'] not in availableRaces:
                    print('Not a valid class')
                    print('Choose one of the following')
                    for race in availableRaces:
                        print(race.title())
                    character['RACE'] = ''
            print('Would you like to change anything else? (y/n)', end='')
            answer = raw_input().lower()
            if answer == 'n':
                sheetChange = 'n'
        else:
            print('If you want to change something, do it.')


speech('One more thing, ' +character['NAME'] + '.')
pressEnter()
speech('It\'s dangerous to go alone. Take this!')
inventory['Mainhand'] = 'Wooden Stick'
speech('Received: ' + inventory['Mainhand'])
pressEnter()
clearScreen()


printQuests()
