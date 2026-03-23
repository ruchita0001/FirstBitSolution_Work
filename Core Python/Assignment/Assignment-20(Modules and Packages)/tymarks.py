class TYMarks:

    def __init__(self, theory=0, practical=0):
        self.theory = theory
        self.practical = practical

    def accept(self):
        self.theory = int(input('Enter TY Theory Marks: '))
        self.practical = int(input('Enter TY Practical Marks: '))

    def total(self):
        return self.theory + self.practical
