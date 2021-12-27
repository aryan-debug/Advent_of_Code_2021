from pathlib import Path

total = 0


def read_file():
    with open(Path(__file__).parent / "input.txt", "r") as file:
        chunks = [[*map(int, line.strip())] for line in file.readlines()]
        return chunks


class Light:
    def __init__(self, value):
        self.value = value
        self.flashed = False

    def change_flashed(self):
        self.flashed = not self.flashed

    def reset(self):
        self.value = 0

    def __repr__(self) -> str:
        return f"Value: {self.value}"

    def flash(self, y, x, lights):
        self.reset()
        self.change_flashed()
        neighbours = get_neighbours(y, x)
        for row, col in neighbours:
            if not lights[row][col].flashed:
                lights[row][col].value += 1
        return lights


def get_neighbours(light_y, light_x):
    neighbours = []
    for delta_y, delta_x in [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),
        (-1, -1),
        (-1, 1),
        (1, -1),
        (1, 1),
    ]:
        offset_y = light_y + delta_y
        offset_x = light_x + delta_x
        if -1 < offset_y < 10 and -1 < offset_x < 10:
            neighbours.append((offset_y, offset_x))
    return neighbours


def add_one_to_lights(lights):
    for row in range(len(lights)):
        for col in range(len(lights[row])):
            lights[row][col].value += 1
    return lights


def predict_lights(lights, steps):
    global total
    for step in range(steps):
        lights = add_one_to_lights(lights)
        for row in range(len(lights)):
            for col in range(len(lights[row])):
                curr = lights[row][col]
                if curr.value >= 10:
                    total += 1
                    lights = curr.flash(row, col, lights)
                    flashed = flash_neighbours(row, col, lights)
                    if flashed:
                        lights = flashed
                    if check_synchronized_lights(lights):
                        return step + 1

        lights = change_all_flashed(lights)

    return total


def change_all_flashed(lights):
    for row in range(len(lights)):
        for col in range(len(lights[row])):
            lights[row][col].flashed = False
    return lights


def flash_neighbours(row, col, lights):
    global total
    neighbours = get_neighbours(row, col)
    can_flash = any([lights[n_row][n_col].value >= 10 for n_row, n_col in neighbours])
    if not can_flash:
        return lights
    for n_row, n_col in neighbours:
        if lights[n_row][n_col].value >= 10 and not lights[n_row][n_col].flashed:
            last_flashed_y, last_flashed_x = n_row, n_col
            total += 1
            lights = lights[n_row][n_col].flash(n_row, n_col, lights)
            flash_neighbours(last_flashed_y, last_flashed_x, lights)


def convert_to_lights(lights):
    new_lights = []
    for row in range(len(lights)):
        new_lights.append([])
        for col in range(len(lights[row])):
            new_lights[-1].append(Light(lights[row][col]))
    return new_lights


def check_synchronized_lights(lights):
    for row in range(len(lights)):
        for col in range(len(lights[row])):
            if lights[row][col].value != 0:
                return False
    return True


def part1():
    lights = read_file()
    lights = convert_to_lights(lights)
    print(f"Part 1 solution: {predict_lights(lights, 100)}")


def part2():
    lights = read_file()
    lights = convert_to_lights(lights)
    print(f"Part 2 solution: {predict_lights(lights, 400)}")


def main():
    part1()
    part2()


main()
