class A:
  def __init__(self):
    self.x=int(input())
    self.y=input()
    self.z=int(input())
  def method1(self,a,b):
    print(self.a[::-1])
    print(self.b**2)
  def display_result(self):
    print(self.x%self.z)
    print(len(self.y))
obj=A()
obj.method1('str',4)
obj.display_result()
