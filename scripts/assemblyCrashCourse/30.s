mov     rbp, rsp
sub     rsp, 0x100
mov     r8, 0x0

mov     r9, 0x0
mov     r13, 0x1

loop1:
cmp     r8, rsi
jg      smth

mov     r9b, [rdi + r8]

mov     r12, rsp
add     r12, r9
add     byte ptr [r12], 1

add     r8, 1

jmp     loop1

smth:

mov     rcx, 0x0
mov     rbx, 0x0
mov     rax, 0x0

loop2:
cmp     rcx, 0xff
jg      done

mov     r12, rsp
add     r12, rcx

cmp     [r12], bl
jg      update
jmp     endl

update:
mov     bl, [r12]
mov     rax, rcx
jmp     endl

endl:
add     rcx, 0x1
jmp     loop2

done:
mov     rsp, rbp
ret
