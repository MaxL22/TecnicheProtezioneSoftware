.intel_syntax noprefix
.global _start
_start:
mov rax, 60
mov rdi, rsi
syscall
