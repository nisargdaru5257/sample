def integer(x):
    int_number = int(x)
    return int_number

def show(x,y):
    print(f"Your preferred choice of language is \"{x}\" and your favourite tv-show is \"{y}\".")

def sub(x,y):
    print("Your choice language is {} and your favourite show is {}.".format(x,y))

print("""Select your preferred language of choice for Tv-shows
1. English
2. Hindi""")

lang = input('> ')

if lang == '1' or lang == '2':
    if lang == '1':
        language = "English"
        print(f"You have choosen {language} as your preferred language.")
        print("""Choose your favourite tv show from the list below:
        1. Game of thrones
        2. Person of Interest
        3. Westworld""")
        #choice = input('> ')
        choice = input('> ')
        x,y,z = "Game of Thrones", "Person of Interest", "Westworld"
        if choice == '1':
            show(language, x)
        elif choice == '2':
            show(language, y)
        elif choice == '3':
            show(language, z)
        else:
            print("Please try again!")

    else:
        language = "Hindi"
        print(f"You have choosen {language} as your preferred language.")
        print("""Choose your favourite tv show from the list below:
        1. Taarak Mehta ka ooltah chasma
        2. Tenali Rama
        3. Aladdin""")
        choice = input('> ')
        #choice = integer(choice)
        x,y,z = "Taarak Mehta ka ooltah chasma", "Tenali Rama", "Aladdin"
        if choice == '1':
            show(language, x)
        elif choice == '2':
            show(language, y)
        elif choice == '3':
            show(language, z)
        else:
            print("Please try again!")
    
else:
    print("Please make your selection from number \"1\" or \"2\".")
