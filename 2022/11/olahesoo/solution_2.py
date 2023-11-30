from __future__ import annotations
from math import floor
from typing import Callable, Any
from dataclasses import dataclass

with open('input') as infile:
    inlines = [i.strip() for i in infile.readlines()]

@dataclass
class Monkey:
    number: int
    items: list[int]
    operation: Callable[[int], int]
    relief: Callable[[int], int]
    test: Callable[[int], bool]
    true_monkey: Monkey
    false_monkey: Monkey
    inspection_count: int = 0

    def set_monkeys(self, true_monkey: Monkey, false_monkey: Monkey):
        self.true_monkey = true_monkey
        self.false_monkey = false_monkey
    
    def inspect(self):
        self.inspection_count += len(self.items)
        self.items = [self.relief(self.operation(item)) for item in self.items]

    def act(self):
        self.inspect()
        for item in self.items:
            if self.test(item):
                self.true_monkey.items.append(item)
            else:
                self.false_monkey.items.append(item)
        self.items = []

    def get_inspection_count(self):
        return self.inspection_count
    
    def __str__(self):
        return (f'monkey {self.number}')

# Manual input parsing is faster to write :)
# Calculate relief mod by multiplying all prime numbers in tests
sample_monkeys = {
        0: Monkey(0, [79, 98], lambda x: x*19, lambda x: x%96577, lambda x: x%23 == 0, None, None),
        1: Monkey(1, [54, 65, 75, 74], lambda x: x+6, lambda x: x%96577, lambda x: x%19 == 0, None, None),
        2: Monkey(2, [79, 60, 97], lambda x: x*x, lambda x: x%96577, lambda x: x%13 == 0, None, None),
        3: Monkey(3, [74], lambda x: x+3, lambda x: x%96577, lambda x: x%17 == 0, None, None),
        }
sample_monkeys[0].set_monkeys(sample_monkeys[2], sample_monkeys[3])
sample_monkeys[1].set_monkeys(sample_monkeys[2], sample_monkeys[0])
sample_monkeys[2].set_monkeys(sample_monkeys[1], sample_monkeys[3])
sample_monkeys[3].set_monkeys(sample_monkeys[0], sample_monkeys[1])

# Calculate relief mod by multiplying all prime numbers in tests
relief_mod = 9699690
monkeys = {
        0: Monkey(0, [80], lambda x: x*5, lambda x: x%relief_mod, lambda x: x%2 == 0, None, None),
        1: Monkey(1, [75, 83, 74], lambda x: x+7, lambda x: x%relief_mod, lambda x: x%7 == 0, None, None),
        2: Monkey(2, [86, 67, 61, 96, 52, 63, 73], lambda x: x+5, lambda x: x%relief_mod, lambda x: x%3 == 0, None, None),
        3: Monkey(3, [85, 83, 55, 85, 57, 70, 85, 52], lambda x: x+8, lambda x: x%relief_mod, lambda x: x%17 == 0, None, None),
        4: Monkey(4, [67, 75, 91, 72, 89], lambda x: x+4, lambda x: x%relief_mod, lambda x: x%11 == 0, None, None),
        5: Monkey(5, [66, 64, 68, 92, 68, 77], lambda x: x*2, lambda x: x%relief_mod, lambda x: x%19 == 0, None, None),
        6: Monkey(6, [97, 94, 79, 88], lambda x: x*x, lambda x: x%relief_mod, lambda x: x%5 == 0, None, None),
        7: Monkey(7, [77, 85], lambda x: x+6, lambda x: x%relief_mod, lambda x: x%13 == 0, None, None),
        }

monkeys[0].set_monkeys(monkeys[4], monkeys[3])
monkeys[1].set_monkeys(monkeys[5], monkeys[6])
monkeys[2].set_monkeys(monkeys[7], monkeys[0])
monkeys[3].set_monkeys(monkeys[1], monkeys[5])
monkeys[4].set_monkeys(monkeys[3], monkeys[1])
monkeys[5].set_monkeys(monkeys[6], monkeys[2])
monkeys[6].set_monkeys(monkeys[2], monkeys[7])
monkeys[7].set_monkeys(monkeys[4], monkeys[0])

def get_inspection_counts(monkeys, rounds):
    for i in range(rounds):
        for j in range(len(monkeys)):
            monkeys[j].act()
    return [monkey.get_inspection_count() for monkey in monkeys.values()]

inspection_counts = get_inspection_counts(monkeys, 10000)
inspection_counts.sort()
print(inspection_counts[-2] * inspection_counts[-1])

