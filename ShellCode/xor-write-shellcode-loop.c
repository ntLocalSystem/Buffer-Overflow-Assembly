#include <stdio.h>
#include <string.h>

int main(int argc, char* argv[]){

    // Shell code
    unsigned char shell_code[] = \
        "\xeb\x0f\x80\x36\xaa\x46\xe2\xfa\xeb\x0c\x5e\x31\xc9\xb1\x31\xeb\xf1\xe8\xf4\xff\xff\xff\x41\xbd\x9b\x6a\x1a\xae\x9b\x71\x19\xab\xf3\x9b\x78\x18\xb8\x67\x2a\x9b\x6a\x1a\xab\x9b\x71\x67\x2a\x42\x4e\x55\x55\x55\xe3\xc4\xd9\xc3\xce\xcf\x8a\xf9\xc2\xcf\xc6\xc6\xc9\xc5\xce\xcf\x8b\xa0";

    printf("Shellcode length is: %d\n", strlen(shell_code));

    // Get a function pointer to the shell code
    void (*shellCodePtr)() = (void(*)())shell_code;

    // Call the shell code
    shellCodePtr();

    return 0;
}


