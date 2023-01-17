'''COMPUTER QUIZ PROJECT'''

print('=====WELCOME TO MY COMPUTER QUIZ=====')

cont = 0
play = str(input('Do you wanna play? '))
if play.lower() == 'yes':
    print('Ok, Lets play!')

    answer = str(input('Who invented the lamp? '))
    if answer.lower() == 'thomas edison':
        print('THAT IS CORRECT!')
        cont += 1
    else:
        print('INCORRECT!')
    answer2 = str(input('What is the fastest animal on Earth? '))
    if answer2.lower() == 'cheetah':
        print('THAT IS CORRECT!')
        cont += 1
    else:
        print('INCORRECT!')
    answer3 = str(input('Who is the father of computer science? '))
    if answer3.lower() == 'alan turing':
        print('THAT IS CORRECT!')
        cont += 1
    else:
        print('INCORRECT!')
    print(f'Thank you for playing! You got {cont} points!')
elif play.lower() == 'no':
    print('Thank you for coming!')
    quit()
else:
    print('Invalid answer!')
