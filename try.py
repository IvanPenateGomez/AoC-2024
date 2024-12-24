import subprocess
import os

# Path to your PyPy executable
pypy_executable = r"C:\Users\gagre\Downloads\pypy3.10-v7.3.17-win64\pypy3.10-v7.3.17-win64\pypy3.exe"

for x in range(1, 24):
    print(f"\nRunning day {x}")
    subprocess.run([pypy_executable, f"day {x}.py"], check=True)
    