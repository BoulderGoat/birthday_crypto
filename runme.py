import binascii


"""
String to decipher/decrypt:
6fac24bb9c847ea1298f1bc37ae52fab3c45b60f5fc0b74de3d04be6

as binary the data is:
11011111010110000100100101110111001110010000100011111101
01000010010100110001111000110111100001101111010111001010
01011111010101100111100010001011011011000001111010111111
1000000101101110100110111100011110100000100101111100110

as bytes the data is:
b'o\xac$\xbb\x9c\x84~\xa1)\x8f\x1b\xc3z\xe5/\xab<E\xb6\x0f_\xc0\xb7M\xe3\xd0K\xe6'
"""

hex_string_1 = "6fac24bb9c847e"
hex_string_2 = "a1298f1bc37ae5"
hex_string_3 = "2fab3c45b60f5f"
hex_string_4 = "c0b74de3d04be6"

byte_array_1 = bytes.fromhex(hex_string_1)
byte_array_2 = bytes.fromhex(hex_string_2)
byte_array_3 = bytes.fromhex(hex_string_3)
byte_array_4 = bytes.fromhex(hex_string_4)

binary_string_1 = ""
binary_string_2 = ""
binary_string_3 = ""
binary_string_4 = ""

print("data1: ", byte_array_1, type(byte_array_1), len(byte_array_1))
print("data2: ", byte_array_2, type(byte_array_2), len(byte_array_2))
print("data3: ", byte_array_3, type(byte_array_3), len(byte_array_3))
print("data4: ", byte_array_4, type(byte_array_4), len(byte_array_4))
