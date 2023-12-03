from typing import Tuple
def get_first_digit(s: str):
    for c in s:
        if c in "".join([str(i) for i in range(10)]):
            return int(c)
def extract_digits_from_s(s: str) -> Tuple[int,int]:
    text_to_digit_map = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    letter_digits = list(text_to_digit_map.keys())
    digits = list(text_to_digit_map.values())
    extracted_digits = []
    for x in letter_digits:
        first = s.find(x)
        last = s.rfind(x)
        if first > -1:
            extracted_digits.append((x, first))
        if last > -1:
            extracted_digits.append((x, last))
    for x in digits:
        first = s.find(x)
        last = s.rfind(x)
        if first > -1:
            extracted_digits.append((x, first))
        if last > -1:
            extracted_digits.append((x, last))
    extracted_digits_sorted_by_idx = sorted(extracted_digits, key=lambda x: x[1])
    if len(extracted_digits_sorted_by_idx) == 0:
        return s
    first_digit = extracted_digits_sorted_by_idx[0]
    last_digit = extracted_digits_sorted_by_idx[-1]
    first_digit= text_to_digit_map[first_digit[0]] if first_digit[0] in text_to_digit_map else first_digit[0]
    last_digit= text_to_digit_map[last_digit[0]] if last_digit[0] in text_to_digit_map else last_digit [0]
    return [int(first_digit), int(last_digit)]
def main():
    final_sum = 0
    with open("input.txt", mode="r") as f:
        for line in f:
            first, last = extract_digits_from_s(line[::])
            final_sum += int(f"{first}{last}")
    return final_sum
print(main())