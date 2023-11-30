def count_calories(inlines):
    max_calories = [0, 0, 0]
    current_calories = 0
    for i in inlines:
        if i == "":
            for i in range(len(max_calories)):
                if current_calories > max_calories[i]:
                    max_calories[i] = current_calories
                    max_calories.sort()
                    break
            current_calories = 0
        else:
            current_calories += int(i)
    
    return sum(max_calories)

with open('input') as infile:
    inlines = [i.strip() for i in infile.readlines()]
    print(count_calories(inlines))

