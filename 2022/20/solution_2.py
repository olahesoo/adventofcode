def mix(numbers):
    for i in range(len(numbers)):
        index = [i[0] for i in numbers].index(i)
        entry = numbers.pop(index)
        numbers.insert((index + entry[1]) % len(numbers), entry)
    return numbers

with open('input') as infile:
    inlines = [i.strip() for i in infile.readlines()]

decryption_key = 811589153
numbers = list(enumerate([int(i)*decryption_key for i in inlines]))
mixed_numbers = mix(numbers)
for i in range(9):
    mixed_numbers = mix(mixed_numbers)

zero_location = [i[1] for i in mixed_numbers].index(0)
answer_coords = [1000, 2000, 3000]
answer_numbers = [mixed_numbers[(i + zero_location) % len(mixed_numbers)][1] for i in answer_coords]
answer = sum(answer_numbers)
print(answer)

