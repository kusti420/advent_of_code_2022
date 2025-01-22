if __name__ == "__main__":
    # import os; exec(open(f"{os.path.dirname(os.path.dirname(os.path.realpath(__file__)))}\\setup.txt").read())
    import os
    idk = f"{os.path.dirname(os.path.dirname(os.path.realpath(__file__)))}"
    year = idk.split("\\")[-1]
    idk = idk.replace(f"\\{year}", "")
    # print(idk)
    exec(open(f"{idk}\\setup.txt").read())

    data = [line for line in data if line != ""]

    print(data, len(data))
    print()
    seeds = data[0]
    seeds = [int(x) for x in seeds.split(" ")[1::]]

    print(seeds)
    print()

    seed_to_soil_map = data[data.index(
        "seed-to-soil map:"):data.index("soil-to-fertilizer map:")][1::]
    seed_to_soil_map = [[int(y) for y in x.split(" ")]
                        for x in seed_to_soil_map]
    print(seed_to_soil_map)
    print()

    soil_to_fertilizer_map = data[data.index(
        "soil-to-fertilizer map:"):data.index("fertilizer-to-water map:")][1::]
    soil_to_fertilizer_map = [[int(y) for y in x.split(" ")]
                              for x in soil_to_fertilizer_map]
    print(soil_to_fertilizer_map)
    print()


if __name__ != "__main__":
    print("That would break the script. Please run it directly.")
