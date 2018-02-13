symbols = '$¢£¥¤'
beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
print(beyond_ascii)
# result --> [36, 162, 163, 165, 164]

beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))
print(beyond_ascii)
# result --> [36, 162, 163, 165, 164]
