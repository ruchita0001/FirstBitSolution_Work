class Distance:

    #Constructor
    def __init__(self, km=0, m=0, cm=0):
        self.km = km
        self.m = m
        self.cm = cm

    #Destructor
    def __del__(self):
        print('Object destroyed')

    #Normalize function (important 🔥)
    def normalize(self):
        self.m += self.cm // 100
        self.cm = self.cm % 100

        self.km += self.m // 1000
        self.m = self.m % 1000

    #Overload + Operator
    def __add__(self, other):
        d = Distance(
            self.km + other.km,
            self.m + other.m,
            self.cm + other.cm
        )
        d.normalize()
        return d

    #Overload - Operator
    def __sub__(self, other):
        total1 = self.km * 100000 + self.m * 100 + self.cm
        total2 = other.km * 100000 + other.m * 100 + other.cm

        diff = total1 - total2

        km = diff // 100000
        diff %= 100000

        m = diff // 100
        cm = diff % 100

        return Distance(km, m, cm)

    #Display
    def display(self):
        print(f'{self.km} km {self.m} m {self.cm} cm')
