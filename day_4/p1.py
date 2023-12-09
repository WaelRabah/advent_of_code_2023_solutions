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


def count_total_cards(cards: list[str], start: int, finish: int) -> int:
    if (cards_total := cards_total_history.get((start, finish))) is not None:
        return cards_total
    total = cards_total_history[(start, finish)] = 0
    for idx in range(start, finish):
        initial, card = cards[idx]
        card_num, numbers = card.split(":")
        if (count_matches := cards_counter_history.get(card_num)) is None:
            cards_counter_history[
                card_num
            ] = count_matches = count_winning_numbers_in_card(numbers)
            print(card_num)
        if count_matches > 0:
            print((start, finish), count_matches)
            total += count_matches + count_total_cards(
                [
                    (initial if idx >= start and idx <= finish else c[0], c[1])
                    for idx, c in enumerate(cards)
                ],
                initial + 1,
                min(len(cards), initial + count_matches + 1),
            )
    cards_total_history[(start, finish)] = total
    return total


def main():
    inputs_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt")
    final_sum = 0
    with open(inputs_path, mode="r") as f:
        cards = f.readlines()
        cards = [(idx, c) for idx, c in enumerate(cards)]
        final_sum = count_total_cards(cards, 0, len(cards))

    return final_sum


if __name__ == "__main__":
    cards_counter_history = dict()
    cards_total_history = dict()
    print(main())
