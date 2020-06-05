# Python in High Performance Computing - PRACE
# 01 Week - Introduction and Performance Analysis

During the following weeks we will discuss various topics related to high-performance computing and Python.

- Analysing performance of Python programs
- Performing numerical computations efficiently with Python
- Using Python with compiled code
- Parallel programming with Python

## Why are Python programs slow?

- Python is an interpreted language 
  - Features that make development rapid with Python are a result of that, with the price of reduced performance in some cases;

- Dynamic Typing
  - As variables get type only during the runtime as values are assigned to them, it is more difficult for the interpreter to optimize the execution (in comparison, a compiler can make extensive analysis and optimization before the execution)

- Flexible data structures
  - The built-in data structures of Python are very flexible, but they are also very generic, which makes them not so well suited for extensive numerical computations;
  - Data structure implementation, as CPython, can turn it quite efficient;

- Multithreading
  - Unfortunately, the memory management of the standard CPython interpreter is not thread-safe, and it uses something called Global Interpreter Lock (GIL) to safeguard memory integrity;

## Where program spends time?

**Analyse before you optimize.**

Low-level optimization should be done only after correctness and readability are taken care of, especially as low-level optimization normally detracts readability.

First, make the program work correctly, then you should try to optimize the program.

**90/10 rule: 90% of time is spent in 10% of the source code.**

The two main ways to analyze performance:
- via applications own timers, which measure the time spent in specific region of a program;
- by utilizing special performance analysis software;

## Using applications own timers

Python standard library has a time module which provides various time-related functions. time.process_time function can be used for measuring a specific region:

```python
from math import exp, sin
import time

def calculate(a):
    result = 0
    for val in a:
        result += exp(val) * sin(val)
    return result

x = [0.1 * i for i in range(1000)]
t0 = time.process_time()

for r in range(1000):
    calculate(x)
t1 = time.process_time()

print("Time spent", t1 - t0)
```

### Timing with a context manager

Python context managers provide features for executing functions when entering and exiting a region, using the *with* statement.

```python
from math import exp, sin
import time

class Timer:
    def __enter__(self):
        self.start = time.process_time()
        return self

    def __exit__(self, *args):
        self.end = time.process_time()
        self.interval = self.end - self.start

def calculate(a):
    result = 0
    for val in a:
        result += exp(val) * sin(val)
    return result

x = [0.1 * i for i in range(1000)]
with Timer() as t:
    for r in range(1000):
        calculate(x)
print("Time spent", t.interval)
```

## Measuring small code snippets with *timeit*

Measuring very short execution times has some pitfalls that can be avoided with the help of the *timeit* Python module.

Python standard library contains the *timeit* module. When a code snippet is measured with *timeit*, the module takes care of running the snippet several times and calculating statistics.

```
IPython 6.1.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: from math import sin, cos

In [2]: %timeit sin(0.2)
68.8 ns ± 0.181 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)

In [3]: %timeit cos(0.2)
71.1 ns ± 1.57 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)
```

## Using cProfile

cProfile is powerful performance analysis tool included in the Python standard library.

### How to measure the profile of the whole program

```sh
# Generating dat file
python3 -m cProfile -o profile.dat <YOUR-PROGRAM>.py

# Explore dat file using pstats module
python3 -m pstats profile.dat
```

The module *pstats* opens an interactive browser over documentation and statistics of the program.

- Examples of *pstats* commands:
-- 'help': lists all documented commands
-- 'help <COMMAND>': documentation and statistics of a given command
-- 'sort time': shows time spent in each function sorted by execution time

#### Testing cProfile
You can use 'hpc-python/demos/cython/mandel_main.py' program to test.

```sh
python3 setup.py build_ext --inplace
python3 -m cProfile -o profile.dat mandel_main.py 
python3 -m pstats profile.dat
```

### Performance analysis of heat equation solver

Now, we analyse the code of *performance/cprofile/heat_main.py* file, which heat (or diffusion) equation is a partial differential equation that describes how the temperature varies in space over time.

Using *cProfile*, we found:

```
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      200   26.234    0.131   26.234    0.131 hpc-python/performance/cprofile/heat.py:9(evolve)
        2    0.116    0.058    0.116    0.058 {built-in method matplotlib._png.write_png}
      247    0.049    0.000    0.049    0.000 {built-in method marshal.loads}
```

Which means that the program takes more time inside the *heat.py* execution, done 200 times, in the *evolve* function.

We can also use *pysintrument* module:

```
python3 -m pyinstrument -o pyinstrument.dat heat_main.py
```

The analysis file *pyinstrument.dat* contains:

```
  _     ._   __/__   _ _  _  _ _/_   Recorded: 15:53:23  Samples:  666
 /_//_/// /_\ / //_// / //_'/ //     Duration: 26.842    CPU time: 27.190
/   _/                      v3.1.3

Program: heat_main.py

26.842 <module>  heat_main.py:1
├─ 26.482 main  heat_main.py:8
│  └─ 26.194 iterate  heat.py:27
│     └─ 26.194 evolve  heat.py:9
└─ 0.357 <module>  heat.py:1
```