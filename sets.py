showroom = set()
showroom = {'charger', 'blazer', 'challenger', 'octane'}

# print(showroom)
# print(len(showroom))

more_cars = set()
more_cars = {'cybertruck', 'mystery_machine'}

showroom.update(more_cars)
# print(showroom)

# showroom.discard('challenger')
# print(showroom)


junkyard = set()
junkyard = {'dominus', 'breakout', 'octane', 'challenger'}

same_cars = showroom.intersection(junkyard)
# print(same_cars)

all_cars = showroom.union(junkyard)
all_cars.discard('challenger')
print(all_cars)
