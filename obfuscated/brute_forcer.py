# the naive approach is too slow,
# just how I like it

from subprocess import run, PIPE
from time import sleep
b64_chars = "AQgwBRhxCSiyDTjzEUk0FVl1GWm2HXn3IYo4JZp5Kaq6Lbr7Mcs8Ndt9Oeu+Pfv/"

f = open('/dev/null', 'w')

for a in b64_chars:
    print(a)
    for b in b64_chars:
        for c in b64_chars:
            for d in b64_chars:
                # f.write(a+b+c+d)
                # print(a+b+c+d)
                p = run(['python3', 'processed_3.py'], stdout=PIPE, input=(a+b+c+d).encode())
                if p.stdout != b'?':
                    print(p.stdout)
