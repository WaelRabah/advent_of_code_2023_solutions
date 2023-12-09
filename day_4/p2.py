import os
import re


def count_winning_numbers_in_card(numbers: str) -> int:
    winning_numbers, my_numbers = numbers.strip().split("|")
    pattern = re.compile(r"\s+")
    winning_numbers = re.sub(pattern, " ", winning_numbers)
    my_numbers = re.sub(pattern, " ", my_numbers)
    winning_numbers = winning_numbers.strip().split(" ")
    my_numbers = my_numbers.strip().split(" ")
    count = 0
    for num in my_numbers:
        if num in winning_numbers:
            count += 1

    return count


def count_scratchoffs(start: int, finish: int, total_cards_num: int):
    total = 0
    for idx in range(start, finish):
        copies_num = cards_counter_history.get(idx, 0)
        if copies_num == 0:
            continue
        total += copies_num
        total += count_scratchoffs(
            idx +  1, min(idx + 1 + copies_num, total_cards_num), total_cards_num
        )
    return total


def main():
    inputs_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt")
    final_sum = 0
    with open(inputs_path, mode="r") as f:
        cards = f.readlines()
        cards = [c.split(":")[1] for _, c in enumerate(cards)]
        for idx, c in enumerate(cards):
            cards_counter_history[idx] = count_winning_numbers_in_card(c)
        final_sum = len(cards) + count_scratchoffs(0, len(cards), len(cards))

    return final_sum


if __name__ == "__main__":
    cards_counter_history = dict()
    print(main())
