from pathlib import Path


def read_file():
    with open(Path(__file__).parent / "input.txt", "r") as file:
        return [line.strip().split(" -> ") for line in file.readlines()]


def make_ocean_floor(rows: int, cols: int) -> list[list[int]]:
    return [[0 for j in range(cols)] for i in range(rows)]


def check_horizontal(y1: int, y2: int) -> bool:
    return y1 == y2


def check_vertical(x1: int, x2: int) -> bool:
    return x1 == x2


def arrange_coords(coord1: str, coord2: str) -> tuple[int, int, int, int]:
    if int("".join(coord1.split(","))) > int("".join(coord2.split(","))):
        return (
            int((c := coord2.split(","))[0]),
            int(c[1]),
            int((c := coord1.split(","))[0]),
            int(c[1]),
        )
    return (
        int((c := coord1.split(","))[0]),
        int(c[1]),
        int((c := coord2.split(","))[0]),
        int(c[1]),
    )


def check_upward_slope(x1: int, y1: int, x2: int, y2: int) -> bool:
    return x1 > x2 and y1 < y2


def find_dangerous_areas(coords: list[list[str, str]], part2: bool = False) -> int:
    floor = make_ocean_floor(1000, 1000)
    dangerous_areas = 0
    for coord in coords:
        x1, y1, x2, y2 = arrange_coords(coord[0], coord[1])
        if check_horizontal(y1, y2):
            for i in range(abs(x1 - x2) + 1):
                floor[y1][x1 + i] += 1
        elif check_vertical(x1, x2):
            for i in range(abs(y1 - y2) + 1):
                floor[y1 + i][x1] += 1
        elif part2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
            if check_upward_slope(x1, y1, x2, y2):
                i = 0
                while True:
                    floor[y1 + i][x1 - i] += 1
                    if (y1 + i, x1 - i) == (y2, x2):
                        break
                    i += 1
            else:
                if x1 < x2:
                    j = 0
                    while True:
                        floor[y2 + j][x2 - j] += 1
                        if (y2 + j, x2 - j) == (y1, x1):
                            break
                        j += 1
                else:
                    j = 0
                    while True:
                        floor[y2 + j][x2 + j] += 1
                        if (y2 + j, x2 + j) == (y1, x1):
                            break
                        j += 1
    for i in range(len(floor)):
        for j in range(len(floor[i])):
            if floor[i][j] > 1:
                dangerous_areas += 1
    return dangerous_areas


def main():
    coords = read_file()
    print(f"Part 1 solution: {find_dangerous_areas(coords)}")
    print(f"Part 2 solution: {find_dangerous_areas(coords, part2=True)}")


if __name__ == "__main__":
    main()
