class Person :
  def __init__(self,fname,lname):
    self.fname = fname
    self.lname = lname

  def printn(self) :
    print(self.fname, self.lname)

class Student(Person) :
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduatinyear = year

x = Student('Joey', 'King', 2021)
x.printn
print(x.graduatinyear)