
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
    if you want to add a new person please enter 3. \n"""))
        
    if service_input not in service_type:
        return "\nIncorrect value. This is not an option!"
    else:
        service = service_input

    return service


## Search by number function 
def SearchByNumber():

    try:
        number_input = int(input("Please enter phone number: "))
        if len(str(abs(number_input))) != 10:
            return '\nThis is invalid number' 
        else:
            if number_input not in tele_book:
                return "\nSorry, the number is not found!"
            else:
                number_owner = tele_book[number_input]
    except (KeyboardInterrupt, ValueError):
                return "\nIncorrect value. This is not an option!"
        
    return '\nThe owner of the number is: ', number_owner


## Search by name function 
def SearchByName():

    name_input = str(input("Please enter the name: "))
    for key, value in tele_book.items():
        if name_input == value:
            tele_number = key
    
    return '\nThis number belongs to: ', tele_number


## add new number function 
def addNew():

    while True:
        try:
            new_number = int(input('Enter Number: '))
            if new_number in tele_book:
                print("This number already exists")
            else:
                new_name = str(input('Enter Name: '))
                break
        except (KeyboardInterrupt, ValueError):
            return "Incorrect value. This is not an option!"

    tele_book[new_number] = new_name 
    return '\nName and number added successfully', new_number, new_name 


while True:
    Service = service()
    while True:
        if Service == 1:
            print(SearchByNumber())
            break
        elif Service == 2:
            print(SearchByName())
            break
        elif Service == 3:
            print(addNew())
            break

    restart = input('\nWould you like to restart? Enter yes or no.\n')
    if restart.lower() != 'yes':
        break