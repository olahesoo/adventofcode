def mix(numbers):
    enumerated_numbers = list(enumerate(numbers))
    for i in range(len(numbers)):
        index = [i[0] for i in enumerated_numbers].index(i)
        entry = enumerated_numbers.pop(index)
        enumerated_numbers.insert((index + entry[1]) % len(enumerated_numbers), entry)
    return [i[1] for i in enumerated_numbers]

with open('input') as infile:
    inlines = [i.strip() for i in infile.readlines()]

numbers = [int(i) for i in inlines]
mixed_numbers = mix(numbers)

zero_location = mixed_numbers.index(0)
answer_coords = [1000, 2000, 3000]
answer_numbers = [mixed_numbers[(i + zero_location) % len(numbers)] for i in answer_coords]
answer = sum(answer_numbers)
print(answer)

