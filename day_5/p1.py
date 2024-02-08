import os


def main():
    inputs_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt")
    final_sum = 0
    with open(inputs_path, mode="r") as f:
        # cards = f.readlines()
        # cards = [c.split(":")[1] for _, c in enumerate(cards)]
        seeds =[int(s) for s in f.readline().split("seeds: ")[-1].split(" ")]
        seed_to_soil_map = {seed: seed for seed in seeds}
        soil_to_fertilizer_map = dict()
        fertilizer_to_water_map = dict()
        water_to_light_map = dict()
        light_to_temperature_map = dict()
        temperature_to_humidity_map = dict()
        humidity_to_location_map = dict()
        f.readline()

        # seed-to-soil map:
        f.readline()
        while (line := f.readline()) != "\n" and len(line) > 0:
            destination_start, source_start, range_length = map(int, line.split(" "))
            destination_end, source_end = (
                destination_start + range_length,
                source_start + range_length,
            )
            for seed in seeds:
                seed = int(seed)
                if seed == seed_to_soil_map.get(seed):
                    if seed >= source_start and seed <= source_end:
                        delta = seed - source_start
                        seed_to_soil_map[source_start + delta] = destination_start + delta
                    else:
                        seed_to_soil_map[seed] = seed
        print(seed_to_soil_map)
        input()
        # soil-to-fertilizer map:
        f.readline()
        while (line := f.readline()) != "\n" and len(line) > 0:
            destination_start, source_start, range_length = map(int, line.split(" "))
            destination_end, source_end = (
                destination_start + range_length,
                source_start + range_length,
            )
            for seed in seeds:
                soil = seed_to_soil_map[seed]
                if soil == soil_to_fertilizer_map.get(soil):
                    if soil >= source_start and soil <= source_end:
                        delta = soil - source_start
                        soil_to_fertilizer_map[source_start + delta] = (
                            destination_start + delta
                        )
                    else:
                        soil_to_fertilizer_map[soil] = soil

        print(soil_to_fertilizer_map)
        input()
        # fertilizer-to-water map:
        f.readline()
        while (line := f.readline()) != "\n" and len(line) > 0:
            destination_start, source_start, range_length = map(int, line.split(" "))
            destination_end, source_end = (
                destination_start + range_length,
                source_start + range_length,
            )
            for seed in seeds:
                soil = seed_to_soil_map[seed]
                fertilizer = soil_to_fertilizer_map[soil]
                if fertilizer == fertilizer_to_water_map.get(fertilizer):
                    if fertilizer >= source_start and fertilizer <= source_end:
                        delta = fertilizer - source_start
                        fertilizer_to_water_map[source_start + delta] = (
                            destination_start + delta
                        )
                    else:
                        fertilizer_to_water_map[fertilizer] = fertilizer

        print(fertilizer_to_water_map)
        input()
        # water-to-light map:
        f.readline()
        while (line := f.readline()) != "\n" and len(line) > 0:
            destination_start, source_start, range_length = map(int, line.split(" "))
            destination_end, source_end = (
                destination_start + range_length,
                source_start + range_length,
            )
            for seed in seeds:
                soil = seed_to_soil_map[seed]
                fertilizer = soil_to_fertilizer_map[soil]
                water = fertilizer_to_water_map[fertilizer]
                if water == water_to_light_map.get(water):
                    if water >= source_start and water <= source_end:
                        delta = water - source_start
                        water_to_light_map[source_start + delta] = destination_start + delta
                    else:
                        water_to_light_map[water] = water


        print(water_to_light_map)
        input()
        # light-to-temperature map:
        f.readline()
        while (line := f.readline()) != "\n" and len(line) > 0:
            destination_start, source_start, range_length = map(int, line.split(" "))
            destination_end, source_end = (
                destination_start + range_length,
                source_start + range_length,
            )
            for seed in seeds:
                soil = seed_to_soil_map[seed]
                fertilizer = soil_to_fertilizer_map[soil]
                water = fertilizer_to_water_map[fertilizer]
                light = water_to_light_map[water]
                if light == light_to_temperature_map.get(light):
                    if light >= source_start and light <= source_end:
                        delta = light - source_start
                        light_to_temperature_map[source_start + delta] = (
                            destination_start + delta
                        )
                    else:
                        light_to_temperature_map[light] = light


        print(light_to_temperature_map)
        input()
        # temperature-to-humidity map:
        f.readline()
        while (line := f.readline()) != "\n" and len(line) > 0:
            destination_start, source_start, range_length = map(int, line.split(" "))
            destination_end, source_end = (
                destination_start + range_length,
                source_start + range_length,
            )
            for seed in seeds:
                soil = seed_to_soil_map[seed]
                fertilizer = soil_to_fertilizer_map[soil]
                water = fertilizer_to_water_map[fertilizer]
                light = water_to_light_map[water]
                temp = light_to_temperature_map[light]
                if temp == temperature_to_humidity_map.get(temp):
                    if temp >= source_start and temp <= source_end:
                        delta = temp - source_start
                        temperature_to_humidity_map[source_start + delta] = (
                            destination_start + delta
                        )
                    else:
                        temperature_to_humidity_map[temp] = temp

        print(temperature_to_humidity_map)
        input()
        # humidity-to-location map:
        f.readline()
        while (line := f.readline()) != "\n" and len(line) > 0:
            destination_start, source_start, range_length = map(int, line.split(" "))
            destination_end, source_end = (
                destination_start + range_length,
                source_start + range_length,
            )
            for seed in seeds:
                soil = seed_to_soil_map[seed]
                fertilizer = soil_to_fertilizer_map[soil]
                water = fertilizer_to_water_map[fertilizer]
                light = water_to_light_map[water]
                temp = light_to_temperature_map[light]
                humidity = temperature_to_humidity_map[temp]
                
                if humidity == humidity_to_location_map.get(humidity):
                    if humidity >= source_start and humidity <= source_end:
                        delta = humidity - source_start
                        humidity_to_location_map[source_start + delta] = (
                            destination_start + delta
                        )

                    else:
                        humidity_to_location_map[humidity] = humidity
        print(humidity_to_location_map)
        input()
    # print(
    #     seed_to_soil_map,
    #     soil_to_fertilizer_map,
    #     fertilizer_to_water_map,
    #     water_to_light_map,
    #     light_to_temperature_map,
    #     temperature_to_humidity_map,
    #     humidity_to_location_map,
    # )
    print(humidity_to_location_map)
    return min(humidity_to_location_map.values())


if __name__ == "__main__":
    cards_counter_history = dict()
    print(main())
