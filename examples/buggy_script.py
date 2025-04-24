import os,sys

def  add_numbers( a,b ):
  result=a+b
  print("result is",result)
  return result

def divide(a, b):
    if b == 0:
        print("division by zero")
        return
    return a / b

def greet(name):
    print("Hello " + name + "!")


class Person:
  def __init__(self,name,age):
      self.name=name
      self.age=age
  
  def greet(self):
      print("Hi, my name is",self.name,"and I'm",self.age,"years old")

x = add_numbers(4,5)
y = divide(10,0)
g = greet("Alice")
p = Person("Bob", "twenty five")
p.greet()