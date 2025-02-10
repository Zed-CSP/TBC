# (1)
# Complete the sequence_calculator function, which should
# Return the n-th number of the sequence S_n, defined as:
# S_n = 3*S_(n-1) - S_(n-2), with S_0 = 0 and S_1 = 1.
# Your implementation should minimize the execution time.
#
# (2)
# Find the time complexity of the proposed solution, using
# the "Big O" notation, and explain in detail why such
# complexity is obtained, for n ranging from 0 to at least
# 100000. HINT: you are dealing with very large numbers!
#
#
#
#********************ANSWER*************************************************
#   The algorithm has O(n) time complexity because:
#   1. It uses a single loop that iterates n-1 times
#   2. Each iteration performs constant time operations:
#       - One multiplication (3 * prev1)
#       - One subtraction (- prev2)
#       - Variable assignments
#   3. No recursive calls or nested loops are used
#   4. The space complexity is O(1) as it maintains only two variables
#       regardless of input size
#
#********************END OF ANSWER*****************************************
#
# (3)
# Plot the execution time VS n (again, for n ranging from 0
# to at least 100000).
#
# (4)
# Confirm that the empirically obtained time complexity curve
# from (3) matches the claimed time complexity from (2) (e.g.
# by using curve fitting techniques).
#
#********************ANSWER*************************************************
#   It doesnt match the claimed time complexity from (2)! ;D
#
#   while the algorithmic complexity appears O(n) from the code structure,
#   the actual runtime complexity is affected by the growing cost
#   of system operations on increasingly large numbers,
#   leading to a better fit with quadratic or cubic models in practice.
#
#********************END OF ANSWER*****************************************

import numpy as np
import matplotlib.pyplot as plt
import time
from scipy.optimize import curve_fit

def sequence_calculator(n):
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    # Use dynamic programming with only two variables to minimize memory usage
    prev2, prev1 = 0, 1
    
    for _ in range(2, n + 1): # O(n)
        current = 3 * prev1 - prev2 # O(1)
        prev2, prev1 = prev1, current # O(1)
    
    return prev1

def measure_execution_time(n): 
    start_time = time.time()
    result = sequence_calculator(n)
    end_time = time.time()
    return end_time - start_time

def linear_fit(x, a, b):
    return a * x + b

def quadratic_fit(x, a, b, c):
    return a * x**2 + b * x + c

def cubic_fit(x, a, b, c, d):
    return a * x**3 + b * x**2 + c * x + d

# Generate data points for time complexity analysis
n_values = np.linspace(0, 100000, 50, dtype=int)
times = []

for n in n_values:
    execution_time = measure_execution_time(n)
    times.append(execution_time)

# Plot execution time vs n
plt.figure(figsize=(10, 6))
plt.plot(n_values, times, 'b.', label='Measured times')
plt.xlabel('n')
plt.ylabel('Execution time (seconds)')
plt.title('Time Complexity Analysis')

# Curve fitting to confirm complexity
popt_quad, _ = curve_fit(quadratic_fit, n_values, times)
popt_linear, _ = curve_fit(linear_fit, n_values, times)
popt_cubic, _ = curve_fit(cubic_fit, n_values, times)

# Plot the different fits
plt.plot(n_values, quadratic_fit(n_values, *popt_quad), 'r-', 
         label=f'Quadratic fit (ax² + bx + c)\na={popt_quad[0]:.2e}, b={popt_quad[1]:.2e}, c={popt_quad[2]:.2e}')
plt.plot(n_values, linear_fit(n_values, *popt_linear), 'g-', 
         label=f'Linear fit (ax + b)\na={popt_linear[0]:.2e}, b={popt_linear[1]:.2e}')
plt.plot(n_values, cubic_fit(n_values, *popt_cubic), 'y-', 
         label=f'Cubic fit (ax³ + bx² + cx + d)\na={popt_cubic[0]:.2e}, b={popt_cubic[1]:.2e}, c={popt_cubic[2]:.2e}, d={popt_cubic[3]:.2e}')

plt.legend()
plt.grid(True)
plt.show()

# Print result for n=100000
print(f"S_{100000} = {sequence_calculator(100000)}")
