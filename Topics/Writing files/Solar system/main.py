# create the planets.txt
list_of_planets = ['Mercury\n', 'Venus\n', 'Earth\n', 'Mars\n', 'Jupiter\n', 'Saturn\n', 'Uranus\n', 'Neptune\n']
file = open('planets.txt', 'w', encoding='utf-8')
file.writelines(list_of_planets)
file.close()
