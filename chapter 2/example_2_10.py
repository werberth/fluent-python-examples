from collections import namedtuple

City = namedtuple('City', 'name country population coordinates')

print(City._fields)
# === result ===
# ('name', 'country', 'population', 'coordinates')

LatLong = namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
delhi = City._make(delhi_data)

delhi_dict = delhi._asdict()
print(delhi_dict)
# === result ===
# OrderedDict([('name', 'Delhi NCR'),
#   ('country', 'IN'),('population', 21.935),
#   ('coordinates', LatLong(lat=28.613889, long=77.208889))])

for key, value in delhi._asdict().items():
    print(key + ':', value)

# === result ===
# name: Delhi NCR
# country: IN
# population: 21.935
# coordinates: LatLong(lat=28.613889, long=77.208889)
