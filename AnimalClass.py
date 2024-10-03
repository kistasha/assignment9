# Task 1: creating the Animal class
class Animal:
    # class constructor
    def __init__(self,genus,name,year_of_birth,fav_fruit):
        # attributes
        self.genus = genus
        self.name = name
        self.year_of_birth = year_of_birth
        self.fav_fruit = fav_fruit
    # defining the get_age method
    def get_age(self, year):
        return (year-self.year_of_birth)
    # defining the get_info method
    def get_info(self):
        if self.genus=="elephant":
            return f'{self.name} is an {self.genus}'
        else:
            return f'{self.name} is a {self.genus}'
    
# Task 2: creating the list of different animals
animals = [Animal("fox","Alex",2005,"kiwi"),
           Animal("dog","Balto",1990,"banana"),
           Animal("python","Kaa",2000,"watermelon"),
           Animal("elephant","Dumbo",2010,"apple")]

# running the methods for each animal using the for loop
for animal in animals:
    print(animal.get_info())
    print(f'{animal.name} is {animal.get_age(2024)} years old')
    print()


# Task 3: creating the method to find the oldest animal
def oldest_animal(animal_list):
    oldest = min(animal_list, key=lambda x: x.year_of_birth)
    return oldest

# using the oldestAnimal method to print out name, genus & age of the oldest animal from the list above
oldie = oldest_animal(animals)
print()
print(f'The oldest animal in the list:\nName: {oldie.name}\nGenus: {oldie.genus}\nAge: {oldie.get_age(2024)}')
print()

# Task 4: writing name and genus to a text file
my_file = "animals.txt"

file = open(my_file,'w')
for animal in animals:
    file.write(f'{animal.name},{animal.genus}\n')
file.close()

# now, reading from the file to check the content right away
file = open(my_file,'r')
content=file.read()
print("Text file contents:")
print(content)
file.close()


