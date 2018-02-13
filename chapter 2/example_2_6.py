colors = ['black', 'white']
sizes = ['S', 'M', 'L']
for tshirt in ('%s %s' %(c,s) for c in colors for s in sizes):
    print(tshirt)

# === result ===
# black S
# black M
# black L
# white S
# white M
# white L
