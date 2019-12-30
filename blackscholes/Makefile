#
# Copyright 2014-2015 NVIDIA Corporation. All rights reserved
#
INCLUDES=-I/usr/local/cuda/extras/CUPTI/include

ifndef OS
 OS   := $(shell uname)
 HOST_ARCH := $(shell uname -m)
endif

ifeq ($(OS),Windows_NT)
    export PATH := $(PATH):../../libWin32:../../libx64
    LIBS= -lcuda -L ../../libWin32 -L ../../libx64 -lcupti
    OBJ = obj
else
    ifeq ($(OS), Darwin)
        export DYLD_LIBRARY_PATH := $(DYLD_LIBRARY_PATH):../../lib
        LIBS= -Xlinker -framework -Xlinker cuda -L ../../lib -lcupti
    else
        export LD_LIBRARY_PATH := $(LD_LIBRARY_PATH):../../lib:../../lib64
        LIBS= -lcuda -L ../../lib -L /usr/local/cuda/extras/CUPTI/lib64 -lcupti
    endif
    OBJ = o
endif

libpcsampling.so: pc_sampling.$(OBJ)
	nvcc -shared -o $@ pc_sampling.$(OBJ) $(LIBS)

pc_sampling.$(OBJ): pc_sampling.cu
	nvcc -Xcompiler -fPIC -arch=sm_52 -lineinfo  -c $(INCLUDES) $<

clean:
	rm -f libpcsampling.so pc_sampling.$(OBJ)

