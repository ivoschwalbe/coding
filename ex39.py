def line(anzahl):
  print('- ' * anzahl)

states = {
  'Oregon': 'OR',
  'Florida': 'FL',
  'California': 'CA',
  'New York': 'NY',
  'Michigan': 'MI'
}

cities = {
  'CA': 'San Francisco',
  'MI': 'Detroit',
  'FL': 'Jacksonville'
}

# Schnacken machen kann man nicht!

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

line(30)
print('Michigan\'s abbrevation is: ', states['Michigan'])
print('Florida\'s abbrevation is: ', states['Florida'])

line(30)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

line(30)
for state, abbrev in list(states.items()):
  print(f"{state} is abbreviated {abbrev}")

line(30)
for abbrev, city in list(cities.items()):
  print(f"{abbrev} has city {city}")

line(30)
for state, abbrev in list(states.items()):
  print(f"{state} state is abbreviated {abbrev}")
  print(f"and has city {cities[abbrev]}")

line(30)
state = states.get('Texas')

if not state:
  print("Sorry, no Texas!")

city = cities.get('TX', 'Does not exist ...')
print(f"The city for the state 'TX' is: {city}")
