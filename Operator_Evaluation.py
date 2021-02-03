import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

inputs = input().split()
o = inputs[0]
if o=="/":o="//"
x = int(inputs[1])
n = list(inputs[2])
n.insert(x,o)
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(eval("".join(n)))
