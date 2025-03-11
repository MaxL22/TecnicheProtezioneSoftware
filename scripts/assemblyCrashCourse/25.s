.intel_syntax noprefix
.global _start
_start:

mov     rax, 0x0
mov     rbx, 0x0
mov     ebx, 0x7f454c46
cmp     [rdi], ebx
jz      sum
mov     ebx, 0x00005A4D
cmp     [rdi], ebx 
jz      subtract
jmp     multiply

sum:
mov     eax, [rdi+4]
add     eax, [rdi+8]
add     eax, [rdi+12]
jmp     done

subtract:
mov     eax, [rdi+4]
sub     eax, [rdi+8]
sub     eax, [rdi+12]
jmp     done

multiply:
mov     eax, [rdi+4]
imul    eax, [rdi+8]
imul    eax, [rdi+12]

done:
