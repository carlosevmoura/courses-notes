# cython: language_level=3, boundscheck=False

def subtract(double x, double y):
	cdef double result
	result = x - y
	return result
