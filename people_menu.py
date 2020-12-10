people = {1: {'name': 'John', 'age': '27', 'city': 'London', 'sex': 'Male', 'married': 'Yes', 'phoneNo':' 072374753'},
          2: {'name': 'Marie', 'age': '22', 'city': 'London', 'sex': 'Female', 'married' : 'No','phoneNo': '072374753'},
          3: {'name': 'Luna', 'age': '24', 'city': 'Edinburgh', 'sex': 'Female', 'married': 'No','phoneNo': '072374753'},
          4: {'name': 'Peter', 'age': '29', 'city': 'Edinburgh', 'sex': 'Male', 'married': 'Yes',
              'phoneNo':' 072374753'}}




def znajdz_people():
    miasto = input('Podaj miasto: ')
    if any(record["city"] == miasto for record in people.values()):
     for x in people:
        if people[x]['city'] == miasto:
            print('Person_ID:', x)
            print('-------------\n')
            for key, value in people[x].items():
                print(key+':', value)
    else:
        print(f'Theres no person living in {miasto}')
def add_people():
    Name = input('Name: ')
    Age = input('Age: ')
    City = input('City: ')
    Sex = ('Sex: ')
    Marrital = input(' Maried: Yes/No ?: ')
    PhoneNo = input('Phone Number: ')
    ile = len(people)
    ile += 1
   # people[ile]
    people[ile] = {'name': Name, 'age' : Age, 'city' : City, 'sex': Sex, 'married': Marrital, 'PhoneNo' : PhoneNo}
def display_people():
    for p_id, p_info in people.items():
        print("\nPerson ID:", p_id)

        for key in p_info:
            print(key + ':', p_info[key])

#def menu():
print('------------------------------------------')
print('1. Display People in Dictionary')
print('2. Find People')
print('3. Add People')
print('------------------------------------------')
option = input('What you wanna do?: ')
if option == 1:
    display_people()
elif option == 2:
    znajdz_people()
elif option == 3:
    add_people()



