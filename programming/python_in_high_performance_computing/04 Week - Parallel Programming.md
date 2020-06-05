# Python in High-Performance Computing - PRACE

# 04 Week - Parallel Programming

During this week we discuss how parallel programming within the message passing paradigm can be done with Python and mpi4py package.

## Introduction to parallel programming

### Computing in parallel

The underlying idea in parallel computing is that the computational problem can be split into smaller subtasks. Multiple subtasks can then be executed simultaneously by multiple processing units. In modern CPUs, the single execution unit is typically a CPU core.

### Types of parallel problems

Parallel programs can be divided in two limiting classes:

- Tightly coupled:
  - Lots of interaction between subtasks;
  - Low latency high speed interconnect between the CPUs is essential for good performance;

- Embarrassingly parallel:
  - Very little (or no) interaction between subtasks;
  - Programming these types of problems is typically easier;

### Exposing parallelism

One common way to expose parallelism is by distributing the data. Each processing unit (e.g. CPU core) holds part of the data, and performs typically identical or at least very similar operations on the data.

Other common parallelization model is the task farm (or master / worker) approach, where a master sends tasks to workers and receives then results from them.

### Parallel Scaling

When the size of the input data is kept constant, but one increases the number of processing units, we typically speak about strong parallel scaling. The purpose of parallel programming in this case is to decrease the time to solve the problem. The relative parallel speed-up can be defined in terms of the $T_p$ (the execution time with $p$ processing units):

$$
S_{\mathrm{rel}} = \frac{T_{p}}{T_{p+1}}
$$

In real-world problems this is rarely the case, and typically when increasing the processing units enough the execution time can even start to increase, resulting in relative speed-up which is smaller than one.

### Processes and threads

The two main types of execution units: processes and threads, in more detail.

#### Threads: Shared Memory Parallelization

- A parallel program that starts as a single process is a single process executing a parallel program
- At some point, the program starts something called a parallel region
- In the parallel region, multiple threads will start executing the program
- The main thing here is that you have multiple threads and they are all sharing the same memory space

*Example*: OpenMP in C and Fortran

#### Processes

- Instead of having a single process, we will have multiple processes in parallel
- They are independent processes but they are executing the same program code
- These independent processes they have their own memory space and they are completely independent from each other
- To exchange information between these processes, you need to explicity send and receive messages between the processes

### Parallel programming with Python

Python has a rich ecosystem also for parallel computing, both standard library and third party packages provide tools for different parallel programming approaches.

[Threading](https://docs.python.org/3/library/threading.html) module provides a thread based approach, whereas multiprocessing is based on child processes. There is also a higher level concurrent.futures module which can utilize either threads or processes

- The standard CPython interpreter has the Global Interpreter Lock, which allows only one thread to execute Python code at once

For parallel data analytics that needs to scale over multiple computers:

- [Dask](https://dask.org/) is a Python library providing advanced parallelism with easy to use interfaces (e.g. NumPy-like parallel Dask array)
- [PySpark](https://spark.apache.org/docs/latest/api/python/pyspark.html) is a Python interface to Apache Spark, a general distributed cluster-computing framework for big data processing


## Message passing with Python

### Introduction to MPI

Message Passing Interface (MPI) is an application programming interface (API) for communication between separate processes.

MPI is the most widely used approach for distributed parallel computing with compilers and libraries available on all typical computer architectures. Python interface is provided by MPI for Python ([mpi4py](https://mpi4py.readthedocs.io/)).

#### MPI contains routines for:

- Communication between processes
  - sending and receiving messages between two processes
  - sending and receiving messages between several processes
- Synchronization between processes
- Communicator creation and manipulation
- Advanced features (e.g. user defined datatypes, one-sided communication and parallel I/O)

### Execution model

A MPI program is launched as a set of independent, identical processes. Each process executes exactly the same program code and instructions and they can reside in different CPU cores, compute nodes or even in different computers.

A high-bandwidth and low-latency interconnect is needed for good performance.

The MPI launcher is needed to start a MPI program: *mpirun*, *mpiexec*, and *srun*.

### MPI communicator

The communicator is a special object representing a group of processes that participate in communication. The communication will involve some or all of the processes in a communicator.

In default execution, all processes start in a global communicator called MPI_COMM_WORLD (or MPI.COMM_WORLD in mpi4py).

In Python, most MPI routines are implemented as methods of a communicator object.

### Data model

As all MPI processes are completely independent, they also have complete separation of data. Each process has its own separate memory space. To exchange information, processes need to explicitly send and receive messages.

### Getting started

To get started with MPI, it is a good idea to look into two basic methods of a communicator object:

- *Get_size()*: total number of MPI processes executing the program
- *Get_rank()*: the unique ID (rank) assigned to this process

### Simple example: Hello world

```python
from mpi4py import MPI

comm = MPI.COMM_WORLD # communicator object containing all processes

size = comm.Get_size()
rank = comm.Get_rank()

print("I am rank %d in group of %d processes" % (rank, size))
```

And running:

```sh
# Needed in MacOS:
$ export PMIX_MCA_gds=hash 

$ mpirun -np 4 python3 hello_world_mpi.py

I am rank 2 in group of 4 processes
I am rank 0 in group of 4 processes
I am rank 3 in group of 4 processes
I am rank 1 in group of 4 processes
```

### Example: Parallel Sum

A p arallel algorithm to calculate the total sum of all elements in array A:

1. Scatter the data
   1. receive operation for scatter
   2. send operation for scatter
2. Compute partial sums in parallel
3. Gather the partial sums
   1. receive operation for gather
   2. send operation for gather
4. Compute the total sum

## MPI Communication

Since MPI processes are independent, in order to coordinate work, they need to communicate by explicitly sending and receiving messages.

### Point-To-Point Communication

In point-to-point communication, one process sends a message (some data) to another process that receives it. The sends and receives in a program have to match: one receive per one send.

- *Example*: Sending and receiving a dictionary

```python
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    data = {'a': 7, 'b': 3.14}
    comm.send(data, dest=1)
elif rank == 1:
    data = comm.recv(source=0)
```

#### Sending and receiving data

Python objects can be communicated with the *send()* and *recv()* methods of a communicator. This includes all standard Python objects and most derived ones as well.

The basic interfaces are:

- .send(data, dest)
  - data: Python object to send
  - dest: destination rank
- .recv(source)
  - source: source rank

#### Fast communication of large arrays

In practice, Python objects are converted to byte streams (pickled) when sending and back to Python objects (unpickled) when receiving.

MPI for Python offers alternative routines for sending and receiving contiguous memory buffers (such as NumPy arrays) with very little overhead.

#### Send/receive NumPy arrays

To send, one needs to use the upper case method *Send()* giving the NumPy array and destination rank as arguments:

```python
Send(data, dest)
```

To receive, one needs to first prepare a NumPy array to receive the data to and then use the upper case method *Recv()*:

```python
data = numpy.empty(shape, dtype)
Recv(data, source)
```

The routine *Sendrecv()* is a combination of *Send()* and *Recv()* routines:

```python
buffer = numpy.empty(data.shape, dtype=data.dtype)
Sendrecv(data, dest=tgt, recvbuf=buffer, source=src)
```

#### Communicate any contiguous array

##### MPI datatypes

MPI has the following pre-defined datatypes:

- MPI.INT for an integer (int)
- MPI.DOUBLE for a floating point number (float)
- MPI.CHAR for a single character (str)
- MPI.COMPLEX for a complex number (complex)

If you have another type of contiguous array, you have to do it manually instead. It can be automatically obtained from a NumPy array, but now we need to define them manually as a list of three items: buffer, count, datatype. For example, assuming data contains an array of 100 integers:

```python
comm.Send([data, 100, MPI.INT], dest=tgt)
```

### Non-blocking communication

In non-blocking communication, the communication will happen in the background while the process is free to do something else in the mean time. It means doing some local calculations while waiting for some synchronisation with neighbouring processes to be finished.

Non-blocking communication allows concurrent computation and communication and avoids many common deadlock situations and is the smart way to do point-to-point communication in MPI.

#### Finalise communication

All non-blocking communication needs to be finalised at some point. If you want to wait for the communication started with *isend* or *irecv* (or *Isend* etc.) to finish, you can simply use *wait()*.

- *Example*: non-blocking send/receive

```python
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
    data = arange(size, dtype=float) * (rank + 1)
    req = comm.Isend(data, dest=1)    # start a send
    calculate_something(rank)         # .. do something else ..
    req.wait()                        # wait for send to finish
    # safe to read/write data again

elif rank == 1:
    data = empty(size, float)
    req = comm.Irecv(data, source=0)  # post a receive
    calculate_something(rank)         # .. do something else ..
    req.wait()                        # wait for receive to finish
    # data is now ready for use
```

### #Multiple non-blocking operations

*waitall* will wait for all initiated requests to complete and *waitany* will wait for one of the initiated requests to complete. To wait for all of them to be finished with:

```python
MPI.Request.waitall(requests)
Similar functions are also available for testing multiple requests.
```

- *Example*: Non-blocking message chain

```python
from mpi4py import MPI
import numpy

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# send buffer
data = numpy.arange(10, dtype=float) * (rank + 1)
# receive buffer
buffer = numpy.zeros(10, dtype=float)

tgt = rank + 1
src = rank - 1
if rank == 0:
    src = MPI.PROC_NULL
if rank == size - 1:
    tgt = MPI.PROC_NULL

req = []
req.append(comm.Isend(data, dest=tgt))
req.append(comm.Irecv(buffer, source=src))

MPI.Request.waitall(req)
```

### Communicators

A MPI communicator is a object representing a group of processes that participate in communication. The communication will involve some or all of the processes in a communicator. In Python, most MPI routines are implemented as methods of a communicator object.

#### User-defined communicators

All processes start in a global communicator called MPI_COMM_WORLD (or MPI.COMM_WORLD in mpi4py), but the user can also define. By default a single universal communicator exists to which all processes belong (MPI.COMM_WORLD).

A new communicator is created as a collective operation of an existing communicator. To split the processes in a communicator into sub-groups:

```python
comm = MPI.COMM_WORLD
rank = comm.Get_rank()

color = rank % 4

local_comm = comm.Split(color)
local_rank = local_comm.Get_rank()

print("Global rank: %d Local rank: %d" % (rank, local_rank))
```

## Collective Communication

Collective communication transfers data between all the processes in a communicator.

MPI includes collective communication routines for data movement and for collective computation and synchronisation. The MPI barrier *comm.barrier()* makes every task hold until all tasks in the communicator comm have called it.

The collective routines must be called by all the processes in the communicator. Also, the amount of data sent and received must match.

The code when using collective communication tirns more compact and easier to maintain. Then, **collective communication is usually the smart way of doing MPI communication**.

- *Comparison example*: communicating a numpy array of 1M elements from task 0 to all the other tasks is simplified from something like this:

```python
if rank == 0:
    for i in range(1, size):
        comm.Send(data, i)
else:
    comm.Recv(data, 0)
```

into a single line of code:

```python
comm.Bcast(data, 0)
```

#### Broadcast

Broadcast sends the same data from one process to all the other processes. It replicates the data to all processes, so that they all have it available locally.

- *Example*: Broadcasting a dictionary and a numpy array

```python
from mpi4py import MPI
import numpy

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    py_data = {'key1' : 0.0, 'key2' : 11}  # Python object
    data = numpy.arange(8) / 10.              # numpy array
else:
    py_data = None
    data = numpy.zeros(8)

new_data = comm.bcast(py_data, root=0)
comm.Bcast(data, root=0)
```

#### Scatter

Scatter sends an equal amount of data from one process to all the other processes and allows it to distribute data equally among the processes.

- *Example*: Scattering a list of numbers (one number to each task) and a numpy array (multiple elements to each task)

```python
from mpi4py import MPI
from numpy import arange, empty

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
if rank == 0:
    py_data = range(size)
    data = arange(size**2, dtype=float)
else:
    py_data = None
    data = None

# returns the value
new_data = comm.scatter(py_data, root=0)

# prepare a receive buffer
buffer = empty(size, float)
# in-place modification
comm.Scatter(data, buffer, root=0)
```

### Collective communication: many to one

#### Gather

Gather collects an equal amount of data from all the processes in a communicator to one process. It as an inverse scatter operation that allows to collect partial results from the tasks.

- *Example*: Gathering a list of single values (rank) from each process as well as a numpy array of multiple elements (data) that are then stored in a larger receive array (buffer)

```python
from mpi4py import MPI
from numpy import arange, zeros

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

data = arange(10, dtype=float) * (rank + 1)
buffer = zeros(size * 10, float)

# returns the value
n = comm.gather(rank, root=0)
# in-place modification
comm.Gather(data, buffer, root=0)
```

#### Reduce

Reduce gathers data from all the processes in a communicator and applies an operation on the data before storing the result in a single process. It is just like gather but with an additional operation applied to the gathered data.

- *Example*: Reduction using MPI.SUM to calculate the total sum of all received values

```python
from mpi4py import MPI
from numpy import arange, zeros

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

data = arange(10 * size, dtype=float) * (rank + 1)
buffer = zeros(size * 10, float)

# returns the value
n = comm.reduce(rank, op=MPI.SUM, root=0)
# in-place modification
comm.Reduce(data, buffer, op=MPI.SUM, root=0)
```

### Collective communication: many to many

#### Allreduce

Allreduce is a Reduce operation followed by Broadcast, so that in the end of the operation all processes have the results of reduction. The MPI library can implement the operation more efficiently than when using two successive calls.

- *Example*: Allreduce usafge

```python
from mpi4py import MPI
from numpy import arange, empty

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

data = arange(10 * size, dtype=float) * (rank + 1)
buffer = empty(size * 10, float)

# returns the value
n = comm.allreduce(rank, op=MPI.SUM)
# in-place modification
comm.Allreduce(data, buffer, op=MPI.SUM)
```

#### Alltoall

In Alltoall each process sends and receives to/from each other, and can be considered as combination of Scatter and Gather. The operation can be also viewed as “transpose”.

- *Example*: Alltoall both with a Python list and a NumPy array

```python
from mpi4py import MPI
from numpy import arange, empty, zeros_like

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

py_data = range(size)
data = arange(size**2, dtype=float)

new_data = comm.alltoall(py_data)  # returns the value

buffer = zeros_like(data) # prepare a receive buffer
comm.Alltoall(data, buffer)  # in-place modification
```

