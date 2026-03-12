from abc import ABC, abstractmethod

# --- ABSTRACTION & BASE CLASS ---
class Animal(ABC):
    def __init__(self, name, age, species):
        self._name = name      # Protected attribute (Encapsulation)
        self.__age = age       # Private attribute (Encapsulation)
        self.species = species

    # Getter for private age
    def get_age(self):
        return self.__age

    # Method to update age
    def update_age(self, new_age):
        if new_age > 0:
            self.__age = new_age

    @abstractmethod
    def speak(self):
        """Polymorphic method to be implemented by subclasses"""
        pass

    def display_info(self):
        print(f"Name: {self._name} | Age: {self.__age} | Species: {self.species}")

# --- INHERITANCE ---
class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age, "Dog")
        self.breed = breed

    # POLYMORPHISM: Overriding the speak method
    def speak(self):
        return "Woof! Woof!"

    def bark(self):
        print(f"{self._name} is barking loudly!")

class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age, "Cat")
        self.color = color

    # POLYMORPHISM: Overriding the speak method
    def speak(self):
        return "Meow! Meow!"

    def meow(self):
        print(f"{self._name} is meowing softly.")
class AnimalShelter(ABC):
    @abstractmethod
    def add_animal(self, animal):
        pass

    @abstractmethod
    def remove_animal(self, name):
        pass

class Shelter(AnimalShelter):
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"Successfully added {animal._name} to the shelter.")

    def remove_animal(self, name):
        for animal in self.animals:
            if animal._name.lower() == name.lower():
                self.animals.remove(animal)
                print(f"{name} has been adopted/removed.")
                return
        print(f"Animal named '{name}' not found.")

    def display_all(self):
        if not self.animals:
            print("\nThe shelter is currently empty.")
        else:
            print("\n--- Current Animals in Shelter ---")
            for animal in self.animals:
                animal.display_info()
                print(f"Sound: {animal.speak()}") # Demonstrating Polymorphism
def main():
    my_shelter = Shelter()
    
    while True:
        print("\n--- Animal Shelter Menu ---")
        print("1. Add a Dog")
        print("2. Add a Cat")
        print("3. Remove an Animal")
        print("4. Display All Animals")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            name = input("Enter Dog's name: ")
            age = int(input("Enter Dog's age: "))
            breed = input("Enter Dog's breed: ")
            my_shelter.add_animal(Dog(name, age, breed))

        elif choice == '2':
            name = input("Enter Cat's name: ")
            age = int(input("Enter Cat's age: "))
            color = input("Enter Cat's color: ")
            my_shelter.add_animal(Cat(name, age, color))

        elif choice == '3':
            name = input("Enter the name of the animal to remove: ")
            my_shelter.remove_animal(name)

        elif choice == '4':
            my_shelter.display_all()

        elif choice == '5':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()