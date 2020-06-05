# Python in High-Performance Computing - PRACE

# 03 Week - Using Compiled Code and Libraries

In this week we discuss how pure Python code can be easily converted to a more static Cython code which has typically superior performance. We present also how code written in C/C++ or Fortran programming languages can be used from Python.

## What is Cython?

Cython is an optimising static compiler for Python that also provides its own programming language as a superset for standard Python.

Cython is designed to provide C-like performance for a code that is mostly written in Python by adding only a few C-like declarations to an existing Python code. Especially for scientific programs performing a lot of numerical computations, Cython can speed up the execution times more than an order of magnitude. Cython makes it also easy to interact with external C/C++ code.

Cython can alleviate the following Python performance bottlenecks:

- Interpretation overhead
- Unboxing or boxing Python objects
- Overheads of Python control structures
- Function call overheads

## Creating Cython modules

Normally, when working with Cython one does not Cythonize the whole program but only selected modules.

Using a Python module named as my_module.py:

```python
def add(x, y):
    result = x + y
    return result
```

It can be imported using:

```python
from my_module import add

z = add(4, 5)
```

Cython can transform the Python code into an equivalent C-code utilizing the Python API as:
```sh
$ cython3 my_module.py
```

The result is a file my_module.c, which can then be compiled into a Python C-extension. In order to make building of C-extensions from Cython easier, one does not normally use Cython directly from the command line but via Python distutils setup.py build file:

```python
from distutils.core import setup
from Cython.Build import cythonize

setup(
     ext_modules=cythonize("my_module.pyx"),
)
```

As the C-extension implements the fully dynamic Python code (just using the Python C-API), **transforming the pure Python module into C-extension gives normally only very modest speed-ups**. However, as we will discuss in the following steps, by adding Cython language extensions into the code (so it is no longer valid Python code) it is possible to achieve much more significant performance improvements.

## Using static typing

Python is both a strongly typed and a dynamically typed language. Due to dynamic typing, in Python the same variable can have a different type at different times during the execution. Dynamic typing allows for flexibility in programming, but with a price in performance.

One of the key features of Python is that everything is an object, and the type is just one attribute of an object. The fact that everything is an object means that there is a lot of “unboxing” and “boxing” involved when Python performs operations with variables.

There are several steps Python needs to do when adding two variables, for example:

1. Check the types of both operands
2. Check whether they both support the + operation
3. Extract the function that performs the + operation (due to operator overloading objects can have a custom definition for addition)
4. Extract the actual values of the objects
5. Perform the + operation
6. Construct a new integer object for the result

### Adding static type information

Cython allows one to add static typing information so that boxing and unboxing are not needed, and one can operate directly with the actual values.

When Cythonizing a Python code, static type information can be added either:

1. In function signatures by prefixing the formal arguments by their type
2. By declaring variables with the cdef Cython keyword, followed by the the type

The function works now only with integers but with less boxing/unboxing overheads.

```python
def add (int x, int y):
    cdef int result
    result = x + y
    return result
```

### The most common C types and their corresponding Python types

| From Python types | To C types    |
|-------------------|---------------|
| int               | int, long     |
| int, float        | float, double |
| str/bytes         | char *        |

## Where to add types?

Cython provides an easy-to-use annotate tool, which allows one to investigate the translation to C with web browser.

```sh
$ cython -a your_code.cyt
```

## Avoiding function call overheads

Function calls in Python are relatively expensive in comparison to for example C. Cython allows one to reduce this overhead significantly.

Main reason for the large function call overhead in Python is the “boxing” and “unboxing” of function call arguments and return values. Once again, dynamic typing makes programming more flexible but with a cost in performance.

For example:
```python
def inner(i):
    return i+1

def outer_1(n):
    x = 0
    for i in range(n):
        x = inner(x)
```

We can create also a version which does not have the function call:

```python
def outer_2(n):
    x = 0
    for i in range(n):
        x = x + 1
```

The function call in the loop is **typically 3-4 times slower**.

### Using pure C functions

If a function is used only within a Cython module, one can get rid of a large part of Python’s function call overhead by declaring the function as a pure C function, using the *cdef* keyword:

```python
cdef int add (int x, int y):
    cdef int result
    result = x + y
    return result
```

When a function is defined as a pure C function, it can be called only from the corresponding Cython module, but not from a Python code. If a function is called both from Cython and Python, Cython can generate an additional Python wrapper by declaring the function with *cpdef* instead of cdef:

```python
cpdef int add (int x, int y):
    cdef int result
    result = x + y
    return result
```

**If the function is not called from Python it is better to use just *cdef*.**

## Using NumPy with Cython

NumPy arrays are the work horses of numerical computing with Python, and Cython allows one to work more efficiently with them.

When working with NumPy arrays in Python one should avoid for-loops and indexing individual elements and instead try to write operations with NumPy arrays in a vectorized form. When taking Cython into the game that is no longer true. When the Python for structure only loops over integer values (e.g. for in range(N)), Cython can convert that into a pure C for loop. Also, when additional Cython declarations are made for NumPy arrays, indexing can be as fast as indexing C arrays.

### Compile time defitions for NumPy

In order to create more efficient C-code for NumPy arrays, additional declarations are needed. To start with, one uses the Cython cimport statement for getting access to NumPy types:

```python
cimport numpy as cnp
```

### More indexing enhancements

Python is still performing bounds checking for arrays (i.e. trying to access outside the allocated memory gives an error), and allowing negative indexing. If negative indexing is not needed, and one is certain that there are no out of bounds errors in indexing, performance can be enhanced even more by disabling negative indexing and bounds checking for all indexing operations within the function.

This is done by using cython decorators before the function as follows:

```python
@cython.boundscheck(False)
@cython.wraparound(False)
def func():  # declarations can be made only in function scope
    cdef cnp.ndarray[cnp.int_t, ndim=2] data
    data = np.empty((N, N), dtype=int)

    …
    for i in range(N):
        for j in range(N):
            data[i,j] = …       # double loop is done in nearly C speed
```

## Profiling Cython

As the first rule of optimization is to measure performance before starting any optimization work, one should have made profile of the pure Python code before starting any Cythonization. However, in the next optimization cycle one should profile also the Cython code.

In order to enable profiling for the whole function, simply include a global directive at the top of a file:

```python
# cython: profile=True

import numpy as np

def myfunc():
...
```

In order to enable profiling for a single function, one can include the cython decorator before a function definition:

```python
cimport cython

@cython.profile(True)
def my_func():
    ...
```

# Interfacing with external libraries

We discuss how to utilize external libraries or existing code written in C and Fortran in Python programs.

## Interfacing C code with CFFI

CFFI is an external package providing a C Foreign Function Interface for Python

- Allows to interact with almost any C code from Python
- C++ is not currently supported
- User needs to add C-like declarations to Python code
  - The declarations can often be directly copy-pasted from C headers or documentation

CFFI has two different main modes:

- ABI mode: accesses the library at binary level (easier)
- API mode: a separate compilation step with a C compiler is used (faster)

### Calling a C library function

Let’s call functions from C math library within Python code using API.

- Works for any shared object, i.e. .dll (Windows) or .so (Linux and others) or .dylib (OS X)
- To start with, we create a Python file which we will call *build_mymath.py*:

```python
from cffi import FFI
ffibuilder = FFI()

ffibuilder.cdef("""
    double sqrt(double x);   // list all the function prototypes from the
    double sin(double x);    // library that we want to use
                """)

# set_source() gives the name of the python extension module to
# produce, and some C source code as a string.  This C code needs
# to make the declarated functions, types and globals available,
# so it is often just the "#include".
ffibuilder.set_source("_my_math",
"""
     #include <math.h>   // the C header of the library
""",
   library_dirs = [],  # here we can provide where the library is located,
                       # as we are using C standard library empty list is enough
   libraries = ['m']   # name of the library we want to interface
)

ffibuilder.compile(verbose=True)
```

When we execute the script, CFFI creates a Python extension module, called _my_math in this case.

We can now import the module, and use the functions we selected via the lib handle:

```python
from _mymath import lib

a = lib.sqrt(4.5)
b = lib.sin(1.2)
```

The library functions **assume C double precision numbers as input arguments**, but CFFI takes care of converting Python float objects into C numbers, as well as converting the returned C doubles into Python floats.

### Creating Python extension from C source

You can utilize direct C source code instead of an existing library. Procedure for generating the Python extension module is almost the same as before, the only difference is that we provide the sources argument to the set_source function.

If the C code uses some libraries, these are still provided in the libraries argument, and build_mymath.py could look like:

```python
from cffi import FFI
ffibuilder = FFI()

ffibuilder.cdef("""
    double sqrt(double x);   // list all the function prototypes from the
    double sin(double x);    // library that we want to use
                """)

# set_source() gives the name of the python extension module to
# produce, and some C source code as a string.  This C code needs
# to make the declarated functions, types and globals available,
# so it is often just the "#include".
ffibuilder.set_source("_my_math",
"""
    double sqrt(double x);   // we don't have a header, so function prototypes
    double sin(double x);    // are provided directly
""",
   sources = ['mymath.c'],
   library_dirs = [],
   libraries = ['m']   # if mymath utilizes math library we need to include it
                       # here
)

ffibuilder.compile(verbose=True)
```

### Passing NumPy arrays to external C code

Let us assume we have a C-function add which sums up two arrays and returns the result in the third:

```python
// c = a + b
void add(double *a, double *b, double *c, int n)
{
  for (int i=0; i<n; i++)
     c[i] = a[i] + b[i];
}
```

If we want to use this function from Python, we can use CFFI for creating an extension module just as previously. When we use the module and the function, cast and from_buffer functions can be used for obtaining pointers to the “data areas” of NumPy arrays:

```python
from add_module import ffi, lib

a = np.random.random((1000000,1))
b = np.random.random((1000000,1))
c = np.zeros_like(a)

# Pointer objects need to be passed to library
aptr = ffi.cast("double *", ffi.from_buffer(a))
bptr = ffi.cast("double *", ffi.from_buffer(b))
cptr = ffi.cast("double *", ffi.from_buffer(c))

lib.add(aptr, bptr, cptr, len(a))
```

## Interfacing C code with Cython

As Cython code compiles down to C code, it is relatively straightforward to utilize also Cython for interfacing with C.

In order to use C functions and variables from the library, one must provide external declarations for them in the Cython .pyx file. Functions and variables can be defined elsewhere. The actual library or source implementing the function needs to be included in setup.py when building the extension module with Cython.

```python
cdef extern void add(double *a, double *b, double *c, int n)
```

With the above construct, Cython will add the declaration to the generated .c file. However, when using libraries it is preferable to have the actual library header included in the generated file:

```python
cdef extern from "mylib.h"
    void add(double *a, double *b, double *c, int n)
    void subtract(double *a, double *b, double *c, int n)
```

Cython does not itself read the C header file, so you still need to provide declarations from it that you use.

### Including the library in setup.py

Compared to building simple pure Cython modules, one has to provide some extra information in the setup.py. If the code to be interfaced is in a library (i.e. .so) one can use the following type of setup.py:

```python
from distutils.core import setup, Extension
from Cython.Build import cythonize

ext = Extension("module_name",
                sources=["cython_source.pyx",],
                libraries=["name",], # Cython module is linked against
                library_dirs=[".",]) # libname.so, looked in "."

setup(ext_modules=cythonize(ext))
```

You can also use direct C source files if more appropriate:

```python
from distutils.core import setup, Extension
from Cython.Build import cythonize

# Specify all sources in Extension object
ext = Extension("module_name",
                sources=["cython_source.pyx", "c_source.c"])

setup(ext_modules=cythonize(ext))
```

### Passing NumPy arrays from Cython to C

Cython needs to be able to pass a pointer to the “data area” of an array. For arrays that are declared as type of ndarray, Cython supports similar & syntax as in C:

```python
import numpy as np
cimport numpy as np

cdef extern from "myclib.h":

    void add(double *a, double *b, double *c, int n)

    void subtract(double *a, double *b, double *c, int n)

def add_py(np.ndarray[cnp.double_t,ndim=1] a,
           np.ndarray[cnp.double_t,ndim=1] b):

    add(&a[0], &b[0], &c[0], len(a))
```

## Interfacing Fortran code

The f2py is part of NumPy, and it is normally provided both as a command line tool as well as a Python module. We discuss here the command line tool.

Assume we have the following Fortran code that adds together two arrays (c = a + b):

```fortran
subroutine add(a, b, c, n)

  implicit none

  ! f2py understands only limited number of kind parameters
  real(kind=8), intent(in) :: a(n)
  real(kind=8), intent(in) :: b(n)
  real(kind=8), intent(out) :: c(n)
  integer :: n

  c = a + b

end subroutine
```

We can create a Python interface to this subroutine as follows:

```sh
$ f2py3 -c add.f90 -m fortran_module
```

The -c flag instructs f2py to compile and build a Python extension module from file add.f90, and the name of the this module is designated with the -m flag. 

We can now import the module, and use the functions from Python:

```python
import numpy as np
from fortran module import add

x = np.arange(10.)
y = np.arange(0.1, 10.1)
z = add(x, y)
```

More complex examples on how to use f2py can be found in the [f2py user guide](https://docs.scipy.org/doc/numpy/f2py/).
