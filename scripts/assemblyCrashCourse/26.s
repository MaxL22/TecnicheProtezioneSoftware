.intel_syntax noprefix
.global _start
_start:


sub     rdi, 4
js      table
jmp     [rsi + 32]

table:
add     rdi, 4
jmp     [rsi + rdi*8]
