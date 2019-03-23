import sys
data = sys.stdin.readlines()
try:
    multiplier = int(sys.argv[3])
except IndexError:
    multiplier = 1

for line in data:
    output = sys.argv[1] + "("
    for char in line:
        # print(char, file=sys.stderr)
        output += sys.argv[2] + "(" + str(ord(char) * multiplier) + ")+"
    output = output[:-1]
    output += ")"
    print(output)
