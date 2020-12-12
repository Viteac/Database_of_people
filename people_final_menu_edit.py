import sys

people = {1: {'name': 'John', 'surname': 'Mclachan', 'age': '27', 'city': 'London', 'sex': 'Male', 'married': 'Yes', 'phoneNo': '072374753'},
          2: {'name': 'Marie', 'surname': 'Rose', 'age': '22', 'city': 'London', 'sex': 'Female', 'married': 'No', 'phoneNo': '072374753'},
          3: {'name': 'Luna', 'surname': 'Stallone', 'age': '24', 'city': 'Edinburgh', 'sex': 'Female', 'married': 'No', 'phoneNo': '072374753'},
          4: {'name': 'Peter', 'surname': 'Griffin', 'age': '29', 'city': 'Edinburgh', 'sex': 'Male', 'married': 'Yes', 'phoneNo': '072374753'}}


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

    change_to = input(' You want to change it to?: ').title()

    people[number_change][what] = change_to

    print(f" Data for {people[number_change]['name']} is changed")
    for key, value in people[number_change].items():
        print(f' {key}:  {value}')


def find_people():
    city = input('Input city: ').title()
    name = input('name: ').title()

    if any(record["name"] == name for record in people.values()):
        for x in people:
            if people[x]['name'] == name and people[x]['city'] == city:
                print('\n Person_ID:', x)
                print('-------------')
                for key, value in people[x].items():
                    print(key+':', value)
    else:
        print(f'Theres no person living in {city}')


def add_people():
    name = input('Name: ').title()

    def how_old():
        ages = input('Your age: ')
        while not ages.isnumeric():
            print('Input must contain digits only')
            return how_old()
        return ages
    age = how_old()

    surname = input('Surname').title()
    city = input('City: ').title()

    def p_sex():
        sexs = input('Male/Female: ').title()
        while sexs != 'Male' and sexs != 'Female':
            print('Please answer Male or Female')
            return p_sex()
        return sexs

    sex = p_sex()

    def marriage():
        maritals = input('Married: Yes/No ?: ').title()
        while maritals != 'Yes' and maritals != 'No':
            return marriage()
        return maritals
    marital = marriage()

    def phone_number():
        phone_nos = input('Phone Number: ')
        while not phone_nos.isnumeric():
            phone_nos = input('Input phone number, must containg digits: ')
        return phone_nos

    phone_no = phone_number()

    ile = len(people)
    ile += 1

    people[ile] = {'Name': name, 'Surname': surname, 'Age': age, 'City': city, 'Sex': sex, 'Married': marital, 'Phone_No': phone_no}

    print(people)


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

    def menu_choice():
        try:
            option = int(input('What you wanna do?: '))
            while option not in range(1, 6):
                option = int(input('You need enter 1 - 5: '))
            else:
                if option == 1:
                    display_people()
                elif option == 2:
                    find_people()
                elif option == 3:
                    add_people()
                elif option == 4:
                    changes()
                elif option == 5:
                    sys.exit()

        except ValueError:
            print('You can choose only numbers.')
            menu_choice()

    menu_choice()


while True:
    menu()
