import os
import ctypes

# References:
#
# How to load a dll:
# https://stackoverflow.com/questions/7586504/python-accessing-dll-using-ctypes?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
#
# How to wrap a C++ file in C
# https://stackoverflow.com/questions/1615813/how-to-use-c-classes-with-ctypes?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
#
# Fix error message about "ValueError: Procedure probably called with too many arguments (16 bytes in excess)"
# https://stackoverflow.com/questions/41760830/ctypes-procedure-probably-called-with-too-many-arguments-92-bytes-in-excess?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
#
# Instructions for writing a dll and calling it from Python
# http://wolfprojects.altervista.org/articles/dll-in-c-for-python/
#
#


path_to_dll = r'C:\Users\Allen W. Ingling\Projects\TestUDll\Debug\TestUDll.dll'

#dll = ctypes.windll.LoadLibrary(path_to_dll)
dll = ctypes.CDLL(path_to_dll)

#dll.TimesTwo.argtypes(ctypes.c_double, ctypes.c_double)
x = ctypes.c_double(44.4)
y = ctypes.c_double(66.6)
dll.TimesTwo.restype = ctypes.c_double
z = dll.TimesTwo(x, y)
print(z)


