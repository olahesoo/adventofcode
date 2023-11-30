with open('input') as infile:
    inlines = [i.strip() for i in infile.readlines()]

def get_score(first, second):
    results = {
            'A': {
                'X': 3,
                'Y': 6,
                'Z': 0
            },
            'B': {
                'X': 0,
                'Y': 3,
                'Z': 6
            },
            'C': {
                'X': 6,
                'Y': 0,
                'Z': 3
            }
        }

    return results[first][second]

values = {
        'X': 1,
        'Y': 2,
        'Z': 3
    }

sum = 0
for i in inlines:
    first, second = i.split()
    sum += get_score(first, second) + values[second]

print(sum)

