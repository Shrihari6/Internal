class student:
    def getstu(self):
        self.rollno = input("Enter the roll number of student: ")
        self.name = input("Enter the name of student: ")
        self.physics = int(input("Enter the marks of physics: "))
        self.chemistry = int(input("Enter the marks of chemistry: "))
        self.maths = int(input("Enter the marks of maths:"))
    def printresult(self):
        self.result = (float)((self.physics + self.chemistry + self.maths )/ 300 * 100)
        print(self.rollno,'\t',self.name,'\t',self.result)

import time 
import sys
st = time.time()
s1 = student()
s1.getstu()
print('RESULT: ')
print('Roll num\t name \t result')
s1.printresult()
et = time.time()
el = et - st

sproll = sys.getsizeof(s1.rollno)
spname = sys.getsizeof(s1.name)
spphy = sys.getsizeof(s1.physics)
spchem = sys.getsizeof(s1.chemistry)
space = sproll + spname + spphy + spchem
print('Total space: ',space)
