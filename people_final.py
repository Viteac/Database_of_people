import sys

people = {1: {'name': 'John', 'age': '27', 'city': 'London', 'sex': 'Male', 'married': 'Yes', 'phoneNo': '072374753'},
          2: {'name': 'Marie', 'age': '22', 'city': 'London', 'sex': 'Female', 'married': 'No', 'phoneNo': '072374753'},
          3: {'name': 'Luna', 'age': '24', 'city': 'Edinburgh', 'sex': 'Female', 'married': 'No', 'phoneNo': '072374753'},
          4: {'name': 'Peter', 'age': '29', 'city': 'Edinburgh', 'sex': 'Male', 'married': 'Yes', 'phoneNo': '072374753'}}


def changes():
    print("Who\'s data do you want to change: ")
    for p_id in people:
        print(f"{p_id} : {people[p_id]['name']}")
        print("-----------------")
    number_change = input("Change: ")
    number_change = int(number_change)
    for key, value in people[number_change].items():
        print(f' {key}:  {value}')
        print("-----------------")
    keys = {}
    for number, y in enumerate(people[number_change].keys(), 1):
        keys[number] = y

    print('What do You want to change? ')
    for i in keys:
        print(f' {i}: {keys[i]}')
        print("-----------------")
    what = input(': ')
    what = int(what)
    what = keys[what]

    change_to = input(' You want to change it for?: ')

    people[number_change][what] = change_to

    print(f" Data for {people[number_change]['name']} is changed")
    for key, value in people[number_change].items():
        print(f' {key}:  {value}')


def find_people():
    city = input('Input city: ')
    name = input('name: ')

    if any(record["name"]  ==  name for record in people.values()):
        for x in people:
            if people[x]['city'] == city and people[x]['name'] == name:
                print('\n Person_ID:', x)
                print('-------------')
                for key, value in people[x].items():
                    print(key+':', value)
    else:
        print(f'Theres no person living in {city}')


def add_people():
    name = input('Name: ')
    age = input('Age: ')
    city = input('City: ')
    sex = input('Sex: ')
    marital = input(' Married: Yes/No ?: ')
    phoneno = input('Phone Number: ')
    ile = len(people)
    ile += 1

    people[ile] = {'Name': name, 'Age': age, 'City': city, 'Sex': sex, 'Married': marital, 'PhoneNo': phoneno}


def display_people():
    for p_id in people:
        print('\n Person ID:', p_id)
        print('__________________')
        for key, value in people[p_id].items():
            print(key + ':', value)


def menu():
    print('------------------------------------------')
    print('1. Display People in Dictionary')
    print('2. Find People')
    print('3. Add People')
    print('4. Change People\'s data')
    print('5. Quit')
    print('------------------------------------------')
    option = input('What you wanna do?: ')
    if option == '1':
        display_people()
    elif option == '2':
        find_people()
    elif option == '3':
        add_people()
    elif option == '4':
        changes()
    elif option == '5':
        sys.exit()


while True:
    menu()

