from time import sleep
import sys
import os
os.system('clear')

#people = None
people={}
def menu():
    print('')
    print('* Vimart Database v.1 *')
    print(
        ' ---------------------------------------------------------------------------------------------------------------- ')
    print(
        '|                    |               |              |               |                 |                 |        |')
    print(
        '| 1.Display Database | 2.Find People | 3.Add People | 4.Change Data | 5.Save Database | 6.Load Database | 7.Exit |')
    print(
        '|                    |               |              |               |                 |                 |        |')
    print(
        ' ---------------------------------------------------------------------------------------------------------------- ')

    def menu_choice():
        try:
            option = int(input('What you wanna do?: '))
            while option not in range(1, 8):
                option = int(input('You need enter 1 - 7: '))
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
                    save_tofile()
                elif option == 6:
                    people = load_from_file()
                    return people
                elif option == 7:
                    sys.exit()

        except ValueError:
            print('You can choose only numbers.')
            menu_choice()

    people = menu_choice()
    return people


def load_from_file():
    global people

    def load_json():
        import json
        print('*Load from JSON File*')
        file_name = input('Input file name: ')
        while os.path.isfile(f'{file_name}.json') != True:
            print(f' File {file_name}.json is not in a Folder. Enter a correct file name.')
            file_name = input('Input file name: ')
        else:
            f = open(f'{file_name}.json', )
            people = json.load(f)
            f.close()

            return people

    def load_options():
        os.system('clear')
        print('* Vimart Database v.1 *')
        print('-----------------------------')
        print('* Load Database from a file *')
        print('-----------------------------')
        print(' You load from file type:')
        print('1. CSV File (.csv)')
        print('2. JSON File (.json)')
        print('3. TXT File (.txt)')
        print('4. Pickle file (.pkl)')
        print('5. Go back to Main Menu')
        try:
            load_from = int(input('You want to load from: '))

            while load_from not in range(1, 6):
                load_from = int(input('You need enter 1 - 5: '))
            else:
                if load_from == 1:
                    print('not jet')
                    load_csv()
                elif load_from == 2:
                    people = load_json()
                    return people
                elif load_from == 5:
                    menu()

        except ValueError:
            print('You can choose only numbers.')
            load_options()

    people = load_options()

    os.system('clear')
    print(f'Peoples data loaded: {people}')
    return people

def display_people():
    os.system('clear')
    print('* Vimart Database v.1 *')
    if len(people) == 0:
        print('No data to display.')
    else:

        for p_id in people:
            print('\n Person ID:', p_id)
            print('___________________')
            for key, value in people[p_id].items():
                print(key + ':', value)
        menu()


def changes():
    os.system('clear')
    print("Who\'s data do you want to change: ")

    for p_id in people:
        k = people[p_id]['name']
        print(f"{p_id} : {k}")
        print("-----------------")

    how_many = len(people) + 1

    def choice(how_many):
        while True:
            try:
                number = int(input("Choose the number "))
            except ValueError:
                pass
            else:
                if number in range(1, how_many):
                    return number

    number_change = choice(how_many)
    number_change = str(number_change)

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
    a = len(people[number_change].items())
    a = a+1

    def what_change(a):
        while True:
            try:
                number = int(input("Choose the number: "))
            except ValueError:
                pass
            else:
                if number in range(1, a):
                    return number

    what = what_change(a)

    what = keys[what]
    m = people[number_change]['name']
    change_to = input(f' You want to change {m}\'s {what} to?:  ').title()
    people[number_change][what] = change_to
    os.system('clear')
    print(f" Data for {people[number_change]['name']} is changed")
    print('--------------------------------------')

    print(f'\n Person_ID: {number_change}')
    print('-------------')
    for key, value in people[number_change].items():
                print(key + ':', value)

    menu()


def find_people():
    os.system('clear')
    print('------------------------------')
    print('*        Find People          *')
    print('------------------------------')
    city = input('Input city >> ').title()
    surname = input('surname >> ').title()
    name_p = input('name >> ').title()
    sex = input('sex >> ').title()
    age = input('age >> ').title()
    if any(record["name"] == name_p or record['city'] == city or record['sex'] == sex or record['age'] == age or record['surname']== surname for record in people.values()):
        for x in people:
            if people[x]['name'] == name_p and people[x]['city'] == city or people[x]['name'] == name_p or people[x]['city'] == city or people[x]['sex'] == sex\
                    or people[x]['city'] == city and people[x]['sex'] == sex and people[x]['age'] == age:
            #if people[x]['name'] == name_p and people[x]['city'] == city:
                print('\n Person_ID:', x)
                print('-------------')
                for key, value in people[x].items():
                    print(key+':', value)
            elif people[x]['sex']== sex and people[x]['city']== city:
            #if people[x]['name'] == name_p and people[x]['city'] == city:
                print('\n Person_ID:', x)
                print('-------------')
                for key, value in people[x].items():
                    print(key+':', value)
    else:
        print(f'Theres no person living in {city}')

    menu()


def add_people():
    os.system('clear')
    print('------------------------------')
    print('*Adding people to the Catalog*')
    print('------------------------------')
    name = input('Name: ').title()
    surname = input('Surname: ').title()

    def how_old():
        while True:
            ages = input('Age: ')
            if ages.isnumeric() is True:
                break
            print(' Try again. Your respond mus be numeric')
        return ages

    age = how_old()

    city = input('City: ').title()

    def p_sex():
        while True:
            sexs = input('Male/Female: ').title()
            if sexs in ['Male', 'Female']:
                break
            print(' Try again. Respond Male or Female')
        return sexs

    sex = p_sex()

    def marriage():
        while True:
            maritals = input('Married: Yes/No ?: ').title()
            if maritals in ['Yes', 'No']:
                break
            print('Try again. Respond Yes or No')
        return maritals
    marital = marriage()

    def phone_number():
        while True:
            phone_nos = input('Phone Number: ')
            if  phone_nos.isnumeric() is True:
                break
            print('Input phone number, must containing digits: ')
        return phone_nos

    phone_no = phone_number()

    ile = len(people)
    ile += 1
    ile = str(ile)

    people[ile] = {'name': name, 'age': age, 'surname': surname,  'city': city, 'sex': sex, 'married': marital, 'phoneNo': phone_no}

    os.system('clear')
    print(f" Data for {people[ile]['name']} in a database")
    print('--------------------------------------')

    print(f'\n Person_ID: {ile}')
    print('-------------')
    for key, value in people[ile].items():
                print(key + ':', value)

    menu()


def save_tofile():
    os.system('clear')
    print('--------------------------------------')
    print('* Save the Database of people to file*')
    print('--------------------------------------')

    def save_csv():
        import csv
        print('--------------------')
        print('* Save file to CSV *')
        print('--------------------')
        file_name = input('Input file name: ')
        w = csv.writer(open(file_name+".csv", "w"))
        for key, val in people.items():
            w.writerow([key, val])
        #menu()

    def save_json():
        print('---------------------')
        print('* Save file to JSON *')
        print('---------------------')
        print('')
        import json

        file_name = input('Input file name: ')
        json = json.dumps(people)
        f = open(file_name+".json", "w")
        f.write(json)
        f.close()
        #menu()

    def save_txt():
        print('--------------------')
        print('* Save file to TXT *')
        print('--------------------')

        file_name = input('Input file name: ')
        f = open(file_name+".txt", "w")
        f.write(str(people))
        f.close()
        #menu()

    def save_pkl():
        import pickle
        print('--------------------')
        print('* Save file to PKL *')
        print('--------------------')
        file_name = input('Input file name: ')
        f = open(file_name+".pkl", "wb")
        pickle.dump(dict, f)
        f.close()


    def save_options():
        print('--------------------')
        print('*     Save Menu      *')
        print('--------------------')
        print(' You want to save file to:')
        print('1. CSV File (.csv)')
        print('2. JSON File (.csv)')
        print('3. TXT File (.txt)')
        print('4. Pickle file (.pkl)')
        try:
            save_to = int(input('Save to: '))

            while save_to not in range(1, 5):
                save_to = int(input('You need enter 1 - 4: '))
            else:
                if save_to == 1:
                    save_csv()
                elif save_to == 2:
                    save_json()
                elif save_to == 3:
                    save_txt()
                elif save_to == 4:
                    save_pkl()

        except ValueError:
            print('You can choose only numbers.')
            save_options()

    save_options()

#people = load_from_file()
while True:
    menu()
