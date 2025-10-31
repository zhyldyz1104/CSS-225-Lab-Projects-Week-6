# Zhyldyz
# 10/31/2025
# Problem 5 – Convert radians to degrees
import math

radians = float(input("Enter the number of radians:"))
manual_degrees = radians * (180 / math.pi)
module_degree = math.degrees(radians)
print(module_degree)
print(manual_degrees)
