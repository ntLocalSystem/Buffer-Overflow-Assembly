; execve-assembly-stack.nasm

global _start

section .text
_start:
    ; edx - envp
    xor edx, edx
    push edx
    mov edx, esp

    ; Prepare ecx (argv) for later
    xor ecx, ecx
    push ecx
    mov ecx, esp

    ; Prepare ebx - (pathname)
    xor ebx, ebx
    push ebx

    ; push the string into the stack
    ; "/bin//sh" - Extra slash to make it align
    ; with boundary of 4.
		mov dword [esp-4], 0x68732f2f
		mov dword [esp-8], 0x6e69622f
    sub esp, 0x8

    mov ebx, esp


    ; Finalize ecx
    mov DWORD [ecx], ebx

    ; Prepare eax - 11 (execve)
    xor eax, eax
    mov al, 0xB

    ; System Call
    int 0x80