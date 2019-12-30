from cffi import FFI
ffibuilder = FFI() 
ffibuilder.cdef("void initTrace(); void finiTrace();") 
ffibuilder.set_source("_cupti_cffi", "void initTrace(); void finiTrace();",
                      libraries=['pcsampling']) 

ffibuilder.compile(verbose=True)
