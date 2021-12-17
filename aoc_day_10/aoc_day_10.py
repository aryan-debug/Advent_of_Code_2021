from pathlib import Path


def read_file():
    with open(Path(__file__).parent / "input.txt", "r") as file:
        chunks = [line.strip() for line in file.readlines()]
        return chunks


def get_solution(chunks: list[str]) -> tuple[int, int]:
    opening = "({[<"
    pairs = {")": "(", "}": "{", ">": "<", "]": "["}
    points = {")": 3, "]": 57, "}": 1197, ">": 25137}
    points_2 = {")": 1, "]": 2, "}": 3, ">": 4}
    total_points = 0
    points_list = []
    for chunk in chunks:
        error = False
        queue = []
        for bracket in chunk:
            if bracket in opening:
                queue.append(bracket)
            elif queue.pop() != pairs[bracket]:
                error = True
                total_points += points[bracket]
        if not error:
            completed = complete_brackets(chunk)[::-1]
            total_2 = 0
            for bracket in completed:
                total_2 *= 5
                total_2 += points_2[bracket]
            points_list.append(total_2)
    return total_points, sorted(points_list)[len(points_list) // 2]


def complete_brackets(chunk: str) -> str:
    while any(bracket not in "({[<" for bracket in chunk):
        chunk = (
            chunk.replace("()", "")
            .replace("[]", "")
            .replace("{}", "")
            .replace("<>", "")
        )
    return chunk.replace("{", "}").replace("(", ")").replace("<", ">").replace("[", "]")


def main():
    chunks = read_file()
    first_solution, second_solution = get_solution(chunks)
    print(f"Part 1 soltuion: {first_solution}")
    print(f"Part 2 soltuion: {second_solution}")


main()
