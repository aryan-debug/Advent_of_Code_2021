import pathlib


def read_file() -> list[int]:
    with open(pathlib.Path(__file__).parent / "input.txt", "r") as file:
        lines = [line.strip().split() for line in file.readlines()]
        return lines


def get_axis(instructions):
    x_axis, y_axis = 0,0
    for direction, distance in instructions:
        distance = int(distance)
        match direction:
            case "forward":
                x_axis += distance
            case "up":
                y_axis -= distance
            case "down":
                y_axis += distance
    return x_axis, y_axis
        
def use_aim(instructions):
    x_axis, y_axis, aim = 0, 0, 0
    for direction, distance in instructions:
        distance = int(distance)
        match direction:
            case "forward":
                x_axis += distance
                y_axis += aim * distance
            case "up":
                aim -= distance
            case "down":
                aim += distance
        print(x_axis, y_axis, aim)
    return x_axis, y_axis

def main():
    instructions = read_file()
    x,y = get_axis(instructions)
    new_x, new_y = use_aim(instructions)
    print(f"Part 1 solution: {x * y}")
    print(f"Part 2 solution: {new_x * new_y}")

main()
