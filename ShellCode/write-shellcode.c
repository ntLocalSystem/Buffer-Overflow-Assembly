#include <stdio.h>
#include <string.h>

int main(int argc, char* argv[]){

    // Shell code
    unsigned char shell_code[] = \
        "\x68\x72\x6c\x64\x0a\x68\x6f\x20\x57\x6f\x68\x48\x65\x6c\x6c\x31\xc0\xb0\x04\x31\xdb\xb3\x01\x89\xe1\x31\xd2\xb2\x0c\xcd\x80\x31\xc0\xb0\x01\x31\xdb\xcd\x80";

    printf("Shellcode size: %d\n", strlen(shell_code));

    // Get a function pointer to the shell code
    void (*shellCodePtr)() = (void(*)())shell_code;

    // Call the shell code
    shellCodePtr();

    return 0;
}