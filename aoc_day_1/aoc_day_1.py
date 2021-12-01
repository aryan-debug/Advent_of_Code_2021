import pathlib


def read_file() -> list[int]:
    with open(pathlib.Path(__file__).parent / "input.txt", "r") as file:
        lines = [int(line.strip()) for line in file.readlines()]
        return lines


def part_1(nums: list[int]) -> int:
    count_increased = 0
    for i, j in zip(nums, nums[1:]):
        if check_increased(i, j):
            count_increased += 1
    return count_increased


def part_2(nums: list[int]) -> int:
    count_increased = 0
    for i in range(len(nums)):
        increment_3 = nums[i : i + 3]
        next_nums = nums[i + 1 : i + 4]
        if len(increment_3) == len(next_nums) == 3 and check_increased(
            sum(increment_3), sum(next_nums)
        ):
            count_increased += 1
    return count_increased


def check_increased(num1: int, num2: int) -> bool:
    return num2 > num1


def main():
    numbers = read_file()
    print(f"Part 1: {part_1(numbers)}")
    print(f"Part 2: {part_2(numbers)}")


if __name__ == "__main__":
    main()
