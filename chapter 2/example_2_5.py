symbols = '$¢£¥¤'
genexp_tuple = tuple(ord(symbol) for symbol in symbols)

print(genexp_tuple)
# === result ===
# (36, 162, 163, 165, 164)

import array
genexp_array = array.array('I', (ord(symbol) for symbol in symbols))

print(genexp_array)
# === result ===
# array('I', [36, 162, 163, 165, 164])
