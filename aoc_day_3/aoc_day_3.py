from pathlib import Path


def read_file() -> list[str, int]:
    with open(Path(__file__).parent / "input.txt", "r") as file:
        return [(line.strip()) for line in file]


def get_gamma_rate(binary_data: list[tuple[str]]) -> str:
    gamma_rate = ""
    for data in binary_data:
        count_0, count_1 = get_count(data)
        if count_1 > count_0:
            gamma_rate += "1"
        else:
            gamma_rate += "0"
    return gamma_rate


def zip_data(binary_data: list[str]) -> list[tuple[str]]:
    return [*zip(*binary_data)]


def get_eplison_rate(gamma_rate: str) -> int:
    eplison_rate = ""
    for i in gamma_rate:
        eplison_rate += str(int(i) ^ 1)
    return int(eplison_rate, 2)


def get_oxygen_data(binary_data: list[str]) -> str:
    current_bit = 0
    while len(binary_data) != 1:
        binary_data = filter_o2_data(binary_data, current_bit)
        current_bit += 1
    return binary_data[0]


def get_co2_data(binary_data: list[str]) -> str:
    current_bit = 0
    while len(binary_data) != 1:
        binary_data = filter_co2_data(binary_data, current_bit)
        current_bit += 1
    return binary_data[0]


def get_count(binary_data: tuple[str]) -> tuple[int, int]:
    return binary_data.count("0"), binary_data.count("1")


def filter_o2_data(binary_data: list[str], bit_to_check: int) -> list[str]:
    o2_data = []
    zipped_data = zip_data(binary_data)
    count_0, count_1 = get_count(zipped_data[bit_to_check])

    for i in range(len(zipped_data[0])):
        current_bit = zipped_data[bit_to_check][i]

        if (count_1 == count_0 or count_1 > count_0) and current_bit == "1":
            o2_data.append(binary_data[i])

        if count_0 > count_1 and current_bit == "0":
            o2_data.append(binary_data[i])

    return o2_data


def filter_co2_data(binary_data: list[str], bit_to_check: int) -> list[str]:
    co2_data = []
    zipped_data = zip_data(binary_data)
    count_0, count_1 = get_count(zipped_data[bit_to_check])

    for i in range(len(zipped_data[0])):
        current_bit = zipped_data[bit_to_check][i]

        if (count_1 == count_0 or count_0 < count_1) and current_bit == "0":
            co2_data.append(binary_data[i])

        if count_1 < count_0 and current_bit == "1":
            co2_data.append(binary_data[i])

    return co2_data


def main():
    binary_data = read_file()
    zipped_binary_data = zip_data(binary_data)
    gamma_rate = get_gamma_rate(zipped_binary_data)
    eplison_rate = get_eplison_rate(gamma_rate)
    oxygen_data = int(get_oxygen_data(binary_data), 2)
    co2_data = int(get_co2_data(binary_data), 2)

    print(f"Part 1 solution: {int(gamma_rate,2) * eplison_rate}")
    print(f"Part 2 solution: {oxygen_data * co2_data}")


main()
