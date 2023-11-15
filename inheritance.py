class Animal:
    def speak(self):
        print("Animal speaking")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class DogChild(Dog):
    def eats(self):
        print("prining milk")

dog = Dog() #this is the object
dog.bark()
dog.speak()

domdogo= DogChild() #object2
dog.bark()
dog.speak()