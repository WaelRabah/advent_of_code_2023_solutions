import os
import re


def main():
    inputs_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt")
    final_sum = 0
    with open(inputs_path, mode="r") as f:
        all_lines = f.readlines()
        l = len(all_lines[0])
        joined_lines = "".join(all_lines)
        matches = [
            (match.group(), match.start())
            for match in re.finditer(r"[0-9]+", joined_lines)
        ]
        for m in matches:
            idx = m[1]
            char_after = joined_lines[idx + len(m[0])]
            char_before = joined_lines[idx - 1]
            line_before_range = joined_lines[
                (idx - l - 1) or 0 : idx - l + len(m[0]) + 1
            ]
            line_after_range = joined_lines[
                idx + l - 1 : idx + l + len(m[0]) + 1
            ]
            special_character_matches = re.findall(
                r"[^0-9.\n]",
                "".join([char_before, char_after, line_after_range, line_before_range]),
            )

            if len(special_character_matches) > 0:
                final_sum += int(m[0])
    return final_sum


print(main())
