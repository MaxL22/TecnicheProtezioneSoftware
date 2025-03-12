.intel_syntax noprefix
.global _start 

str_lower:
mov     r8, 0
mov     r9, rdi
mov     rcx, 0x403000

cmp     r9, 0x0
jz      done

loop:
mov     rbx, 0x00
cmp     bl, [r9]
jz      done

mov     bl, [r9]
cmp     bl, 0x5a
ja      cont

mov     rdi, [r9]
call    rcx

mov     [r9], rax
add     r8, 1
jmp     cont

cont:
add     r9, 1
jmp     loop

done:
mov     rax, r8
ret 
