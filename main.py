# map

## procedural
names = ['Mary', 'Isla', 'Sam']

for i in range(len(names)):
    names[i] = hash(names[i])

print names

## functional
names = ['Mary', 'Isla', 'Sam']

print map(lambda x: hash(x), names)

# reduce

## procedural
people = [{'name': 'Mary', 'height': 160},
          {'name': 'Isla', 'height': 80},
          {'name': 'Sam'}]

height_total = 0
height_count = 0
for person in people:
    if 'height' in person:
        height_total += person['height']
        height_count += 1

if height_count > 0:
    average_height = height_total / height_count

    print average_height
    # => 120

## functional

people_with_height = filter(lambda p: 'height' in p, people)
height_count = len(people_with_height)
height_total = reduce(lambda a, p: a + p['height'], people_with_height, 0)

if height_count > 0:
    average_height = height_total / height_count

    print average_height