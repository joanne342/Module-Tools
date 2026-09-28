from datetime import date

class Person:
    def __init__(
        self,
        name: str,
        date_of_birth: date,
        preferred_operating_system: str,
    ):
        self.name = name
        self.date_of_birth = date_of_birth
        self.preferred_operating_system = preferred_operating_system

    def age(self) -> int:
        today = date.today()

        age = today.year - self.date_of_birth.year

        # If their birthday hasn't happened yet this year,
        # they are one year younger.
        if (today.month, today.day) < (
            self.date_of_birth.month,
            self.date_of_birth.day,
        ):
            age -= 1

        return age

    def is_adult(self) -> bool:
        return self.age() >= 18


imran = Person("Imran", date(2004, 4, 18), "Ubuntu")

print(imran.is_adult())
