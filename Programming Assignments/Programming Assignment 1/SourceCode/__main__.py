from numpy.random import choice
from numpy import arange
from datetime import datetime
from pathlib import Path
import sys
from math import comb
from SourceCode.closestpoints import Point, brute_force_closest_m_pairs, divide_and_conquer_m_closest_pairs

n = input('Please enter a number of points to be evaluated \n')
m = input('Please enter a value of m closest pairs \n')

try:
    n = int(n)
    m = int(m)
except ValueError:
    print('You need to enter integer values for n and m')

max_m = comb(n, 2)
if m > max_m:
    print(f'The maximum value allowed for m is {max_m}.'
          f'm={m}>={max_m}. Please select a value for m<={max_m}')
    quit()

today = datetime.now().strftime("%Y%m%d%H%M%S")

x_values = choice(arange(-n//4, n//4, 0.25), size=n, replace=False)
y_values = choice(arange(-n//4, n//4, 0.25), size=n, replace=False)
print(f'Your {n} points have been generated.\n')
points = [Point(x_values[i], y_values[i]) for i in range(n)]
file_name = f'Inputs/n{str(n)}_m{m}_{str(today)}.txt'
file = Path(file_name)
original_stdout = sys.stdout
with file.open('w') as file:
    sys.stdout = file
    print(f'The following are {n} x-y points')
    print(f'Out of which we will choose the {m} closest points')
    for i in range(len(x_values)):
        print(f'{x_values[i]},{y_values[i]}')
    sys.stdout = original_stdout
print(f'You can find the input file at {file_name}\n')

operations = 0
brute_result, operations = brute_force_closest_m_pairs(points, m, 0)
print(f'Below are the {m} closest points brute force')
for i in brute_result:
    print(brute_result[i]['distance'], brute_result[i]['points'][0], brute_result[i]['points'][1])
print(f'Operations under naive method = {operations}')

file_name = f'Outputs/n{str(n)}_m{m}_{str(today)}_brute.txt'
file = Path(file_name)
original_stdout = sys.stdout
with file.open('w') as file:
    sys.stdout = file
    print(f'Below are the {m} closest points')
    for i in brute_result:
        print(brute_result[i]['distance'], brute_result[i]['points'][0].__str__(),
              brute_result[i]['points'][1].__str__())
    sys.stdout = original_stdout
print(f'\nYou can find the output file for Brute Force at {file_name}\n')

dc_operations = 0
dc_result, dc_operations = divide_and_conquer_m_closest_pairs(points, m, 0)

print(f'Below are the {m} closest points under divide and conquer')
for i in dc_result:
    print(dc_result[i]['distance'], dc_result[i]['points'][0], dc_result[i]['points'][1])
print(f'Operations under divide and conquer = {dc_operations}')

file_name = f'Outputs/n{str(n)}_m{m}_{str(today)}_divide.txt'
file = Path(file_name)
original_stdout = sys.stdout
with file.open('w') as file:
    sys.stdout = file
    print(f'Below are the {m} closest points')
    for i in dc_result:
        print(dc_result[i]['distance'], dc_result[i]['points'][0].__str__(),
              dc_result[i]['points'][1].__str__())
    sys.stdout = original_stdout
print(f'\nYou can find the output file for Divide and Conquer at {file_name}\n')





