from pathlib import Path


def read_file():
    with open(Path(__file__).parent / "input.txt", "r") as file:
        crabs = [int(num) for num in file.readlines()[0].strip().split(",")]
        return crabs


def calculate_fuel(submarines: list[int], min_amount: int) -> int:
    total_fuel = 0
    for fuel in submarines:
        total_fuel += abs(fuel - min_amount)

    return total_fuel


def calculate_fuel_2(submarines: list[int], amount: int) -> int:
    total_fuel = 0
    for fuel in submarines:
        total_fuel += sum(range(abs(fuel - amount) + 1))
    return total_fuel


def get_average_shift(submarines: list[int]) -> int:
    return sum(submarines) // len(submarines)


def find_optimal_fuel(submarines: list[int], fuel_cost: int, amount: int) -> int:
    left = calculate_fuel(submarines, fuel_cost - 1)
    right = calculate_fuel(submarines, fuel_cost + 1)
    if left > amount < right:
        return amount
    if left < amount:
        return find_optimal_fuel(submarines, fuel_cost - 1, left)
    else:
        return find_optimal_fuel(submarines, fuel_cost + 1, right)


def find_optimal_fuel_2(submarines: list[int], fuel_cost: int, amount: int) -> int:
    left = calculate_fuel_2(submarines, fuel_cost - 1)
    right = calculate_fuel_2(submarines, fuel_cost + 1)
    if left > amount < right:
        return amount
    if left < amount:
        return find_optimal_fuel_2(submarines, fuel_cost - 1, left)
    else:
        return find_optimal_fuel_2(submarines, fuel_cost + 1, right)


def main():
    crabs = read_file()
    print(
        f"Part 1 solution: {find_optimal_fuel(crabs, (a := get_average_shift(crabs)), calculate_fuel(crabs, a))}"
    )
    print(
        f"Part 2 solution: {find_optimal_fuel_2(crabs, (a := get_average_shift(crabs)), calculate_fuel_2(crabs, a))}"
    )


main()
