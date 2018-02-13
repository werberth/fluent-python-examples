colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]

print(tshirts)
# result --> [('black', 'S'), ('black', 'M'), ('black', 'L'),
# ('white', 'S'), ('white', 'M'), ('white', 'L')]

for color in colors:
    for size in sizes:
        print((color, size))

# result
# ('black', 'S')
# ('black', 'M')
# ('black', 'L')
# ('white', 'S')
# ('white', 'M')
# ('white', 'L')

tshirts = [(color, size) for size in sizes for color in colors]

print(tshirts)
# result --> [('black', 'S'), ('white', 'S'), ('black', 'M'),
# ('white', 'M'), ('black', 'L'), ('white', 'L')]
