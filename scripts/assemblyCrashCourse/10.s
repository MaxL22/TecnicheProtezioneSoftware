.intel_syntax noprefix
.global _start
_start:

and     rdi, rsi
and     rax, 0
or      rax, rdi
