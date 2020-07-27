import binascii


"""
String to decipher/decrypt:
6fac24bb9c847ea1298f1bc37ae52fab3c45b60f5fc0b74de3d04be6

as bytes the data is:
b'o\xac$\xbb\x9c\x84~\xa1)\x8f\x1b\xc3z\xe5/\xab<E\xb6\x0f_\xc0\xb7M\xe3\xd0K\xe6'
which makes no sence...

as binary the data is:
01101111101011000010010010111011100111001000010001111110
10100001001010011000111100011011110000110111101011100101
00101111101010110011110001000101101101100000111101011111
11000000101101110100110111100011110100000100101111100110
"""

binary_string_1 = f'{0x6fac24bb9c847e:0>56b}'
binary_string_2 = f'{0xa1298f1bc37ae5:0>56b}'
binary_string_3 = f'{0x2fab3c45b60f5f:0>56b}'
binary_string_4 = f'{0xc0b74de3d04be6:0>56b}'

print("bin1: ", binary_string_1)
print("bin2: ", binary_string_2)
print("bin3: ", binary_string_3)
print("bin4: ", binary_string_4)

n = 8
bin_array_1 = [(binary_string_1[i:i+n])
               for i in range(0, len(binary_string_1), n)]
bin_array_2 = [(binary_string_2[i:i+n])
               for i in range(0, len(binary_string_2), n)]
bin_array_3 = [(binary_string_3[i:i+n])
               for i in range(0, len(binary_string_3), n)]
bin_array_4 = [(binary_string_4[i:i+n])
               for i in range(0, len(binary_string_4), n)]

print(bin_array_1)
print(bin_array_2)
print(bin_array_3)
print(bin_array_4)

hex_array_1 = [hex(int(bin_nbr, 2)) for bin_nbr in bin_array_1]
hex_array_2 = [hex(int(bin_nbr, 2)) for bin_nbr in bin_array_2]
hex_array_3 = [hex(int(bin_nbr, 2)) for bin_nbr in bin_array_3]
hex_array_4 = [hex(int(bin_nbr, 2)) for bin_nbr in bin_array_4]

print(hex_array_1)
print(hex_array_2)
print(hex_array_3)
print(hex_array_4)
