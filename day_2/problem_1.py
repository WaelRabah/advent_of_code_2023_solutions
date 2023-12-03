MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14


def count_colors(round: str):
    colors_counter = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }

    for selected_color in round.split(","):
        count, color = selected_color.strip().split(" ")
        colors_counter[color] = int(count)

    return (
        colors_counter.get("red"),
        colors_counter.get("blue"),
        colors_counter.get("green"),
    )


def main():
    final_sum = 0
    with open("input.txt", mode="r") as f:
        for line in f:
            game_id, games_str = line.split(":")
            game_rounds = games_str.strip().split(";")
            is_impossible_game = False
            for round in game_rounds:
                num_red, num_blue, num_green = count_colors(round)
                if num_red > MAX_RED or num_green > MAX_GREEN or num_blue > MAX_BLUE:
                    is_impossible_game = True
                    break

            if not is_impossible_game:
                final_sum += int(game_id.split(" ")[-1])

    return final_sum


print(main())
