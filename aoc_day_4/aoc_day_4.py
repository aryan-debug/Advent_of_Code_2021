from pathlib import Path


def read_file() -> list[str, int]:
    with open(Path(__file__).parent / "input.txt", "r") as file:
        random_numbers = file.readline().split(",")
        boards = [line.split() for line in file.readlines()[1:] if line.strip()]
        return random_numbers, boards


def get_board(board_num: int, boards: list[list[str]]) -> list[list[str]]:
    return boards[board_num * 5 : (board_num + 1) * 5]


def check_rows(board: list[list[str]], drawn_numbers: list[str]) -> bool:
    for row in range(len(board)):
        if all(board[row][col] in drawn_numbers for col in range(5)):
            return True
    return False


def check_cols(board: list[list[str]], drawn_numbers: list[str]) -> bool:
    for row in range(len(board)):
        if all(board[col][row] in drawn_numbers for col in range(5)):
            return True
    return False


def find_winning_board(
    boards: list[list[str]], random_numbers: list[str], part1=False
) -> tuple[list[list[str]], list[str], int]:
    boards_won = []
    drawn_numbers = []
    final = 0
    for number in random_numbers:
        drawn_numbers.append(number.strip())
        for board_num in range(len(boards) // 5):
            current_board = get_board(board_num, boards)
            if check_rows(current_board, drawn_numbers) or check_cols(
                current_board, drawn_numbers
            ):
                if current_board not in boards_won:
                    boards_won.append(current_board)
                    final = number
                if part1:
                    return boards_won, drawn_numbers, number
        if len(boards_won) == len(boards) // 5:
            break
    return (boards_won, drawn_numbers, final)


def calculate_score(
    board: list[list[str]], drawn_numbers: list[str], final_number: int
) -> int:
    _sum = 0
    for row in range(len(board)):
        for col in range(len(board[row])):
            number = int(board[row][col])
            if str(number) not in drawn_numbers:
                _sum += number
    return int(final_number) * _sum


def main():
    random_numbers, boards = read_file()
    boards_won_1, drawn_numbers_1, final_number_1 = find_winning_board(
        boards, random_numbers, part1=True
    )
    boards_won, drawn_numbers, final_number = find_winning_board(boards, random_numbers)

    print(
        f"Part 1 solution: {calculate_score(boards_won_1[0], drawn_numbers_1, final_number_1)}"
    )
    print(
        f"Part 2 solution: {calculate_score(boards_won[-1], drawn_numbers, final_number)}"
    )


if __name__ == "__main__":
    main()
