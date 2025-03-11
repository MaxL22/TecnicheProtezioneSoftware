.intel_syntax noprefix
.global _start
_start:

mov     rax, 0
mov     rbx, 0
mov     rdx, 0

loop:
add     rax, [rdi + rbx*8]
add     rbx, 1
cmp     rsi, rbx
jnz     loop

div     rbx
