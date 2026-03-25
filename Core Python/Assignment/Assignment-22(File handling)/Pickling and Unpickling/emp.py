class Emp:

    def __init__(self, eid=0, ename='', basic=0.0):
        self.eid = eid
        self.ename = ename
        self.basic = basic

    def accept(self):
        print('\n--- Enter Employee Details ---')
        self.eid = int(input('Enter Employee ID: '))
        self.ename = input('Enter Employee Name: ')
        self.basic = float(input('Enter Basic Salary: '))

    def display(self):
        print(f'ID: {self.eid} | Name: {self.ename} | Salary: {self.basic}')

    def get_id(self):
        return self.eid

    def set_data(self, eid, ename, basic):
        self.eid = eid
        self.ename = ename
        self.basic = basic

    def __str__(self):
        return f'Emp({self.eid}, {self.ename}, {self.basic})'
