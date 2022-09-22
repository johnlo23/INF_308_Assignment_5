# Collect user info


# Add User
def add_user(users):
    # Get details about the new user to add
    name = input("Enter a new user name: ")

    # Check if user name already exists
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

    # Iterate through the list of users
    for i in range(0, len(users)):
        # Print line number and user name
        print(f"{i+1}. {users[i]['user']}")


# Find users
def find_user(users, name):
    # If user number was entered
    try:
        return int(name) - 1

    # If not an integer, assume a name was entered
    except ValueError:
        for i in range(0, len(users)):
            if users[i].get('user') == name:
                return i
    return None


# Show user details
def show_user_details(users, i):
    # Check that user index exists in the user list
    if i in range(0, len(users)):
        user = users[i].get('user')
        name = users[i].get('name')[1] + ", " + users[i].get('name')[0]
        eyes = users[i].get('eyes')
        hair = users[i].get('hair')
        location = users[i].get('location')[0]  + ", " + users[i].get('location')[1]

        print(f"User: {user}")
        print(f"Name: {name}")
        print(f"Eyes: {eyes}")
        print(f"Hair: {hair}")
        print(f"Location: {location}")
    else:
        print("Sorry, that user was not found")


# Main
# Initialize empty user list
user_list = list()
# Sample Data
sample_list = list()
sample_list.append(('John23', 'John', 'Logiudice', 'brown', 'brown', 'Wala Wala', 'WA'))
sample_list.append(('RollyPanda', 'Gandolph', 'Verspasian', 'hazel', 'blonde', 'Portland', 'OR'))
sample_list.append(('Jandra2001', 'Jandra', 'De La Cruz', 'green', 'brown', 'La Jolla', 'CA'))
# Fill list with sample data
for i in range(0, len(sample_list)):
    user_list.append(({'user': sample_list[i][0],
                       'name': (sample_list[i][1], sample_list[i][2]),
                       'eyes': sample_list[i][3],
                       'hair': sample_list[i][4],
                       'location': (sample_list[i][5], sample_list[i][6])
                       }))
del sample_list

# Loop for main menu
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

    # Add user
    if user_choice == '1':
        add_user(user_list)
        print()

    # Show user info
    elif user_choice == '2':
        show_user_list(user_list)
        show_user_details(user_list, find_user(user_list, input("Enter the user name or number: ")))
        print()

    # Quit
    elif user_choice == '3':
        print('Goodbye')
        break

    # Invalid entry
    else:
        print("Please enter a valid menu option.")
        print()
