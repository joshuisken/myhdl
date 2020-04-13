IVVP ?= iverilog-vpi

all: myhdl.vpi

myhdl.vpi: myhdl.c myhdl_table.c
	$(IVVP) myhdl.c myhdl_table.c

.PHONY: test
test: myhdl.vpi
	cd test && python test_all.py

clean:
	-rm myhdl.vpi $(wildcard *.o *~)

