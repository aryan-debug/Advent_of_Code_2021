from pathlib import Path


def read_file():
    with open(Path(__file__).parent / "input.txt", "r") as file:
        school = [int(num) for num in file.readlines()[0].strip().split(",")]
        return school


def get_number_of_fishes(initial_timer: list[int], fishes: list[int]) -> list[int]:
    for i in initial_timer:
        fishes[i] = initial_timer.count(i)
    return fishes


def solution(initial_timer: list[int], days: int) -> int:
    fishes = [0] * 7
    babies = [0] * 2
    fishes = get_number_of_fishes(initial_timer, fishes)
    total_fishes = len(initial_timer)
    for i in range(days):
        total_fishes += fishes[0]
        first = fishes.pop(0)
        fishes.append(first)
        fishes[-1] += babies[0]
        last_baby = babies[-1]
        babies[0] = last_baby
        babies[-1] = first
    return total_fishes


def main():
    initial_timer = read_file()
    print(f"Part 1 solution: {solution(initial_timer, 80)}")
    print(f"Part 2 solution: {solution(initial_timer, 256)}")


main()
