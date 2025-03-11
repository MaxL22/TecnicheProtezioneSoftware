.intel_syntax noprefix
.global _start
_start:

jmp     target
.rept   0x51
nop
.endr
target:
pop     rdi
mov     rax, 0x403000
jmp     rax
