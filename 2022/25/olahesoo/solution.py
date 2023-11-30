digits = {
        '2': 2,
        '1': 1,
        '0': 0,
        '-': -1,
        '=': -2
        }

digit_order = ['0', '1', '2', '=', '-']

def decode_SNAFU(number_str):
    p = 0
    output = 0
    for i in number_str[::-1]:
        output += digits[i] * 5**p
        p += 1
    return output

def encode_SNAFU(number):
    rev_output = []
    while number:
        digit = digit_order[number % 5]
        rev_output.append(digit)
        number -= digits[digit]
        number = int(number / 5)
    return ''.join(rev_output[::-1])

with open('input') as infile:
    inlines = [i.strip() for i in infile.readlines()]

numbers_sum = sum([decode_SNAFU(i) for i in inlines])
print(encode_SNAFU(numbers_sum))

