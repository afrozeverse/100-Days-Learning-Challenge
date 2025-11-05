from ctypes import *
#this is the path where my library is. Full path has to given
c_library_path=R"C:\Mysirg\100 Days Learning Challenge\Day31_callCFromPython\myLibrary.dll"
#Now we will make an python object, and fill the object with my c library, name of the object could be anything
my_library=CDLL(c_library_path)

p=my_library.fact(10)
print(p)