def addEmp(emp):
    id=int(input("Enter Emp Id= "))
    if id in emp:
        print("Emp is Exist")
    else:
        name=input("Enter the Name= ")
        esal=float(input("Enter the Sal="))
        emp[id]={"eName":name,"sal":esal}
        print("Emp added successfully.....!!")
# AddEmp Ends Here

def displyEmp(emp):
    if not emp:
        print("Emp not found")
    else:
        print("\nID\t name \t sal")
        print("--------------------------------------")
        for id in emp:
            print(f'{id}\t{emp[id]["eName"]}\t{emp[id]["sal"]}')
            
#Display ends Here    

def delEmp(emp):
    id=int(input("Enter Emp Id= "))
    if id in emp:
        del emp[id]  
        print("Emp delted Successfully...........!")
    else:
        print("Emp is Exist")
        
#Delete Ends Here...........

def updateEmp(emp):
    id=int(input("Enter Emp Id= "))
    if id not in emp:
        print("Emp is not exit")
    else:
        while True:
            print("Enter 1 for edit name=")
            print("Enter 2 fo edit sal")
            print("Enter 3 for exit.....")
            num=int(input("Enter your choice="))
            if num==1:
                name=input("Enter new name=")
                emp[id]["eName"]=name
                print("Name Updated Successfully....!")
                return
            elif num==2:
                sal=input("Enter new sal")
                emp[id]["sal"]=sal
                print("Salay Updated Successfully....!")
                return
                
            elif num==3:
                break
            else:
                print("Invalid choice")
#update ends here.......

def searchEmp(emp):
    id=int(input("Enter Emp Id= "))
    if id not in emp:
        print("Emp is not exit")
    else:
        print("\nID\t name \t sal")  
        print("--------------------------------------")
        print(f'{id}\t{emp[id]["eName"]}\t{emp[id]["sal"]}')  
 #search ends here......

emp={1:{'eName':"Virat","sal":120000},
    2:{'eName':"Sachin","sal":123000}
    }

# addEmp(emp)
# displyEmp(emp)
# delEmp(emp)
# updateEmp(emp)
# displyEmp(emp)
# searchEmp(emp)
while True:
    print("\nEnter 1 for Add Emp")
    print("Enter 2 for display all emp")
    print("Enter 3 for update emp")
    print("Enter 4 for search emp")
    print("Enter 5 for delete emp")
    print("Enter 6 for exit.....")
    
    choice=int(input("Enter the choice="))
    if choice==1:
        addEmp(emp)
    elif choice==2:
        displyEmp(emp)
    elif choice==3:
        updateEmp(emp)
    elif choice==4:
        searchEmp(emp)
    elif choice==5:
        delEmp(emp)
    elif choice==6:
        print("Thank you....!!!") 
        break   
    else:
        print("Invalid choice")
