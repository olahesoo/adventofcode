with open('input') as infile:
    inlines = [i.strip() for i in infile]

def contains(a, b):
    a1, a2 = a
    b1, b2 = b
    if (a1 <= b1 and b2 <= a2) or (b1 <= a1 and a2 <= b2):
        return True
    else:
        return False

out = 0
for i in inlines:
    a, b = i.split(',')
    a1, a2 = a.split('-')
    b1, b2 = b.split('-')
    if contains((int(a1), int(a2)), (int(b1), int(b2))):
        out += 1
print (out)

