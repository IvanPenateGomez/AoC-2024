import subprocess
from time import time

# Path to your PyPy executable
pypy_executable = r"C:\Users\gagre\Downloads\pypy3.10-v7.3.17-win64\pypy3.10-v7.3.17-win64\pypy3.exe"

start = time()
for x in range(1, 26):
    print(f"\nRunning day {x}")
    start2 = time()
    subprocess.run([pypy_executable, f"day {x}.py"], check=True)
    t2 = time() - start2
    print(f"Time taken: {int(t2)} seconds, {int((t2 % 1) * 1000)} milliseconds")
t = time() - start
print(f"Time taken: {int(t)} seconds and {int((t % 1) * 1000)} milliseconds")