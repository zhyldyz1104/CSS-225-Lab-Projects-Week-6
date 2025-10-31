# Zhyldyz
# 10/31/2025
# Search on the internet for a way to calculate an approximation for pi. There are
# many that use simple arithmetic. Write a program to compute the approximation and then
# print that value as well as the value of math.pi from the math module

# π ≈ 4 × (1 - 1/3 + 1/5 - 1/7 + 1/9 - ...)

import math

approx_pi = 0

for i in range(10000):
    term = (-1) ** i / (2 * i + 1)
    approx_pi += term
approx_pi *= 4
print("Approximate π:", approx_pi)
print("math.pi:", math.pi)
