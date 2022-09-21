# Collect user info


# Add User
def add_user(users):
    name = input("Enter a new user name: ")
    while name in users:
        print("Sorry, that user name is already used.")
        name = input("Please enter another user name: ")

    print("Name details")
    first = input("Enter the first name: ")
    last = input("Enter the last name: ")

    print("Personal description")
    eyes = input("Enter the eye color: ")
    hair = input("Enter the hair color: ")

    print("Location")
    city = input("Enter the city name: ")
    state = input("Enter the state abbreviation: ")

    users.append(({'user': name,
                   'name': (first, last),
                   'eyes': eyes,
                   'hair': hair,
                   'location': (city, state)
                   }))




# Show user list
def show_user_list(users):
    print("User list")
    print('- - - - - -')
    for i in range(0, len(users)):
        print(users[i]['user'])


# Main body
user_list = list()
user_list.append(({'user': 'John23',
                   'name': ('John''', 'Logiudice'),
                   'eyes': 'brown',
                   'hair': 'brown',
                   'location': ('Wala Wala', 'WA')
                   }))

while True:
    # Main menu
    print("Main Menu")
    print("- - - - - - - -")
    print("1. Add a new user")
    print("2. Show user information")
    print("3. Quit")
    print()

    user_choice = input("Enter the number of your choice: ")
    print()

    if user_choice == '1':
        add_user(user_list)
        print()

    elif user_choice == '2':
        show_user_list(user_list)
        print()

    elif user_choice == '3':
        break
