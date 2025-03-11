.intel_syntax noprefix
.global _start
_start:

and     rax, 0x0
and     rbx, 0x0
and     rcx, 0x0
and     rdx, 0x0
mov     al, [0x404000]
mov     bx, [0x404000]
mov     ecx, [0x404000]
mov     rdx, [0x404000]
