class Parent:
    """Store a person's first and last name."""

    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    def get_name(self) -> str:
        """Return the person's current first and last name."""
        return f"{self.first_name} {self.last_name}"


class Child(Parent):
    """A Parent with the ability to change and remember previous surnames."""

    def __init__(self, first_name: str, last_name: str):
        # Initialise first_name and last_name using the Parent constructor.
        super().__init__(first_name, last_name)

        # Keep track of previous surnames.
        self.previous_last_names = []

    def change_last_name(self, last_name: str) -> None:
        """Change the surname and remember the previous surname."""
        self.previous_last_names.append(self.last_name)
        self.last_name = last_name

    def get_full_name(self) -> str:
        """
        Return the current full name and, if applicable,
        the original surname as a née name.
        """
        suffix = ""

        if self.previous_last_names:
            suffix = f" (née {self.previous_last_names[0]})"

        return f"{self.first_name} {self.last_name}{suffix}"


# Create a Child object.
person1 = Child("Elizaveta", "Alekseeva")

# Child inherits get_name() from Parent.
print(person1.get_name())
# Elizaveta Alekseeva

# Child has its own get_full_name() method.
print(person1.get_full_name())
# Elizaveta Alekseeva

# Change the child's surname.
person1.change_last_name("Tyurina")

# get_name() now returns the new surname.
print(person1.get_name())
# Elizaveta Tyurina

# get_full_name() includes the original surname.
print(person1.get_full_name())
# Elizaveta Tyurina (née Alekseeva)


# Create a Parent object.
person2 = Parent("Elizaveta", "Alekseeva")

# Parent has get_name().
print(person2.get_name())
# Elizaveta Alekseeva

# Parent does not have get_full_name() or change_last_name().
# These calls are intentionally NOT made because they would
# raise AttributeError.

