from dataclasses import dataclass
from enum import Enum


class OperatingSystem(Enum):
    MACOS = "macOS"
    ARCH = "Arch Linux"
    UBUNTU = "Ubuntu"


@dataclass(frozen=True)
class Person:
    name: str
    age: int
    preferred_operating_system: OperatingSystem


@dataclass(frozen=True)
class Laptop:
    id: int
    manufacturer: str
    model: str
    screen_size_in_inches: float
    operating_system: OperatingSystem


laptops = [
    Laptop(
        id=1,
        manufacturer="Dell",
        model="XPS",
        screen_size_in_inches=13,
        operating_system=OperatingSystem.ARCH,
    ),
    Laptop(
        id=2,
        manufacturer="Dell",
        model="XPS",
        screen_size_in_inches=15,
        operating_system=OperatingSystem.UBUNTU,
    ),
    Laptop(
        id=3,
        manufacturer="Dell",
        model="XPS",
        screen_size_in_inches=15,
        operating_system=OperatingSystem.UBUNTU,
    ),
    Laptop(
        id=4,
        manufacturer="Apple",
        model="MacBook",
        screen_size_in_inches=13,
        operating_system=OperatingSystem.MACOS,
    ),
]


def read_name() -> str:
    while True:
        name = input("What is your name? ").strip()

        if name and name.isalpha():
            return name

        print("Please enter a valid name using letters only.")


def read_age() -> int:
    while True:
        try:
            age = int(input("What is your age? "))

            if age >= 18:
                return age

            print("You must be 18 or older.")

        except ValueError:
            print("Please enter a valid number.")


def read_operating_system() -> OperatingSystem:
    print("\nAvailable operating systems:")

    operating_systems = list(OperatingSystem)

    for number, operating_system in enumerate(operating_systems, start=1):
        print(f"{number}. {operating_system.value}")

    while True:
        try:
            choice = int(input("Choose an operating system [1-3]: "))

            if 1 <= choice <= len(operating_systems):
                return operating_systems[choice - 1]

            print("Please choose a number from 1 to 3.")

        except ValueError:
            print("Please enter a valid number.")


def find_matching_laptops(
    laptops: list[Laptop],
    person: Person,
) -> list[Laptop]:
    return [
        laptop
        for laptop in laptops
        if laptop.operating_system == person.preferred_operating_system
    ]


def count_laptops_by_operating_system(
    laptops: list[Laptop],
) -> dict[OperatingSystem, int]:
    counts = {
        operating_system: 0
        for operating_system in OperatingSystem
    }

    for laptop in laptops:
        counts[laptop.operating_system] += 1

    return counts


def most_available_operating_system(
    counts: dict[OperatingSystem, int],
) -> OperatingSystem | None:
    if not counts:
        return None

    return max(counts, key=counts.get)


def choose_operating_system(
    person: Person,
    counts: dict[OperatingSystem, int],
) -> OperatingSystem | None:
    preferred_os = person.preferred_operating_system
    preferred_count = counts[preferred_os]

    most_available_os = most_available_operating_system(counts)

    if most_available_os is None:
        return None

    if (
        most_available_os != preferred_os
        and counts[most_available_os] > preferred_count
    ):
        print(
            f"We have {preferred_count} laptop(s) with "
            f"{preferred_os.value}."
        )

        print(
            f"We have {counts[most_available_os]} laptop(s) with "
            f"{most_available_os.value}."
        )

        while True:
            answer = input(
                f"Would you accept {most_available_os.value} instead? Y/N: "
            ).strip().lower()

            if answer == "y":
                return most_available_os

            if answer == "n":
                return preferred_os

            print("Please enter Y or N.")

    return preferred_os


def rent_laptop(
    laptops: list[Laptop],
    operating_system: OperatingSystem,
) -> Laptop | None:
    for index, laptop in enumerate(laptops):
        if laptop.operating_system == operating_system:
            return laptops.pop(index)

    return None


def main() -> None:
    print("Welcome to the CYF laptop library!\n")

    name = read_name()
    age = read_age()
    preferred_operating_system = read_operating_system()

    person = Person(
        name=name,
        age=age,
        preferred_operating_system=preferred_operating_system,
    )

    matching_laptops = find_matching_laptops(laptops, person)

    print(
        f"\nWe have {len(matching_laptops)} laptop(s) with "
        f"your preferred operating system, "
        f"{person.preferred_operating_system.value}."
    )

    counts = count_laptops_by_operating_system(laptops)

    chosen_operating_system = choose_operating_system(
        person,
        counts,
    )

    if chosen_operating_system is None:
        print("Sorry, no laptops are available.")
        return

    rented_laptop = rent_laptop(
        laptops,
        chosen_operating_system,
    )

    if rented_laptop is None:
        print(
            f"Sorry, there are no {chosen_operating_system.value} "
            "laptops available."
        )
        return

    print(
        f"\nCongratulations {person.name}!"
        f"\nYou have rented a {rented_laptop.manufacturer} "
        f"{rented_laptop.model} "
        f"({rented_laptop.screen_size_in_inches}\"), "
        f"running {rented_laptop.operating_system.value}."
    )


if __name__ == "__main__":
    main()
