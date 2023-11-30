with open('input') as infile:
    inlines = [i.strip() for i in infile.readlines()]

def get_score(first, second):
    results = {
            'A': {
                'Z': 8,
                'Y': 4,
                'X': 3
            },
            'B': {
                'Z': 9,
                'Y': 5,
                'X': 1
            },
            'C': {
                'Z': 7,
                'Y': 6,
                'X': 2
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
    sum += get_score(first, second)

print(sum)

