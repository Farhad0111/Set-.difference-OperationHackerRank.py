class Farhad1:
    def __init__(self):
        self.i=int(input())
class Farhad2(Farhad1):
    def a(self):
        self.a=set(input().split())
class Farhad3(Farhad2):
    def j(self):
        self.j=int(input())
class Farhad4(Farhad3):
    def b(self):
        self.b=set(input().split())
class Farhad5(Farhad4):
    def faru(self):
        print(len(self.a.difference(self.b)))
farhad=Farhad5()
farhad.a()
farhad.j()
farhad.b()
farhad.faru()
