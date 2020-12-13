import math
from sympy.ntheory.modular import crt

input = """1000066
13,x,x,41,x,x,x,37,x,x,x,x,x,659,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,19,x,x,x,23,x,x,x,x,x,29,x,409,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,17"""


arr = input.split("\n")
ts = int(arr[0])
data = arr[1].split(",")

busses = []
busses_offset = []
bussesall = []

for a in data:
    if a != "x":
        busses.append(int(a))
    bussesall.append(a)

for bus in busses:
    offset = ((math.floor(ts / bus) + 1) * bus) - ts
    busses_offset.append(offset)

#min_index = busses_offset.index(min(busses_offset))
#print("solution: ", busses[min_index] * busses_offset[min_index])

# chinese reminder theme - crazy stuff
print("solution 2:", crt([bus for bus in busses], [bus - bussesall.index(str(bus)) for bus in busses],)[0])

