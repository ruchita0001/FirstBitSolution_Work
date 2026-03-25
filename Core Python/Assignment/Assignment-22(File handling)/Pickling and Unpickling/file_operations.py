import pickle
import os
from emp import Emp
file_name = 'emp.dat'

# Add Record
def add_record():
    try:
        with open(file_name, 'ab') as f:
            e = Emp()
            e.accept()
            pickle.dump(e, f)
            print('Record added successfully')
    except Exception as e:
        print('Error while adding record:', e)

# Display All Records
def display_all():
    print('\n--- All Employee Records ---')
    try:
        with open(file_name, 'rb') as f:
            count = 0
            while True:
                try:
                    e = pickle.load(f)
                    e.display()
                    count += 1
                except EOFError:
                    break
            if count == 0:
                print('No records found')
    except FileNotFoundError:
        print('File not found')


# Search Record
def search_record():
    try:
        search_id = int(input('Enter ID to search: '))
        found = False

        with open(file_name, 'rb') as f:
            while True:
                try:
                    e = pickle.load(f)
                    if e.get_id() == search_id:
                        print('\n--- Record Found ---')
                        e.display()
                        found = True
                        break
                except EOFError:
                    break

        if not found:
            print('Record not found')

    except FileNotFoundError:
        print('File not found')


# Delete Record
def delete_record():
    try:
        delete_id = int(input('Enter ID to delete: '))
        found = False

        with open(file_name, 'rb') as f, open('temp.dat', 'wb') as temp:
            while True:
                try:
                    e = pickle.load(f)
                    if e.get_id() != delete_id:
                        pickle.dump(e, temp)
                    else:
                        found = True
                except EOFError:
                    break

        os.remove(file_name)
        os.rename('temp.dat', file_name)

        if found:
            print('✅ Record deleted successfully')
        else:
            print('❌ Record not found')

    except FileNotFoundError:
        print('File not found')


# Edit Record
def edit_record():
    try:
        edit_id = int(input('Enter ID to edit: '))
        found = False

        with open(file_name, 'rb') as f, open('temp.dat', 'wb') as temp:
            while True:
                try:
                    e = pickle.load(f)
                    if e.get_id() == edit_id:
                        print('\n--- Enter New Details ---')
                        e.accept()
                        found = True
                    pickle.dump(e, temp)
                except EOFError:
                    break

        os.remove(file_name)
        os.rename('temp.dat', file_name)

        if found:
            print('Record updated successfully')
        else:
            print('Record not found')

    except FileNotFoundError:
        print('File not found')
