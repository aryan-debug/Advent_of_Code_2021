from pathlib import Path


def read_file():
    with open(Path(__file__).parent / "input.txt", "r") as file:
        rows = [[*map(int, line.strip())] for line in file.readlines()]
        return rows


def check_risk_point(point_y: int, point_x: int, points: list[tuple[int, int]]) -> bool:
    for delta_y, delta_x in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
        try:
            if (
                points[point_y][point_x] >= points[point_y + delta_y][point_x + delta_x]
                and -1 < point_y + delta_y < len(points)
                and -1 < point_x + delta_x < len(points[point_y])
            ):
                return False
        except IndexError:
            pass
    return True


def sum_risk_points(points: list[tuple[int, int]]) -> tuple[int, list[tuple[int, int]]]:
    low_points = []
    total = 0
    for row in range(len(points)):
        for col in range(len(points[row])):
            if check_risk_point(row, col, points):
                low_points.append((row, col))
                total += points[row][col] + 1
    return total, low_points


def get_neighbours(
    low_point_y: int, low_point_x: int, points: list[tuple[int, int]]
) -> list[tuple[int, int]]:
    queue = [(low_point_y, low_point_x)]
    for point_y, point_x in queue:
        for delta_y, delta_x in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
            try:
                if (
                    points[point_y + delta_y][point_x + delta_x] < 9
                    and -1 < point_y + delta_y < len(points)
                    and -1 < point_x + delta_x < len(points[point_y])
                    and (point_y + delta_y, point_x + delta_x) not in queue
                ):
                    queue.append((point_y + delta_y, point_x + delta_x))
            except IndexError:
                pass
    return queue


def find_three_largest_basins(low_points: list[tuple[int, int]], points: list[tuple[int, int]]) -> int:
    basins = []
    total = 1
    for low_point_y, low_point_x in low_points:
        basins.append(get_neighbours(low_point_y, low_point_x, points))
    for basin in sorted(basins, key=len, reverse=True)[:3]:
        total *= len(basin)
    return total


def main():
    points = read_file()
    total, low_points = sum_risk_points(points)
    total_2 = find_three_largest_basins(low_points, points)
    print(f"Part 1 solution: {total}")
    print(f"Part 2 solution: {total_2}")


main()
