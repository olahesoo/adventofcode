import pprint

def mine(materials):
    materials_copy = materials.copy()
    materials_copy["ore"] += materials["ore_robots"]
    materials_copy["clay"] += materials["clay_robots"]
    materials_copy["obsidian"] += materials["obsidian_robots"]
    materials_copy["geodes"] += materials["geode_robots"]
    return materials_copy

def build_robot(materials, robot_type, blueprint):
    materials_copy = materials.copy()
    for (material, amount) in blueprint[f"{robot_type}_robot_cost"].items():
        materials_copy[material] -= amount
    materials_copy[f"{robot_type}_robots"] += 1
    return materials_copy

def optimise_materials(materials, blueprint):
    materials_copy = materials.copy()
    highest_ore_cost = max([blueprint[f"{robot_type}_robot_cost"]["ore"] for robot_type in ["ore", "clay", "obsidian", "geode"]])
    materials_copy["ore"] = min(materials["ore"], highest_ore_cost*2)
    materials_copy["clay"] = min(materials["clay"], blueprint["obsidian_robot_cost"]["clay"]*2)
    materials_copy["obsidian"] = min(materials["obsidian"], blueprint["geode_robot_cost"]["obsidian"]*2)
    return materials_copy

def find_highest_geodes(materials, time_remaining, blueprint):
    if materials == None:
        materials = {
                "ore": 0,
                "ore_robots": 1,
                "clay": 0,
                "clay_robots": 0,
                "obsidian": 0,
                "obsidian_robots": 0,
                "geodes": 0,
                "geode_robots": 0
                }
    materials = optimise_materials(materials, blueprint)

    hashed_state = (frozenset(materials.items()), time_remaining)
    if hashed_state in highest_geodes:
        return highest_geodes[hashed_state]

    if time_remaining <= 0:
        highest_geodes[hashed_state] = materials["geodes"]
        return materials["geodes"]

    possible_results = []
    possible_results.append(mine(materials))

    if materials["ore"] >= blueprint["ore_robot_cost"]["ore"]:
        result = mine(materials)
        result = build_robot(result, "ore", blueprint)
        possible_results.append(result)

    if materials["ore"] >= blueprint["clay_robot_cost"]["ore"]:
        result = mine(materials)
        result = build_robot(result, "clay", blueprint)
        possible_results.append(result)

    if materials["ore"] >= blueprint["obsidian_robot_cost"]["ore"] and materials["clay"] >= blueprint["obsidian_robot_cost"]["clay"]:
        result = mine(materials)
        result = build_robot(result, "obsidian", blueprint)
        possible_results.append(result)

    if materials["ore"] >= blueprint["geode_robot_cost"]["ore"] and materials["obsidian"] >= blueprint["geode_robot_cost"]["obsidian"]:
        result = mine(materials)
        result = build_robot(result, "geode", blueprint)
        possible_results.append(result)

    geode_counts = [find_highest_geodes(i, time_remaining - 1, blueprint) for i in possible_results]
    highest_geode_count = max(geode_counts)
    highest_geodes[hashed_state] = highest_geode_count
    return highest_geode_count

with open('input') as infile:
    inlines = [i.strip() for i in infile.readlines()]

blueprints = []
for (index, line) in enumerate(inlines):
    split_line = line.split()
    blueprint = {
            "ore_robot_cost": {
                "ore": int(split_line[6])
                },
            "clay_robot_cost": {
                "ore": int(split_line[12])
                },
            "obsidian_robot_cost": {
                "ore": int(split_line[18]),
                "clay": int(split_line[21])
                },
            "geode_robot_cost": {
                "ore": int(split_line[27]),
                "obsidian": int(split_line[30])
                }
            }
    blueprints.append((index + 1, blueprint))

quality_product = 1
for (id_number, blueprint) in blueprints[:3]:
    print(f"{id_number}/3")
    # Global variable for each blueprint
    highest_geodes = {}
    geodes = find_highest_geodes(None, 32, blueprint)
#    best_geodes_path = [(path, count) for (path, count) in highest_geodes.items() if count == geodes]
#    best_geodes_path = sorted(best_geodes_path, key=lambda x: x[0][1])
#    pprint.pp(best_geodes_path)
    print(id_number, geodes)
    quality_product *= geodes

print(quality_product)

