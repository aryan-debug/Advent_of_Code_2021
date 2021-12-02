import pathlib


def read_file() -> list[str, int]:
    with open(pathlib.Path(__file__).parent / "input.txt", "r") as file:
        return [((i:=line.strip().split())[0], int(i[1])) for line in file.readlines()]


def get_axis(instructions: list[str, int]) -> tuple[int, int]:
    x_axis: int; y_axis: int = 0, 0
    for direction, distance in instructions:
        match direction:
            case "forward":
                x_axis += distance
            case "up":
                y_axis -= distance
            case "down":
                y_axis += distance
    return x_axis, y_axis
        
def use_aim(instructions: list[str, int]) -> tuple[int, int]:
    x_axis: int; y_axis: int; aim:int = 0, 0, 0
    for direction, distance in instructions:
        match direction:
            case "forward":
                x_axis += distance
                y_axis += aim * distance
            case "up":
                aim -= distance
            case "down":
                aim += distance
    return x_axis, y_axis

def main():
    instructions:list[str, int] = read_file()
    x: int ;y: int = get_axis(instructions)
    new_x: int; new_y: int = use_aim(instructions)
    print(f"Part 1 solution: {x * y}")
    print(f"Part 2 solution: {new_x * new_y}")

main()
