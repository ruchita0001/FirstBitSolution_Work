from file_operations import *

def menu():
    print('\n========== Employee Management System ==========')
    print('1. Add Record')
    print('2. Display All Records')
    print('3. Search Record')
    print('4. Delete Record')
    print('5. Edit Record')
    print('6. Exit')


while True:
    menu()
    try:
        choice = int(input('Enter your choice: '))

        if choice == 1:
            add_record()

        elif choice == 2:
            display_all()

        elif choice == 3:
            search_record()

        elif choice == 4:
            delete_record()

        elif choice == 5:
            edit_record()

        elif choice == 6:
            print('Exiting program...')
            break

        else:
            print('Invalid choice. Try again.')

    except ValueError:
        print('Please enter a valid number')
