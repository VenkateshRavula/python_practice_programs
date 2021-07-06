'''
class Calculator(object):
  def add(self,a,b):
    sum = a + b
    print "I am in parent add function"
    return sum
  def sub(self,a,b):
    if a > b:
        diff = a - b
    else:
        diff = b - a
    print "I am in parent sub function"
    return diff
  def mul(self,a,b):
    print "I am in parent mul function"
    return a*b


class Maths(Calculator):
  def test1(self):
    s = self.add(1,5)  # calls method in parent class to child class
    print s
    print "i am in child"

m = Maths()
m.test1()
res = m.sub(4,10)  # calls method in parent class using child object
print res


#############


class Calculator(object):
  def __init__(self, vari="hello"):
    self.testvar = vari
    print "testvar in parent init function is %s" %self.testvar
  def add(self,a,b):
    sum = a + b
    print "I am in parent add function"
    self.testvar = "Parent - add modified"
    print "testvar in parent add function is %s" %self.testvar
    return sum
  def sub(self,a,b):
    if a > b:
        diff = a - b
    else:
        diff = b - a
    print "I am in parent sub function"
    print "testvar in parent sub function is %s" %self.testvar
    return diff
  def mul(self,a,b):
    print "I am in parent mul function"
    return a*b


class Maths(Calculator):
  def test1(self):
    s = self.add(1,5)  # calls method in parent class to child class
    print ">> i am in child"
    print ">> Child class test result is %d" %s

m = Maths()
m.test1()
subtract = m.sub(3,6)
print "Subtract result is %d" %subtract

'''

class Calculator(object):
  def __init__(self, vari="hello"):
    self.testvar = vari
    print "testvar in parent init function is %s" %self.testvar
  def add(self,a,b):
    sum = a + b
    print "I am in parent add function"
    self.testvar = "Parent - add modified"
    print "testvar in parent add function is %s" %self.testvar
    return sum
  def sub(self,a,b):
    if a > b:
        diff = a - b
    else:
        diff = b - a
    print "I am in parent sub function"
    print "testvar in parent sub function is %s" %self.testvar
    return diff
  def mul(self,a,b):
    print "I am in parent mul function"
    return a*b

class Maths(Calculator):
  def __init__(self, vari="children"):
    self.testvar = vari
    print "testvar in child init function is %s" %self.testvar
  def add(self,a,b):
    sum = a + b
    print "I am in child add function"
    self.testvar = "child-add modified"
    print "testvar in child add function is %s" %self.testvar
    return sum
  def parentAdd(self):
    s = Calculator.add(1,5)  # calls method in parent class to child class
    print ">> i am in child"
    print ">> Child class test result is %d" %s

m = Maths()
m.parentAdd()
subtract = m.add(3,6)
print "Subtract result is %d" %subtract
