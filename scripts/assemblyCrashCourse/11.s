.intel_syntax noprefix
.global _start
_start:

and     rdi, 0x1
and     rax, 0x0
or      rax, rdi
xor     rax, 0x1
