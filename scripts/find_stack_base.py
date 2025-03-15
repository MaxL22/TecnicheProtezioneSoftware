#!/usr/bin/python3

from pwn import *

# Path dell'eseguibile
elf = ELF('')

# Altrimenti il programma non fornisce il core dump quando crasha
io = elf.process(setuid=False)

# Dimensione
io.sendline(b'500')

# Generate cyclic string
io.sendline(cyclic(512, n=8))

io.wait()
print(hex(io.corefile.fault_addr))
print(cyclic_find(io.corefile.fault_addr, n=8))

