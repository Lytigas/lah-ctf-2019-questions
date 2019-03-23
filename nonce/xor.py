import sys

file1_b = bytearray(open(sys.argv[1], 'rb').read())
file2_b = bytearray(open(sys.argv[2], 'rb').read())

size = min(len(file1_b), len(file2_b))
xord_byte_array = bytearray(size)

for i in range(size):
	xord_byte_array[i] = file1_b[i] ^ file2_b[i]

open(sys.argv[3], 'wb').write(xord_byte_array)
