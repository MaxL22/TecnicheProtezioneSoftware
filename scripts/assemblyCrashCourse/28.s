.intel_syntax noprefix
.global _start
_start:

mov     rax, 0x0
mov     rcx, 0x0

cmp     rdi, 0
jz      done

loop:
cmp     [rdi + rax], cl
jz      done
add     rax, 1
jmp     loop

done:
