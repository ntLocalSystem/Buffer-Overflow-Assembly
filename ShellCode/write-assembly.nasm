global _start

section .text
_start:
    jmp short Call_Shellcode

Shellcode:

    ; Write syscall
    xor eax, eax
    mov al, 0x04
    xor ebx, ebx
    mov bl, 0x01
    pop ecx
    xor edx, edx
    mov dl, 0x12
    int 0x80

    ; prepare for exit() syscall
    xor eax, eax
    mov al, 0x1
    xor ebx, ebx
    int 0x80


Call_Shellcode:
    call Shellcode
    message: db 'Inside Shellcode!', 0xA
