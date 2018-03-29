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

# walk up a directory tree "steps" number of steps, dropping steps number of directories from back of path string. e.g.
#  up_path("/remarkable/bird/norwegian/blue", 1)  -->  "/remarkable/bird/norwegian"
#  up_path("/remarkable/bird/norwegian/blue", 3)  -->  "/remarkable/"
#  up_path("/remarkable/bird/norwegian/blue", 10)  -->  "/"
def up_path(path, steps):
    for step in range(0, steps):
        path = os.path.split(path)[0]
    return path


# Try to find the dll file, assuming that the project which builds it is at the same level as this PyCharm project.
dll_name = 'TestUDll.dll'

if "__file__" in vars():
    # If this is script then start with the path to it because its a more consistent reference
    starting_dir = os.path.split(__file__)[0]
else:
    # Otherwise use the cwd, which depends now how this script was invoked, but
    starting_dir = os.getcwd()


path_to_dll = os.path.join(up_path(starting_dir, 1), "TestUDll", "Debug", dll_name)

if not os.path.isfile(path_to_dll):
    raise Exception('Can not locate file "%s" on path "%s' % (dll_name, path_to_dll))

#path_to_dll = r'C:\Users\Allen W. Ingling\Projects\TestUDll\Debug\TestUDll.dll'

#dll = ctypes.windll.LoadLibrary(path_to_dll)
dll = ctypes.CDLL(path_to_dll)

#dll.TimesTwo.argtypes(ctypes.c_double, ctypes.c_double)
x = ctypes.c_double(44.4)
y = ctypes.c_double(66.6)
dll.TimesTwo.restype = ctypes.c_double
z = dll.TimesTwo(x, y)
print(z)


