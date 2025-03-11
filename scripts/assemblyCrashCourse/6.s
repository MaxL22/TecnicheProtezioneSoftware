.intel_syntax noprefix
.global _start
_start:

mov     rdx, 0
mov     rax, rdi
div     rsi
mov     rax, rdx
