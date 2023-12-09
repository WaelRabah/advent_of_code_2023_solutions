import os
import re


def main():
    inputs_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt")
    final_sum = 0
    digits = tuple(str(i) for i in range(0, 10))
    with open(inputs_path, mode="r") as f:
        all_lines = f.readlines()
        l = len(all_lines[0])
        joined_lines = "".join(all_lines)
        matches = [
            (match.group(), match.start()) for match in re.finditer(r"\*", joined_lines)
        ]
        for m in matches:
            idx = m[1]
            after = joined_lines[
                idx : idx + 4 if joined_lines[idx + 1] in digits else idx + 1
            ]
            before = joined_lines[
                idx - 3 if joined_lines[idx - 1] in digits else idx : idx + 1
            ]
            top = joined_lines[
                (idx - l - 3 if joined_lines[idx - l - 1] in digits else idx - l) : (
                    idx - l + 4 if joined_lines[idx - l + 1] in digits else idx - l + 1
                )
            ]
            bottom = joined_lines[
                (idx + l - 3 if joined_lines[idx + l - 1] in digits else idx + l) : (
                    idx + l + 4 if joined_lines[idx + l + 1] in digits else idx + l + 1
                )
            ]
            special_character_matches = re.findall(
                r"[0-9]+",
                ",".join(
                    [
                        before,
                        after,
                        top,
                        bottom,
                    ]
                ),
            )
            print(
                special_character_matches,
                [
                    before,
                    after,
                    top,
                    bottom,
                ],
            )

            if len(special_character_matches) == 2:
                final_sum += int(special_character_matches[0]) * int(
                    special_character_matches[1]
                )
    return final_sum


print(main())
