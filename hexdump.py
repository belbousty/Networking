import sys 
import socket
import threading

 
HEX_FILTER = "".join([(len(repr(chr(i))) == 3) and chr(i) or '.' for i in range(256)]) 

# ASCII printable characters from 0 to 255, non printable = '.'
# length of printable characters is 3
# and This is how it look like :  
    # "................................ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRS
    # TUVWXYZ[.]^_`abcdefghijklmnopqrstuvwxyz{|}~..................................¡¢£¤¥¦§¨
    # ©ª«¬.®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿ"

def hexdump(src, length=16):
    if isinstance(src, bytes):
        src = src.decode()
    results = []
    for i in range(0, len(src), length):
        word = str(src[i:i+length])
        hexa = ' '.join([f'{ord(c):02X}' for c in word])
        hexwidth = length*3
        results.append(f'{i:04x} {hexa:<{hexwidth}} {word}') 
    for line in results:
        print(line) 
    return results

if __name__ == '__main__':
    src = "Hi there! This is an implementation of a hexdump using python"
    print(HEX_FILTER)
