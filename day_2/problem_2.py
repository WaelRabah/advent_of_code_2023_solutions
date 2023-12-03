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
            _, games_str = line.split(":")
            game_rounds = games_str.strip().split(";")
            max_possible_red = 0
            max_possible_green = 0
            max_possible_blue = 0
            for round in game_rounds:
                num_red, num_blue, num_green = count_colors(round)
                if num_red > max_possible_red:
                    max_possible_red = num_red
                if num_green > max_possible_green:
                    max_possible_green = num_green
                if num_blue > max_possible_blue:
                    max_possible_blue = num_blue
            print(max_possible_red, max_possible_green, max_possible_blue)
            final_sum += max_possible_red * max_possible_green * max_possible_blue

    return final_sum


print(main())
