
#error: "Person" has no attribute "address"

# Person has no attribute address because address is not defined in the Person class. The class defines name, age, and preferred_operating_system, but not address. Therefore, mypy flags imran.address and eliza.address as errors.

class Person:
    def __init__(self, name: str, age: int, preferred_operating_system: str):
        self.name = name
        self.age = age
        self.preferred_operating_system = preferred_operating_system

imran = Person("Imran", 22, "Ubuntu")
print(imran.name)
print(imran.address)

eliza = Person("Eliza", 34, "Arch Linux")
print(eliza.name)
print(eliza.address)
