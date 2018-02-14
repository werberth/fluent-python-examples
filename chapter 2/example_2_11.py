invoice = """
... 0.....6..................................40............52...55........
... 1909 Pimoni PiBrella                         $17.50   3         $52.50
... 1489 6mm Tactile Switch x20                   $4.50   2          $9.90
... 1510 Panavise Hr, - PV-201                   $28.00   1         $28.00
... 1601 PiTFT Mini Kit 320x240                  $34.95   1         $34.95
"""

SKU = slice(0, 6)
DESCRIPTION = slice(6, 40)
UNIT_PRICE = slice(40, 52)
QUANTITY = slice(52, 55)
ITEM_TOTAL = slice(55, None)
lines_items = invoice.split('\n')[2:]

for item in lines_items:
    print(item[UNIT_PRICE], item[DESCRIPTION])

# === result ===
#         $17 09 Pimoni PiBrella
#          $4 89 6mm Tactile Switch x20
#         $28 10 Panavise Hr, - PV-201
#         $34 01 PiTFT Mini Kit 320x240
