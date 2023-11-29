#include <stdio.h>
#include <string.h>

int main(int argc, char* argv[]){

    // Shell code
    unsigned char shell_code[] = \
        "SHELLCODEHERE";
    
    // Shell code length
    printf("Shellcode Length: %d\n", strlen(shell_code));

    // Get a function pointer to the shell code
    void (*shellCodePtr)() = (void(*)())shell_code;

    // Call the shell code
    shellCodePtr();

    return 0;
}