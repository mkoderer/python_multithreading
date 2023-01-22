all: c_mem_alloc c_mem_alloc_no_free
c_mem_alloc: c_mem_alloc.c
	gcc c_mem_alloc.c -o c_mem_alloc
clean:
	rm -f c_mem_alloc c_mem_alloc_no_free

c_mem_alloc_no_free: c_mem_alloc_no_free.c
	gcc c_mem_alloc_no_free.c -o c_mem_alloc_no_free
