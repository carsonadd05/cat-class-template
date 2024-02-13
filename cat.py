#Revmoe pass and complete the cat class
class Cat():
    def __init__(self):
        self.name = "unkown"
        self.age = 0 
    
    def speak(self):
        return "Meow"


stella = Cat
stella.name = "stella" 
stella.age = 7 
word2 = stella.speak 
print(word2)

garfield = Cat
garfield.name = "garfield"
garfield.age = 50
word = garfield.speak()
print(word)









#Create objects here
#These should NOT be indented inside the class

