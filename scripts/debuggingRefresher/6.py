from pwn import *

elf = ELF("/challenge/embryogdb_level6")
p = elf.process()

# Run 
p.sendline(b"r")
p.recvuntil(b"(gdb) ")
# Set breakpoint before the cmp
p.sendline(b"b *main+686")
p.recvuntil(b"(gdb) ")
# Start exec
p.sendline(b"c")

for i in range(64):
    # Random value
    p.sendline(b"12")
    p.recvuntil(b"(gdb) ")
    # We're in the breakpoint
    p.sendline(b"set $rax=$rdx")
    p.sendline(b"c")

p.interactive()
