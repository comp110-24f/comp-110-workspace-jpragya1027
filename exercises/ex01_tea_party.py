"""This program calculates the tea, treats, and cost required for a tea party using the number of guests."""

__author__: str = "730748160"


def main_planner(guests: int) -> None:
    """This function calls the tea_bags, treats, and cost functions and prints all the information for the party."""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(guests)))
    print("Treats: " + str(treats(guests)))
    print("Cost: $" + str(cost(tea_bags(guests), treats(guests))))


def tea_bags(people: int) -> int:
    """This function returns the number of tea bags required for the party."""
    return people * 2


def treats(people: int) -> int:
    """This function returns the number of treats required for the party."""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """This function returns the cost for the party."""
    return tea_count * 0.50 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
