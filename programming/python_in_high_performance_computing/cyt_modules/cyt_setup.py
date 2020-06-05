from distutils.core import Extension, setup

from Cython.Build import cythonize
from Cython.Compiler import Options

Options.docstrings = False

ext = Extension(name="cyt_module", sources=["cyt_module.pyx"])

setup(
    ext_modules = cythonize(ext),
)

