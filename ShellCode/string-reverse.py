#!/usr/bin/python3

strToReverse = "/bin//sh"

reverseStr = strToReverse[::-1]

print(reverseStr)
print()


hex_vals = (bytes(reverseStr, "ascii")).hex()


hex_chars = ""

for index, hexchhar in enumerate(hex_vals):
    hex_chars += hexchhar
    if((index + 1) % (2*4) == 0):
        if(index == 0):
            hex_chars += hexchhar
            continue
        print(f"PUSH: 0x{hex_chars}")
        hex_chars = ""



if(hex_chars != ""):
    remaining_chars = (index+1) % (2*4)
    high_order_zeros = "0" * (8 - remaining_chars)
    print(f"PUSH: 0x{high_order_zeros}{hex_chars}")


