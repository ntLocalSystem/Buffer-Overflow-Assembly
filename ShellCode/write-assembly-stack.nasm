global _start

section .text
_start:
    ; push the string into the stack
    ; "Hello World!\n"
    push 0x0a646c72
    push 0x6f57206f
    push 0x6c6c6548

    ; Write syscall
    xor eax, eax
    mov al, 0x4
    xor ebx, ebx
    mov bl, 0x1
    mov ecx, esp
    xor edx, edx
    mov dl, 0xc
    int 0x80

    ; Exit gracefully
    xor eax, eax
    mov al, 0x1
    xor ebx, ebx
    int 0x80