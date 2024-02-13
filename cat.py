#Revmoe pass and complete the cat class
class Cat():
    def __init__(self):
        self.name = "unkown"
        self.age = 0 
    def speak(self):
        return "Meow"

#Create objects here
#These should NOT be indented inside the class

stella = Cat()
stella.name = "stella" 
stella.age = 7 

garfield = Cat()
garfield.name = "garfield"
garfield.age = 50
#garfield.speak()