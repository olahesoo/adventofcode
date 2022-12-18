shortest_path = {}
def get_shortest_path(current_valve_name, desired_valve_name, valves):
    if current_valve_name == desired_valve_name:
        return 0
    if (current_valve_name, desired_valve_name) in shortest_path:
        return shortest_path[(current_valve_name, desired_valve_name)]
    if desired_valve_name in valves[current_valve_name]["tunnels"]:
        shortest_path[(current_valve_name, desired_valve_name)] = 1
        return 1

    to_search = [(i, 1) for i in valves[current_valve_name]["tunnels"]]
    searched = [current_valve_name]
    while to_search:
        searching = to_search.pop(0)
        name, distance = searching
        searched.append(name)
        for i in valves[name]["tunnels"]:
            if i == desired_valve_name:
                shortest_path[(current_valve_name, desired_valve_name)] = distance + 1
                return distance + 1
            elif i not in searched:
                to_search.append((i, distance + 1))

    raise RuntimeError("No path found from {current_valve_name} to {desired_valve_name}")


best_flows = {}
def get_best_flow(valve_path, remaining_time, valves):
    if (valve_path, remaining_time) in best_flows:
        return best_flows[(valve_path, remaining_time)]

    best_flow_amount = 0
    if remaining_time <= 1:
        best_flows[(valve_path, remaining_time)] = (0, valve_path)
        return (0, valve_path)

    self_flow_amount = 0
    self_name = valve_path[-1]
    if not valves[self_name]["flow_rate"]:
        next_remaining_time = remaining_time
        self_flow_amount = 0
    else:
        next_remaining_time = remaining_time - 1
        self_flow_amount += valves[self_name]["flow_rate"] * next_remaining_time

    best_flow_amount = self_flow_amount
    best_path = valve_path
    openable_valves = [name for (name, valve) in valves.items() if valve["flow_rate"] and name not in valve_path]
    for valve_name in openable_valves:
        distance = get_shortest_path(self_name, valve_name, valves)
        followed_flow_amount, followed_path = get_best_flow((*valve_path, valve_name), next_remaining_time - distance, valves)
        flow_amount = self_flow_amount + followed_flow_amount
        if flow_amount > best_flow_amount:
            best_flow_amount = flow_amount
            best_path = followed_path

    best_flows[(valve_path, remaining_time)] = (best_flow_amount, best_path)
    return (best_flow_amount, best_path)


with open('input') as infile:
    inlines = [i.strip() for i in infile.readlines()]

valves = {}

for i in inlines:
    description = i.split(maxsplit=9)
    name = description[1]
    flow_rate = int(description[4][5:-1])
    tunnels = description[9].split(', ')
    valves[name] = {
            "flow_rate": flow_rate,
            "tunnels": tunnels
            }

# This works only for my real input, not sample data
first_flow_amount, first_followed_path = get_best_flow(('AA',), 26, valves)
second_flow_amount, second_followed_path = get_best_flow((*first_followed_path, 'AA'), 26, valves)
print(first_flow_amount + second_flow_amount)

