from tabulate import tabulate

# Dictionary for phone book with person name and number
tele_book = {
    1111111111 : 'Amal', 
    2222222222 : 'Mohammed', 
    3333333333 : 'Khadijah', 
    4444444444 : 'Abullah', 
    5555555555 : 'Rawan', 
    6666666666 : 'Faisal', 
    7777777777 : 'Layla' 
}

# Dictionary for types of service
service_type = { 1:"Search by number", 2:"Search by name", 3:"Add new person"}


def service():
    service_input = int(input(""" What service do you want?
    If you want to search by phone number please enter 1, 
    if you want to search by person name please enter 2, 
    if you want to add a new person please enter 3."""))
        
    if service_input not in service_type:
        print("Incorrect value. This is not an option!")
    else:
        service = service_input

    return service


## Search by number function 
def SearchByNumber():
    print('function 1 Search by number')

    number_input = int(input("Please enter phone number: "))
    if number_input not in tele_book:
        print("Incorrect value. This is not an option!")
    else:
        number_owner = tele_book[number_input]
        
    return number_owner

# print(SearchByNumber())


## Search by name function 
def SearchByName():
    print('function 2 Search by name')

    name_input = str(input("Please enter the name: "))
    for key, value in tele_book.items():
        if name_input == value:
            tele_number = key
    
    return tele_number


## add new number function 
def addNew():
    print('function 3 add new')
    while True:
        try:
            new_number = int(input('Enter Number: '))
            if new_number in tele_book:
                print("This number already exists")
            else:
                new_name = str(input('Enter Name: '))
                break
        except (KeyboardInterrupt, ValueError):
            print("Incorrect value. This is not an option!")

    tele_book[new_number] = new_name 
    return new_number, new_name 



while True:
    Service = service()
    while True:
        if Service == 1:
            print('The owner of the number is: ', SearchByNumber())
            break
        elif Service == 2:
            print('This number belongs to: ', SearchByName())
            break
        elif Service == 3:
            print('Name and number added successfully', addNew())
            break

    restart = input('\nWould you like to restart? Enter yes or no.\n')
    if restart.lower() != 'yes':
        break