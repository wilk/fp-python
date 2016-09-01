# These examples are made following this article:
# https://maryrosecook.com/blog/post/a-practical-introduction-to-functional-programming

# map

## procedural
names = ['Mary', 'Isla', 'Sam']

for i in range(len(names)):
    names[i] = hash(names[i])

print names

## functional
names = ['Mary', 'Isla', 'Sam']

# transforms the names list into an hashes list
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
# filters for each person having the height
people_with_height = filter(lambda p: 'height' in p, people)
height_count = len(people_with_height)
# sums the height of each person
height_total = reduce(lambda a, p: a + p['height'], people_with_height, 0)

if height_count > 0:
    average_height = height_total / height_count

    print average_height

## functional solution #2
# transforms the height-filtered people list into a heights list
heights = map(lambda p: p['height'], filter(lambda p: 'height' in p, people))
height_count = len(heights)

if height_count > 0:
    # sum the heights
    average_height = reduce(lambda a, h: a + h, heights, 0) / height_count

    print average_height

# procedural
from random import random

print 'procedural race'

time = 5
car_positions = [1, 1, 1]

while time:
    # decrease time
    time -= 1

    print ''
    for i in range(len(car_positions)):
        # move car
        if random() > 0.3:
            car_positions[i] += 1

        # draw car
        print '-' * car_positions[i]

# functional
def draw_car(position):
    print '-' * position

def move_car(position):
    if random() > 0.3:
        position += 1

    return position

def race(time, positions):
    if time > 0:
        print ''

        positions = map(move_car, positions)
        map(draw_car, positions)
        time -= 1

        race(time, positions)

print 'functional race'
time = 5
car_positions = [1, 1, 1]
race(time, car_positions)

# functional solution #2
def draw(state):
    print ''
    print '\n'.join(map(lambda p: '-' * p, state['car_positions']))

def move(car_position):
    return car_position + 1 if random() > 0.3 else car_position

def race_step(state):
    return {'time': state['time'] - 1, 'car_positions': map(move, state['car_positions'])}

def race(state):
    draw(state)
    if state['time']:
        race(race_step(state))

print 'functional race #2'
time = 5
car_positions = [1, 1, 1]
race({'time': 5, 'car_positions': [1,1,1]})