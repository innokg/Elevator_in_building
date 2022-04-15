"""Main function"""
import random

from elevator import Building


def main():
    """main function"""
    global passengers
    floors = random.randint(5, 20)
    print("Случайный максимальный этаж:", floors)
    for i in range(1, floors + 1):
        passengers = i * random.randint(1, 10)


    Building(floors, passengers)


if __name__ == "__main__":
    main()

