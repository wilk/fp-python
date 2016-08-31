# transform an array

## procedural
names = ['Mary', 'Isla', 'Sam']

for i in range(len(names)):
    names[i] = hash(names[i])

print names

## functional
names = ['Mary', 'Isla', 'Sam']

print map(lambda x: hash(x), names)

