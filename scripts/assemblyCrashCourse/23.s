.intel_syntax noprefix
.global _start
_start:

jmp     target
.rept   0x51
nop
.endr
target:
mov     rax, 0x1
