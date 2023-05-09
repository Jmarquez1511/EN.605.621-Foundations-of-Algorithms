from datetime import datetime
from pathlib import Path
import sys
from SourceCode.interweave import isinterweave

x = input('Please enter a string value for x\n')
y = input('Please enter a string value for y\n')
s = input('Please enter a string value for s\n')

if not(isinstance(x, str) and isinstance(y, str) and isinstance(s, str)):
    print('You need to enter string values for x, y, and s')
    quit()

today = datetime.now().strftime("%Y%m%d%H%M%S")


value, comps = isinterweave(x, y, s, 0)

if value:
    print(f's is an interweave of x and y, it took {comps} comparisons to find the result.\n')
else:
    print(f's is not an interweave of x and y, it took {comps} comparisons to find the result.\n')

file_name = f'SourceCode/Inputs/{str(today)}.txt'
file = Path(file_name)
original_stdout = sys.stdout
with file.open('w') as file:
    sys.stdout = file
    print(f'x:{x}')
    print(f'y:{y}')
    print(f's:{s}\n')
    sys.stdout = original_stdout
print(f'You can find the input file at {file_name}')

file_name = f'SourceCode/Outputs/{str(today)}.txt'
file = Path(file_name)
original_stdout = sys.stdout
with file.open('w') as file:
    sys.stdout = file
    print(f'x:{x}')
    print(f'y:{y}')
    print(f's:{s}\n')
    if value:
        print(f's is an interweave of x and y, it took {comps} comparisons to find the result.')
    else:
        print(f's is not an interweave of x and y, it took {comps} comparisons to find the result.')
    sys.stdout = original_stdout
print(f'You can find the output file at {file_name}\n')







