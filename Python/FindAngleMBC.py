# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
AB = float(input())
BC = float(input())
rad = math.atan(AB/BC)
deg = math.degrees(rad)
print(int(round(deg)),chr(176),sep='')
